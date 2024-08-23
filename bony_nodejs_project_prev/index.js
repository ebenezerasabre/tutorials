const express = require('express');
const path = require('path');
const app = express();
const bodyParser = require('body-parser');
const routes = require('./src/routes');
const patientService = require('./src/services/patient.service');
const patientModel = require('./src/models/patient.model');


app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use('/api', routes);    // use Routes



// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a route for the root URL ("/")
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.get('/record', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'record.html'));
});


app.get('/injured', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'injured.html'));
});

app.post('/submit', async (req, res) => {
    const userData = req.body;
    try{
        console.log(userData);
        
        const data = await patientModel.createPatient(userData);
        // console.log(userData);
        // res.sendFile(path.join(__dirname, 'public', 'record.html'));
        console.log('Form submitted successfully' + data);
        // res.sendFile(path.join(__dirname, 'public', 'index.html'));
    } catch (err){
        res.status(500).send('Error submitting form');
    }
});

// Serve static files from the "public" directory
//app.use(express.static(path.join(__dirname, 'public/views')));


// Set up a view engine if using one (e.g., EJS, Pug)
app.set('view engine', 'ejs'); // Change to your template engine
app.set('views', './public/views'); // Directory for EJS templates


// Route to serve HTML and inject data
// Route to serve HTML and inject data
app.get('/data', async (req, res) => {
    try {
        //const data = await patientService.getAllPatients();
        const data = await patientModel.getAllPatients();
        res.render('index', { data }); // Assuming you're using a template engine
    } catch (error) {
        res.status(500).send('Error retrieving data');
    }
});


app.get('/datax', async (req, res) => {
    try {
        //const data = await patientService.getAllPatients();
        const data = await patientModel.getAllPatients();
        res.render('extra', { data }); // Assuming you're using a template engine
    } catch (error) {
        res.status(500).send('Error retrieving data');
    }
});






// Start the server
app.listen(3000, () => {
    console.log('Server is running on port 3000');
});




