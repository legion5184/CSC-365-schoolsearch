class Student:

    def __init__(self, Student):
        self.StLastName = Student[0]
        self.StFirstName = Student[1]
        self.Grade = Student[2]
        self.Classroom = Student[3]
        self.Bus = Student[4]
        self.GPA = float(Student[5])
        self.TLastName = Student[6]
        self.TFirstName = Student[7]

    def getStLastName(self):
        return self.StLastName

    def getStFirstName(self):
        return self.StFirstName

    def getGrade(self):
        return self.Grade
    def getClassroom(self):
        return self.Classroom

    def getBus(self):
        return self.Bus

    def getGPA(self):
        return self.GPA

    def getTLastName(self):
        return self.TLastName

    def getTFirstName(self):
        return self.TFirstName
    def printStudent(self):
        print(f"{self.StLastName},{self.StFirstName},{self.Grade},{self.Classroom},{self.Bus},{self.GPA},{self.TLastName},{self.TFirstName}")



if __name__ == '__main__':
    Students = []

    file = open("students.txt", 'r')
    while(True):
        content = file.readline()
        if not content:
            break
        std_info = content.split(",")
        Students.append(Student(std_info))

        Students[0].printStudent()

    file.close()



