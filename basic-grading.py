import os

students = {"Bobby Jones": [90, 45, 50, 20, 80],
            "Jimmy Johnson": [30, 20, 10, 15, 20]}
grades = [90, 20]
selection = 0


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


# Starts App
def grades_welcome():
    clear_screen()
    print("1. Enter a new student")
    print("2. Add a student's grades")
    print("3. List all students")
    print("4. Get a student's grades")
    print("5. Get a student's average")
    print("Type 'exit' to Exit (Your data will NOT BE SAVED!)")
    print("***" * 20)
    selection = input(
        "Welcome to your grading app! What would you like to do? Enter the number for your selection: ")
    if selection == "1":
        add_student()
    elif selection == "2":
        add_grades()
    elif selection == "3":
        list_students()
    elif selection == "4":
        get_grades()
    elif selection == "5":
        get_average()
    elif selection.lower() == "exit":
        print("--" * 10)
        print("Thanks for using your grading app.  Have a great day!")
        print("--" * 10)
        exit()
    else:
        print("--" * 10)
        input("***Unrecognized command press enter to try again ***")
        print("--" * 10)
        grades_welcome()


def add_student():
    clear_screen()
    new_student = input(
        "Please enter the student's name (Ex: Bob Jones): ")
    students[new_student] = []
    print("-" * 10)
    print("{} added to the list! Current list of students: ".format(new_student))
    print("-" * 10)
    for key, value in students.items():
        print(key)
    print("-" * 10)
    student_option = input(
        "Type 'add' to add another student or 'home' to return to the main menu: ")
    if student_option.lower() == 'add':
        add_student()
    else:
        grades_welcome()


def add_grades():
    clear_screen()
    select_student = input(
        "Enter the student name you would like to add grades to (Ex: Bob Jones): ")
    grades_to_add = []
    add_more = "y"
    while add_more.lower() == "y":
        print("-" * 10)
        grades_to_add.append(
            input("Type a number to add a grade: "))
        print("-" * 10)
        add_more = input("Add another grade? Y/n: ")
    students[select_student] = students[select_student] + grades_to_add
    for key, value in students.items():
        if key == select_student:
            print("-" * 10)
            print(key, value)
    grades_option = input(
        "Enter '1' to add another student or anything else to return home: ")
    if grades_option == "1":
        add_grades()
    else:
        grades_welcome()


def list_students():
    print("-" * 10)
    for keys in students:
        print(keys)
    print("-" * 10)
    list_option = input("Type 'home' to go home: ")
    grades_welcome()


def get_grades():
    clear_screen()
    student_selection = input(
        "Which student would you like grades for? (Ex: Bobby Jones): ")
    if student_selection in students.keys():
        for key, value in students.items():
            if key == student_selection:
                print(value)
                print("-" * 10)
                get_option = input(
                    "Press '1' to get another student's grades or type 'home' to go home: ")
                if get_option == "1":
                    get_grades()
                else:
                    grades_welcome()
    else:
        print("We could not find that student please try again")
        print("-" * 10)
        get_grades()


def get_average():
    clear_screen()
    sum = 0
    student_selection = input(
        "Which student would you like the average for? (Ex: Bobby Jones): ")
    if student_selection in students.keys():
        for key, value in students.items():
            if key == student_selection:
                for value in students[key]:
                    sum += value
                average = sum/(len(students[key]))
                print("-" * 10)
                letter_grade = grading_scale(average)
                print("The grade average for {} is : ".format(
                    key), int(average), letter_grade)
                print("-" * 10)
                average_option = input(
                    "Press '1' to get another student's average or type 'home' to go home: ")
                if average_option == "1":
                    get_average()
                else:
                    grades_welcome()
    else:
        print("We could not find that student please try again")
        print("-" * 10)
        get_grades


def grading_scale(number):
    if number >= 90:
        return "A"
    elif number >= 80:
        return "B"
    elif number >= 70:
        return "C"
    elif number >= 60:
        return "D"
    else:
        return "F"


grades_welcome()
