# Simple Solitaire Game

# Import Dependencies
from StudentV6 import Student

# Play Solitaire!
def main():
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

    print(Student.numberOfStudents)

    print (Student.passingScore)
    print (student_W_1234.passingScore)


    Student.setPassingScore(65)
    print (Student.passingScore)
    print (student_W_1234.passingScore)

if __name__ == "__main__":
    main()