students = []


def read_file():
    try:
        f = open("students.txt","r")
        for student in read_students(f):
##        for student in f.readlines():
##            students.add_student(student)
              students.append(student)
        f.close()
    except Exception:
        print("Could not read file.")


def read_students(f):
    for line in f:
        yield line


read_file()
print(students)
