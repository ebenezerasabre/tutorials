const pool = require('./db');


const createPatientTable = async () => {
    const query = `
        CREATE TABLE IF NOT EXISTS patient(
            id SERIAL PRIMARY KEY,
            injured_name VARCHAR(255) NOT NULL,
            dob VARCHAR(255) NOT NULL,
            injured_address TEXT,
            injured_occupation VARCHAR(255) NOT NULL,
            pot_name VARCHAR(255) NOT NULL,
            pot_contact TEXT,
            injury_description TEXT,
            news_link TEXT,
            family_contact TEXT,
            document TEXT,
            expenditure VARCHAR(255) NOT NULL,
            informant_contact TEXT,
            photo TEXT,
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
        INSERT INTO patient (injured_name, dob, injured_address, injured_occupation, pot_name, 
        pot_contact, injury_description, news_link, family_contact, document,
        expenditure, informant_contact, photo, status
        )
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, 'pending')
        RETURNING *;
      `;
      const values = [userData.injured_name, userData.dob, userData.injured_address, userData.injured_occupation, userData.pot_name,
        userData.pot_contact, userData.injury_description, userData.news_link, userData.family_contact, userData.document,
        userData.expenditure,  userData.informant_contact, userData.photo
      ];
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
      throw new Error(err);
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