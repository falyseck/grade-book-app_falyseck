from gradebook import *


def display_menu():
    with open("ascii.txt", "r") as ascii:
        print(ascii.read())
    menu = """
    1. Add Student
    2. Add Course
    3. Register Student for Course
    4. Calculate Ranking
    5. Search by Grade
    6. Generate Transcript
    7. Exit
    """
    print(menu)

def main():
    while True:

        display_menu()
        choice = int(input("Choose an option: "))
        if choice == 1:
            student = GradeBook()
            student.add_student()
        elif choice == 2:
            GradeBook().add_course()
        elif choice == 3:
            GradeBook().register_student_for_course()
        elif choice == 4:
            GradeBook().calculate_GPA()
        elif choice == 5:
            GradeBook().search_by_grade()
        elif choice == 6:
            GradeBook().generate_transcript()
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please try again.")

main()
