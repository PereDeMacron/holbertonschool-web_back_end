// task 5
const http = require('http');
const fs = require('fs');
const path = require('path');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter(line => line.trim() !== '');
        const fields = {};
        let totalStudents = 0;

        for (let i = 1; i < lines.length; i++) {
          const studentData = lines[i].split(',');
          if (studentData.length === 4) {
            const field = studentData[3];
            if (!fields[field]) {
              fields[field] = [];
            }
            fields[field].push(studentData[0]);
            totalStudents++;
          }
        }

        let output = `Number of students: ${totalStudents}\n`;
        for (const [field, students] of Object.entries(fields)) {
          output += `Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`;
        }
        resolve(output.trim());
      }
    });
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.setHeader('Content-Type', 'text/plain');
    res.statusCode = 200;
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.setHeader('Content-Type', 'text/plain');
    countStudents(process.argv[2])
      .then((data) => {
        res.statusCode = 200;
        res.end(`This is the list of our students\n${data}`);
      })
      .catch((err) => {
        res.statusCode = 500;
        res.end(`This is the list of our students\n${err.message}`);
      });
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});

module.exports = app;
