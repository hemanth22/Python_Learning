students = []

class Student:
    def __init__(self, name, student_id=332):
        student = {"name": name, "student_id": student_id}
        students.append(student)
    ##    students.append(student) or  self.add_student() declaration


mark = Student("Mark")
hemanth = Student("Hemanth BITRA",9555)


print(students)
