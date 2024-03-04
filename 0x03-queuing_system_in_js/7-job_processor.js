import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Create a queue
const queue = kue.createQueue();

// Function to send notification
function sendNotification(phoneNumber, message, job, done) {
  // Track job progress
  job.progress(0, 100);

  // If phone number is blacklisted, fail the job
  if (blacklistedNumbers.includes(phoneNumber)) {
    job.failed( new Error(`Phone number ${phoneNumber} is blacklisted`));
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  // Update job progress
  job.progress(50, 100);

  // Log message
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  // Job is done
  done();
}

// Process jobs from the 'push_notification_code_2' queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
