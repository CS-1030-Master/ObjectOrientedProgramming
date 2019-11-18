class Student:
    
    numberOfStudents = 0
    
    grade = 0
    passingScore = 75
    awardCredit = True
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.email = first + last + '@weber.edu'
    
        Student.numberOfStudents +=1

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

    @classmethod
    def setPassingScore(cls, score):
        cls.passingScore = 65



