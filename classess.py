students = []

class Student:
    def add_student(self, name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)
    ##    students.append(student) or  self.add_student() declaration


student = Student()
student.add_student("Mark")
student.add_student("Hemanth",9555)


print(students)
