students = []

class Student:

    school_name = "Springfield Elementary"

    def __init__(self, name, student_id=332):
        self.name = name
        student = {"name": name, "student_id": student_id}
        students.append(student)
    ##    students.append(student) or  self.add_student() declaration

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name

# mark = Student("Mark")
# print(mark)

print(Student.school_name)
