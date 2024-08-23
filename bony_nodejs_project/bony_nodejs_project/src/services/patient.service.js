const patientModel = require('../models/patient.model');

exports.getAllPatients = async () => {
    try {
        return await patientModel.getAllPatients();
    } catch (err){
        throw new Error(err);
    }
};

exports.getPatientById = async (id) => {
    try {
        return await patientModel.getPatientById(id);
    } catch (err){
        throw new Error(err);
    }
};

exports.getPatientsbyStatus = async (status) => {
    try {
        return await patientModel.getPatientsByStatus(status);
    } catch (err){
        throw new Error(err);
    }
};

exports.createPatient = async (userData) => {
    try {
      return await patientModel.createPatient(userData);
    } catch (err) {
      throw new Error(err);
    }
  };

  exports.approvePatient = async (id, status) => {
    try {
      return await patientModel.approvePatient(id, status);
    } catch (err) {
      throw new Error(err);
    }
  };

  exports.deletePatient = async (id) => {
    try {
      return await patientModel.deletePatient(id);
    } catch (err) {
      throw new Error(err);
    }
  };
  
