const updateStudentGradeByCity = (id, students) => {
  const getListStudents = students.filter.map((student) => student.id === id);

  return getListStudents;
};

export default getStudentIdsSum;
