const express = require('express');
const fs = require('fs');
const path = require('path');

const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const databasePath = process.argv[2];

  countStudents(databasePath)
    .then((output) => {
      res.write('This is the list of our students\n');
      res.write(output);
      res.end();
    })
    .catch((error) => {
      res.status(500).send('Cannot load the database');
    });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
