class Student:
    
    grade = 0
    passingScore = 75
    awardCredit = True
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + '@weber.edu'
    
    def printStudentInfo(self): #Run this without self to show parameters issue
        print ("Student: " + self.first + ' ' + self.last + ' \nEmail: ' + self.email + ' \nGrade: ' + str(self.grade) + "\nAward Credit: " + str(self.awardCredit) + '\n')

    def setGrade(self, grade):
        self.grade = grade
        if self.grade < self.passingScore:
            self.awardCredit = False
        else:
            self.awardCredit = True
    
    def extraCredit(self, points):
        newGrade = self.grade + points
        return newGrade

student_W_1234 = Student("Scott", "Hadzik")
student_W_1235 = Student("Waldo", "Wildcat")

print('Start of Semester')
print('-----------------')
student_W_1234.printStudentInfo()

print('Middle of Semester')
print('-----------------')
student_W_1234.setGrade(65)
student_W_1234.printStudentInfo()


print('End of Semester')
print('-----------------')
student_W_1234.setGrade(student_W_1234.extraCredit(11))
student_W_1234.printStudentInfo()



# student_W_1234.printStudentInfo()
# student_W_1235.printStudentInfo()


# student_W_1234.printStudentInfo()
# student_W_1235.printStudentInfo()

# print (student_W_1234.__dict__)
# print (Student.__dict__)

