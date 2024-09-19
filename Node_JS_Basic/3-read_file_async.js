const fs = require('fs');

function countStudents(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf-8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const lines = data.split('\n');
      
      const validLines = lines.filter(line => line.trim() !== '');
      
      if (validLines.length <= 1) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const totalStudents = validLines.length - 1;
      console.log(`Number of students: ${totalStudents}`);

      const fields = {};

      for (let i = 1; i < validLines.length; i++) {
        const studentInfo = validLines[i].split(',');

        if (studentInfo.length !== 4) continue;

        const firstname = studentInfo[0];
        const field = studentInfo[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstname);
      }

      for (const field in fields) {
        const studentsInField = fields[field];
        console.log(
          `Number of students in ${field}: ${studentsInField.length}. List: ${studentsInField.join(', ')}`
        );
      }

      resolve();
    });
  });
}

module.exports = countStudents;
