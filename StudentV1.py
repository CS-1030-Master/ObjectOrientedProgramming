class Student:
    pass

student_W_1234 = Student()
student_W_1235 = Student()

print(student_W_1234)
print(student_W_1235)

student_W_1234.first = "Scott"
student_W_1234.last = "Hadzik"
student_W_1234.email = "scotthadzik@weber.edu"
student_W_1234.grade = "Pass"


student_W_1235.first = "Waldo"
student_W_1235.last = "WildCat"
student_W_1235.email = "WaldoWildCat@weber.edu"
student_W_1235.status = "Pass"

print(student_W_1234.email)
print(student_W_1235.email)