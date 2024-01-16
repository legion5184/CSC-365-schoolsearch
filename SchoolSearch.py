class Student:

    def __init__(self, Student):
        self.StLastName = Student[0]
        self.StFirstName = Student[1]
        self.Grade = int(Student[2])
        self.Classroom = int(Student[3])
        self.Bus = int(Student[4])
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
        print(
            f"{self.StLastName},{self.StFirstName},{self.Grade},{self.Classroom},{self.Bus},{self.GPA},{self.TLastName},{self.TFirstName}")


if __name__ == '__main__':
    Students = []

    file = open("students.txt", 'r')
    while True:
        content = file.readline()
        if not content:
            break
        std_info = content.split(",")
        Students.append(Student(std_info))

    file.close()

    while True:
        user_input = input("Input:\n").strip().split()

        # Quit
        if user_input[0] == "Q" or user_input[0] == "Quit":
            break

        if user_input[0] == "I" or user_input[0] == "Info":
            # Create info array
            info_arr = [0, 0, 0, 0, 0, 0, 0]
            # Create Grade information
            for index in range(len(Students)):
                info_arr[int(Students[index].Grade)] += 1
            # Print information to Console
            for index in range(len(info_arr)):
                print(f"{index}: {info_arr[index]}")

        # Bus
        if user_input[0] == "B" or user_input[0] == "Bus":
            # If incorrect args amount, do nothing
            if len(user_input) < 2:
                pass
            # Iterate through Students
            else:
                for item in Students:
                    if item.Bus == int(user_input[1]):
                        print(f"{item.StLastName}, {item.StFirstName}, {item.Grade}, {item.Classroom}")

        # Average
        if user_input[0] == "A" or user_input[0] == "Average":
            pass

        if user_input[0] == "T" or user_input[0] == "Teacher":
            # Teacher Action goes here
            pass

        if user_input[0] == "S" or user_input[0] == "Student":
            try:
                if user_input[2] == "B" or user_input[2] == "Bus":
                    # put bus option for student here
                    pass
            except IndexError:
                # put no bus option for student here:
                pass

        if user_input[0] == "G" or user_input[0] == "Grade":
            try:
                if user_input[2] == "H" or user_input[2] == "High":
                    # put High option for Grade here
                    pass
                if user_input[2] == "L" or user_input[2] == "Low":
                    # put low option for grade here
                    pass
            except IndexError:
                # put no bound option for grade here
                pass
