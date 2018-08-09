from student import Student

students = []

for i in range(3):
    name = str(input("Name: "))
    dorm = str(input("Name: "))
    s = Student(name, dorm)
    students.append(s)
for student in students:
    print(f"{student.name} lives in {student.dorm}")
