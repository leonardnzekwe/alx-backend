import redis from 'redis';
import { promisify } from 'util';

// Create a Redis client
const client = redis.createClient();

// Promisify Redis client functions
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

// Handle connection event
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Handle error event
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Function to set a new school value in Redis
async function setNewSchool(schoolName, value) {
  await setAsync(schoolName, value);
  console.log('Reply: OK');
}

// Function to display the value for a given school name
async function displaySchoolValue(schoolName) {
  try {
    const value = await getAsync(schoolName);
    console.log(value);
  } catch (error) {
    console.error(error);
  }
}

// Call the functions as required
(async () => {
  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
