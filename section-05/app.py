
student_list = []


def create_student():
    student_data = {}
    student_data['name'] = input("What is the student's name: ")
    student_data['marks'] = []
    return student_data


def add_mark(student, mark):
    student['marks'].append(mark)


def calculate_average_mark(student):
    total = sum(student['marks'])
    items = len(student['marks'])
    if items > 0 :
        return total/items
    return 0


def student_details(student):
    print(student['name'])


def print_student_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        student_details(student)


def menu():
    # Add a student (so a student_list)
    # Add a mark to a student
    # Print a list of students
    # Exit the application
    answ = 100
    while answ != 0:
        print("Student grading records")
        print("1 to add a student")
        print("2 to add a mark to a sduent")
        print("3 to print a list of students")
        print("0 to exit the application")
        answ = input("What would you like to do? ")
        if answ == "1":
            s = create_student()
            student_list.append(s)
        elif answ == "2":
            student_id = int(input("Enter the student ID: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark for the student"))
            add_mark(student, new_mark)
            print(student_list)
        elif answ == "3":
            print_student_list(student_list)
    return None


menu()
