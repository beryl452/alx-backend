const kue = require('kue');
const queue = kue.createQueue();

// Tableau contenant les numéros de téléphone sur liste noire
const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];

/**
 * Envoie une notification push à un utilisateur.
 * @param {String} phoneNumber - Le numéro de téléphone de l'utilisateur
 * @param {String} message - Le message à envoyer
 * @param {Object} job - L'objet job de Kue
 * @param {Function} done - Fonction de rappel pour indiquer la fin du traitement
 */
const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
    done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

  done();
};

queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
  });
  