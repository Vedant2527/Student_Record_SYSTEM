from add_student import add_student
from search_student import search_student
from delete_student import delete_student
from update_student import update_student
from display_students import display_students


while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        delete_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        display_students()
    elif choice == "6":
        print("Exiting Student Record System...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
