import kue from 'kue';

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach(jobData => {
    const job = queue.create('push_notification_code_3', jobData);

    // Handle successful job creation
    job.on('enqueue', () => {
      console.log(`Notification job created: ${job.id}`);
    });

    // Handle job completion
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    });

    // Handle job failure
    job.on('failed', (error) => {
      console.log(`Notification job ${job.id} failed: ${error}`);
    });

    // Handle job progress
    job.on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });

    // Save the job to the queue
    job.save();
  });
}

export default createPushNotificationsJobs;
