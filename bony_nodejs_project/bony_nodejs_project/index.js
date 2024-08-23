const express = require('express');
const path = require('path');
const app = express();
const bodyParser = require('body-parser');
const routes = require('./src/routes');
const patientService = require('./src/services/patient.service');
const patientModel = require('./src/models/patient.model');

const multer = require('multer');
const fs = require('fs');



app.use(bodyParser.json());

app.use(bodyParser.urlencoded({ extended: true }));

// Routes
app.use('/api', routes);    // use Routes






// Configure multer for storage
const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        // Use path to resolve the full directory path
        cb(null, path.join(__dirname, './pics')); // Directory where files will be stored temporarily
    },
    filename: function (req, file, cb) {
        // Corrected Date.now() typo and file naming convention
        cb(null, Date.now() + '-' + file.originalname); // Naming files uniquely
    }
});




//const upload = multer({ storage: storage }).single('photo'); // Only handles the 'photo' field

const upload = multer({ storage: storage }).fields([
  
    { name: 'injured_name' },
    { name: 'dob' },
    { name: 'NID' },
    { name: 'injured_address' },
    { name: 'division' },
    { name: 'district' },
    { name: 'occupation' },

    { name: 'jobplace' },
    { name: 'expenditure' },
    { name: 'paymentOption' },
    { name: 'paymentField' },

    { name: 'family_phone' },
    { name: 'info_provider' },
    { name: 'hospital' },
    { name: 'hospital_contact' },
    { name: 'injury_description' },
    { name: 'news_link' },
    { name: 'document', maxCount: 2 },
    { name: 'photo', maxCount: 2 } // Adjust maxCount based on your requirement
  ]);

app.post('/upload', async (req, res) => {
    upload(req, res, async function (err) {
      if (err instanceof multer.MulterError) {
        // A Multer error occurred when uploading.
        return res.status(500).json({ error: err.message });
      } else if (err) {
        // An unknown error occurred when uploading.
        return res.status(500).json({ error: 'Unknown error occurred' });
      }

       // Everything went fine.
    if (req.files && req.files['photo']) {
     
        const photoPaths = req.files['photo'].map(file => file.path).join(',');
        const documentPaths = req.files['document'].map(file => file.path).join(',');

        const userData = {
            injured_name: req.body.injured_name,
            dob: req.body.dob,
            NID: req.body.NID,
            injured_address: req.body.injured_address,
            division: req.body.division,
            district: req.body.district,
            occupation: req.body.occupation,
            jobplace: req.body.jobplace,
            expenditure: req.body.expenditure,
            paymentOption: req.body.paymentOption,
            paymentField: req.body.paymentField,
            family_phone: req.body.family_phone,
            info_provider: req.body.info_provider,
            hospital: req.body.hospital,
            hospital_contact: req.body.contact_hospital,
            injury_description: req.body.injury_description,
            news_link: req.body.news_link,
            photo: photoPaths,
            document: documentPaths
        };
        
        // console.log("userData: ", userData);
        submitPatientData(userData);


        res.send('Upload successful!');
      } 
      // Everything went fine.
    
    
       else {
        res.send('No photo uploaded');
      }
    });
  });



  async function submitPatientData(userData) {
    try {
        // Log the user data
        console.log(userData);

        // Insert the data into the patient table
        const data = await patientModel.createPatient(userData);

        // Log the success message with the returned data
        console.log('Form submitted successfully:', data);

        // Optionally send a response or redirect the user to another page
        // res.sendFile(path.join(__dirname, 'public', 'record.html'));

    } catch (err) {
        // Handle errors and send a 500 status code with an error message
        console.error('Error submitting form:', err.message);
    }
}


/*



const uploadx = multer({ storage: storage }).fields([
    { name: 'photo', maxCount: 10 },
    { name: 'document', maxCount: 10 }
  ]);

// Handle the form submission

// Handle the form submission
app.post('/uploax', uploadx.fields([{ name: 'photo', maxCount: 10 }, { name: 'document', maxCount: 10 }]), async (req, res) => {
    console.log(req.body);
    try {
      const { 
                injured_name, 
                dob, 
                NID,
                injured_address,
                division,
                district,
                occupation,
                
                jobplace,
                expenditure,
                paymentOption,
                paymentField,

                family_phone,
                info_provider,
                hospital,
                contact_hospital,
                injury_description,
                news_link,
                document,
                photo
            } = req.body;
      const photoFiles = req.files['photo'] || [];
      const documentFiles = req.files['document'] || [];
  
      // Save file paths in the database
      const photoPaths = photoFiles.map(file => file.path).join(',');
      const documentPaths = documentFiles.map(file => file.path).join(',');
  
    
      const query = `
        INSERT INTO your_table_name (injured_name, dob, injured_address, photo, document)
        VALUES ($1, $2, $3, $4, $5)
        RETURNING id;
      `;
      const values = [injured_name, dob, injured_address, photoPaths, documentPaths];
      const result = await pool.query(query, values);
  
      res.status(200).send('Files uploaded and data saved successfully!');

      
    } catch (error) {
      console.error('Error uploading files and saving data:', error);
      res.status(500).send('Internal Server Error');
    }
  });
  

  */


// Serve static files from the "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Define a route for the root URL ("/")
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'Home.html'));
});

app.get('/record', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'record.html'));
});


app.get('/injured', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'injured.html'));
});

app.get('/traitor', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'record_traitor'));
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




