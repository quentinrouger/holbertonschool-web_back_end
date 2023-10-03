export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const grade = newGrades.find((element) => element.studentId === student.id);
      return {
        ...student,
        grade: grade === undefined ? 'N/A' : grade.grade,
      };
    });
}
