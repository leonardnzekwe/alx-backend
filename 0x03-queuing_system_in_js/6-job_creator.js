import kue from 'kue';

// Create a job queue
const queue = kue.createQueue();

// Create an object containing the job data
const jobData = {
  phoneNumber: '1234567890',
  message: 'Hello from the job creator!',
};

// Create a job in the queue
const job = queue.create('push_notification_code', jobData);

// Handle successful job creation
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

// Handle job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Handle job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
