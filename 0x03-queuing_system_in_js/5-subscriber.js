import redis from 'redis';

// Create a Redis subscriber client
const subscriber = redis.createClient();

// Handle connection event
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle error event
subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the channel 'holberton school channel'
subscriber.subscribe('holberton school channel');

// Listen for messages on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
