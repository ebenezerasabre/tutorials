const express = require('express');
const router = express.Router();

const patientRoutes = require('./patient.route'); // Import routes

// Use the routes as middleware
router.use('/patient', patientRoutes);

module.exports = router; // Export the router
