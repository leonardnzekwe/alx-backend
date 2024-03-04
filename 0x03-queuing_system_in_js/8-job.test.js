import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', function () {
  let queue;

  // Set up the queue before running tests
  before(function () {
    // Create a new queue in test mode
    queue = kue.createQueue({ redis: { host: '127.0.0.1', port: '6379', auth: 'password', db: 3 } });
    queue.testMode.enter();
  });

  // Clear the queue and exit test mode after running tests
  after(function () {
    queue.testMode.exit();
  });

  it('should display an error message if jobs is not an array', function () {
    expect(() => createPushNotificationsJobs('not an array', queue)).to.throw('Jobs is not an array');
  });

  it('should create two new jobs to the queue', function () {
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153518781',
        message: 'This is the code 5678 to verify your account'
      }
    ];

    createPushNotificationsJobs(jobs, queue);

    // Assert that two jobs were created
    expect(queue.testMode.jobs.length).to.equal(2);

    // Assert that the jobs have the correct data
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);

    expect(queue.testMode.jobs[1].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
  });
});
