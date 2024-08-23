const patientService = require('../services/patient.service');



exports.createPatient = async (req, res) => {
 
    try {
      const patient = await patientService.createPatient(req.body);
      res.status(201).json(patient);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  
  };

exports.getAllPatients = async (req, res) => {
    try {
      const patients = await patientService.getAllPatients();
      res.status(200).json(patients);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  exports.getPatientById = async (req, res) => {
    try {
      const patient = await patientService.getPatientById(req.params.id);
      if (!patient) {
        return res.status(404).json({ message: 'Patient not found' });
      }
      res.status(200).json(patient);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };


exports.getPatientsByStatus = async (req, res) => {
    try {
      const status = req.query.status;
      const patients = await patientService.getPatientsbyStatus(status);
      res.status(200).json(patients);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };

  exports.approvePatient = async (req, res) => {
    try {
      const pid = req.query.pid;
      const status = req.query.status;
      console.log(pid + ", " + status);
      const patient = await patientService.approvePatient(pid, status);
      if (!patient) {
        return res.status(404).json({ message: 'Patient not found' });
      }
      res.status(200).json(patient);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };
  

exports.deletePatient = async (req, res) => {
    try {
      const patient = await patientService.deletePatient(req.params.id);
      res.status(200).json(patient);
    } catch (error) {
      res.status(500).json({ message: error.message });
    }
  };
  
  