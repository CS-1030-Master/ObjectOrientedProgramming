class Student:
    def __init__(self, first, last, grade):
        self.first = first # These are instance variables
        self.last = last
        self.grade = grade
        self.email = first + last + '@weber.edu'


student_W_1234 = Student("Scott", "Hadzik", 65)
student_W_1235 = Student("Waldo", "Wildcat", 75)

print ("Student: " + student_W_1234.first + ' ' + student_W_1234.last + ' \nEmail: ' + student_W_1234.email + ' \nGrade: ' + str(student_W_1234.grade) + '\n')
print ("Student: " + student_W_1235.first + ' ' + student_W_1235.last + ' \nEmail: ' + student_W_1235.email + ' \nGrade: ' + str(student_W_1235.grade) + '\n')