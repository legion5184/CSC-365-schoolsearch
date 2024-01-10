class Student:

    def __init__(self, StLastName, StFirstName, Grade, Classroom, Bus, GPA, TLastName, TFirstName):
        self.StLastName = StLastName
        self.StFirstName = StFirstName
        self.Grade = Grade
        self.Classroom = Classroom
        self.Bus = Bus
        self.GPA = GPA
        self.TLastName = TLastName


if __name__ == '__main__':
    Students = []

    file = open("students.txt", 'r')
    while(True):
        content = file.readline()
        if not content:
            break
        std_info = content.split();
        Students.append(Student(std_info))

    file.close()





