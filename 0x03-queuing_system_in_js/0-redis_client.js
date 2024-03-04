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

// Close the Redis client when the script ends
process.on('SIGINT', () => {
  client.quit();
  process.exit();
});
