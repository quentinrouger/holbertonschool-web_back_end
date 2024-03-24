const fs = require('fs');

function countStudents(path) {
  try {
    const fileContent = fs.readFileSync(path, 'utf8');
    const lines = fileContent.trim().split('\n');

    const studentsData = [];
    const fieldsCount = {};

    for (const line of lines) {
      const [firstName, lastName, age, field] = line.split(',');

      if (firstName && lastName && age && field) {
        studentsData.push(
          {
            firstName, lastName, age, field,
          },
        );

        if (!fieldsCount[field]) {
          fieldsCount[field] = [];
        }

        fieldsCount[field].push(firstName);
      }
    }

    const totalStudents = studentsData.length - 1;
    console.log(`Number of students: ${totalStudents}`);

    for (const field in fieldsCount) {
      if (field !== 'field') {
        const fieldStudents = fieldsCount[field].length;
        const firstNameList = fieldsCount[field].join(', ');
        console.log(`Number of students in ${field}: ${fieldStudents}. List: ${firstNameList}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
