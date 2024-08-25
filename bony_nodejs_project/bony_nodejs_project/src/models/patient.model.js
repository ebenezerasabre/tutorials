const pool = require('./db');


const createPatientTable = async () => {
    const query = `
      CREATE TABLE IF NOT EXISTS patient(
          id SERIAL PRIMARY KEY,
          injured_name VARCHAR(255) NOT NULL,
          dob DATE,
          NID VARCHAR(255) NOT NULL,
          injured_address TEXT NOT NULL,
          division VARCHAR(255) NOT NULL,
          district VARCHAR(255) NOT NULL,
          occupation VARCHAR(255) NOT NULL,
          jobplace VARCHAR(255) DEFAULT '', 
          expenditure VARCHAR(255) DEFAULT '',
          paymentOption VARCHAR(255) DEFAULT '',
          paymentField VARCHAR(255) DEFAULT '',
          family_phone VARCHAR(255) NOT NULL,
          info_provider TEXT NOT NULL,
          hospital VARCHAR(255) NOT NULL,
          hospital_contact VARCHAR(255) NOT NULL,
          injury_description TEXT NOT NULL,
          news_link TEXT DEFAULT '',
          document TEXT DEFAULT '',
          photo TEXT NOT NULL,
          status VARCHAR(100) DEFAULT 'pending',
          created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `;
    await pool.query(query);
  };
  
createPatientTable();



const getAllPatients = async () => {
    try {
      const result = await pool.query('SELECT * FROM patient');
      return result.rows;
    } catch (err) {
      throw new Error(err);
    }
  };
  
  const getPatientById = async (id) => {
    try {
      const result = await pool.query('SELECT * FROM patient WHERE id = $1', [id]);
      return result.rows[0];
    } catch (err) {
      throw new Error(err);
    }
  };
  
  const getPatientsByStatus = async (status) => {
    try {
      const result = await pool.query('SELECT * FROM patient WHERE status = $1', [status]);
      return result.rows;
    } catch (err) {
      throw new Error(err);
    }
  };

const createPatient = async (userData) => {
    try {
      const query = `
          INSERT INTO patient (
                    injured_name,dob,NID,injured_address,division,district,occupation, 
                    jobplace,expenditure,paymentOption,paymentField,family_phone, info_provider, 
                    hospital, hospital_contact, injury_description, news_link, document,photo
                ) VALUES (
                    $1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19
                ) RETURNING id;
      `;

        const values = [
          userData.injured_name,
          userData.dob,
          userData.NID,
          userData.injured_address,
          userData.division,
          userData.district,
          userData.occupation,
          userData.jobplace,
          userData.expenditure,
          userData.paymentOption,
          userData.paymentField,
          userData.family_phone,
          userData.info_provider,
          userData.hospital,
          userData.hospital_contact,
          userData.injury_description,
          userData.news_link,
          userData.document,
          userData.photo
        ];

        console.log("from values", values);

      const result = await pool.query(query, values);
      return result.rows[0];
    } catch (err) {
      throw new Error(err);
    }
  };


  const approvePatient = async (pid, status) => {
    try {
      const query = `
        UPDATE patient SET
          status = $1
        WHERE id = $2
        RETURNING *;
      `;
      const values = [status, pid];
      const result = await pool.query(query, values);
      return result.rows[0];
    } catch (err) {
      throw new Error(err);
    }
  };
  

  const deletePatient = async (id) => {
    try {
      const query = 'DELETE FROM patient WHERE id = $1 RETURNING *;';
      const result = await pool.query(query, [id]);
      return result.rows[0];
    } catch (err) {
        console.error('Error executing query', err.stack);
        throw new Error(err.message);
    }
  };


  
  module.exports = {
    getAllPatients,
    getPatientById,
    getPatientsByStatus,
    createPatient,
    approvePatient,
    deletePatient
  };