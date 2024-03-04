import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Handle connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle error event
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Create Hash function
function createHash() {
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

// Display Hash function
function displayHash() {
  client.hgetall('HolbertonSchools', (error, reply) => {
    if (error) {
      console.error(error);
      return;
    }
    console.log(reply);
  });
}

// Call createHash and displayHash functions
createHash();
displayHash();
