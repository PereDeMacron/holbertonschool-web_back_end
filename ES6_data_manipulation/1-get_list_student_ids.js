<<<<<<< HEAD
const getListStudentIds = (listOfStudents) =>
  listOfStudents && Array.isArray(listOfStudents)
    ? listOfStudents.map((item) => item.id)
    : [];
=======
const getListStudentIds = (listOfStudents) => (listOfStudents && Array.isArray(listOfStudents)
  ? listOfStudents.map((item) => item.id) : []);
>>>>>>> 785fde4422097c905b97170e3a399823086cc999
export default getListStudentIds;
