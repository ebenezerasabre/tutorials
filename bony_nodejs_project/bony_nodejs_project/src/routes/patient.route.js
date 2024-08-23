const express = require('express');
const patientController = require('../controllers/patient.contoller');
const router = express.Router();

// create patient
router.post('/', patientController.createPatient);
router.get('/', patientController.getAllPatients);
router.get('/search', patientController.getPatientsByStatus);
router.get(':id', patientController.getPatientById);
router.get('/status', patientController.approvePatient);
router.delete('/:id', patientController.deletePatient);

module.exports = router;