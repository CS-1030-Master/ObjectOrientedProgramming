class Student:
    def __init__(self, first, last, grade):
        self.first = first
        self.last = last
        self.grade = grade
        self.email = first + last + '@weber.edu'
    
    def printStudentInfo(self): #Run this without self to show parameters issue
        print ("Student: " + self.first + ' ' + self.last + ' \nEmail: ' + self.email + ' \nGrade: ' + str(self.grade) + '\n')


student_W_1234 = Student("Scott", "Hadzik", "65")
student_W_1235 = Student("Waldo", "Wildcat", "75")

student_W_1234.printStudentInfo()
student_W_1235.printStudentInfo()

Student.printStudentInfo(student_W_1234) # alternate way to call the instance