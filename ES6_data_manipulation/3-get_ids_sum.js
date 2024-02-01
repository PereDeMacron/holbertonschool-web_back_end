const getStudentIdsSum = (id, students) => {
  const StudentIdsSum = students.filter(
    (student) => student.id === id
  );

  return StudentIdsSum;
};

export default getStudentIdsSum;
