const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON data
app.use(express.json());

// Endpoint to handle incoming data from ESP32
app.post('/submit_data', (req, res) => {
    const { temperature, humidity } = req.body;
    console.log(`Temperature: ${temperature}°C, Humidity: ${humidity}%`);
    res.status(200).send('Data received');
});

app.get('/', (req, res) => {
	res.status(200).send('Data received');
});

// Use 0.0.0.0 to listen on all network interfaces
app.listen(port, '0.0.0.0', () => {
    console.log(`Server running on http://0.0.0.0:${port}`);
});


//ssh ebenx@10.0.0.53
//password 1995































