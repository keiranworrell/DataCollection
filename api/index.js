const { Client } = require('pg');
const express = require('express')

const client = new Client({
    user: 'postgresadmin',
    host: '10.96.158.44',
    database: 'postgresdb',
    password: 'admin123',
    port: 30100,
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