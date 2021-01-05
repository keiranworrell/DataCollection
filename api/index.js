const { Client } = require('pg');
const express = require('express')

const client = new Client({
    user: 'postgresadmin',
    host: 'localhost',
    database: 'postgresdb',
    password: 'admin123',
    port: 5432,
});

const app = express()
const port = 8000;

app.get('/', (req, res) => {
    res.send('Hello World!')
});
  
app.listen(port, () => {
    console.log(`Listening on port ${port}`)
});

client.connect();