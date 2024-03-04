import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const queue = kue.createQueue();

const reserveSeat = (number) => {
  return new Promise((resolve, reject) => {
    client.set('available_seats', number, (err, reply) => {
      if (err) {
        reject(err);
      } else {
        resolve(reply);
      }
    });
  });
};

const getCurrentAvailableSeats = promisify(client.get).bind(client);

let reservationEnabled = true;

app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getCurrentAvailableSeats('available_seats');
  res.json({ numberOfAvailableSeats });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }
  
  const job = queue.create('reserve_seat').save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
    } else {
      res.json({ status: 'Reservation in process' });
    }
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentAvailableSeats = await getCurrentAvailableSeats('available_seats');
    const newAvailableSeats = parseInt(currentAvailableSeats) - 1;
    
    if (newAvailableSeats === 0) {
      reservationEnabled = false;
    }

    if (newAvailableSeats >= 0) {
      await reserveSeat(newAvailableSeats);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

app.listen(1245, async () => {
  await reserveSeat(50);
  console.log('Server is running on port 1245');
});
