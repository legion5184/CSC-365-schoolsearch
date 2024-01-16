class Student:

    def __init__(self, Student):
        self.StLastName = Student[0]
        self.StFirstName = Student[1]
        self.Grade = int(Student[2])
        self.Classroom = int(Student[3])
        self.Bus = int(Student[4])
        self.GPA = Student[5]
        self.TLastName = Student[6]
        self.TFirstName = Student[7]

    def printStudent(self):
        print(
            f"{self.StLastName},{self.StFirstName},{self.Grade},{self.Classroom},{self.Bus},{self.GPA},{self.TLastName},{self.TFirstName}")


if __name__ == '__main__':
    Students = []

    with open("students.txt", 'r') as file:
        for content in file:
            std_info = content.strip().split(",")
            Students.append(Student(std_info))

    while True:
        user_input = input("Input:\n").strip().split()
        user_input[0] = user_input[0].strip(':')

        # Quit
        if user_input[0] == "Q" or user_input[0] == "Quit":
            break

        # Info
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
            # Ensure user enters valid value
            try:
                grade_level = int(user_input[1])
            except ValueError:
                print("Enter a valid grade (non-decimal)")
                continue

            total = 0
            students = 0
            # If incorrect args amount, do nothing
            if len(user_input) < 2:
                pass
            # Iterate through students
            else:
                for item in Students:
                    if item.Grade == grade_level:
                        total += float(item.GPA)
                        students += 1
                if students == 0:
                    print("No students of that grade. Re-prompt")
                else:
                    print(f"{user_input[1]}, {(float(total) / float(students)):0.2f}")

        # Teacher
        if user_input[0] == "T" or user_input[0] == "Teacher":
            # Test correct args
            if len(user_input) < 2:
                pass
            # Iterate through list
            else:
                for item in Students:
                    if item.TLastName == user_input[1]:
                        print(f"{item.StLastName}, {item.StFirstName}")

        # Student
        if user_input[0] == "S" or user_input[0] == "Student":
            if len(user_input) == 1:
                pass
            elif len(user_input) <= 3:
                try:
                    if user_input[2] == "B" or user_input[2] == "Bus":
                        # Bus Option
                        for item in Students:
                            if item.StLastName == user_input[1]:
                                print(f"{item.StLastName},{item.StFirstName},{item.Bus}")
                except IndexError:
                    # No Bus Option
                    for item in Students:
                        if item.StLastName == user_input[1]:
                            print(
                                f"{item.StLastName},{item.StFirstName},{item.Grade},{item.Classroom}, {item.TLastName},{item.TFirstName}")

        # Grade
        if user_input[0] == "G" or user_input[0] == "Grade":
            if len(user_input) <= 3 and len(user_input) != 1:
                try:
                    # High Option
                    if user_input[2] == "H" or user_input[2] == "High":
                        high_set = set()
                        max_grade = 0
                        best_student = 0
                        for item in Students:
                            if (item.Grade == int(user_input[1])) and (float(item.GPA) > float(max_grade)):
                                max_grade = item.GPA
                                best_student = item

                        high_set.add(best_student)

                        for item in Students:
                            if (item.Grade == int(user_input[1])) and (float(item.GPA) == float(best_student.GPA)):
                                high_set.add(item)

                        try:
                            for student in high_set:
                                print(
                                    f"{student.StLastName}, {student.StFirstName}, {student.GPA}, "
                                    f"{student.TLastName}, {student.TFirstName}, {student.Bus}"
                                )
                        # case of incorrect grade input
                        except AttributeError:
                            pass
                    # Low Option
                    if user_input[2] == "L" or user_input[2] == "Low":
                        # put low option for grade here
                        low_set = set()
                        min_grade = 4
                        best_student = 0
                        for item in Students:
                            if (item.Grade == int(user_input[1])) and (float(item.GPA) < float(min_grade)):
                                min_grade = item.GPA
                                best_student = item

                        low_set.add(best_student)

                        for item in Students:
                            if (item.Grade == int(user_input[1])) and (float(item.GPA) == float(best_student.GPA)):
                                high_set.add(item)

                        try:
                            for student in low_set:
                                print(
                                    f"{student.StLastName}, {student.StFirstName}, {student.GPA}, "
                                    f"{student.TLastName}, {student.TFirstName}, {student.Bus}"
                                )
                        #case of incorrect grade input
                        except AttributeError:
                            pass
                except IndexError:
                    # No Bound Option
                    for item in Students:
                        if item.Grade == int(user_input[1]):
                            print(f"{item.StLastName}, {item.StFirstName}")
