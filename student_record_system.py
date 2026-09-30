# Student Record System

students = {}


def add_student():
    print("\n--- Add Student ---")
    reg_no = input("Enter registration number: ").strip()

    if reg_no in students:
        print("A student with this registration number already exists.")
        return

    name = input("Enter name: ").strip()
    course = input("Enter course: ").strip()
    cgpa = input("Enter CGPA: ").strip()
    state = input("Enter state: ").strip()

    students[reg_no] = {
        "Name": name,
        "Course": course,
        "CGPA": cgpa,
        "State": state
    }
    print("Student record added successfully.")


def search_student():
    print("\n--- Search Student ---")
    reg_no = input("Enter registration number: ").strip()

    if reg_no not in students:
        print("Student record not found.")
        return

    student = students[reg_no]
    print("\nRecord Found")
    print("Registration Number:", reg_no)
    print("Name:", student["Name"])
    print("Course:", student["Course"])
    print("CGPA:", student["CGPA"])
    print("State:", student["State"])


def delete_student():
    print("\n--- Delete Student ---")
    reg_no = input("Enter registration number: ").strip()

    if reg_no in students:
        del students[reg_no]
        print("Student record deleted successfully.")
    else:
        print("Student record not found.")


def update_student():
    print("\n--- Update Student ---")
    reg_no = input("Enter registration number: ").strip()

    if reg_no not in students:
        print("Student record not found.")
        return

    student = students[reg_no]
    print("Press Enter to keep the current value.")

    name = input("Name (" + student["Name"] + "): ").strip()
    course = input("Course (" + student["Course"] + "): ").strip()
    cgpa = input("CGPA (" + student["CGPA"] + "): ").strip()
    state = input("State (" + student["State"] + "): ").strip()

    if name:
        student["Name"] = name
    if course:
        student["Course"] = course
    if cgpa:
        student["CGPA"] = cgpa
    if state:
        student["State"] = state

    print("Student record updated successfully.")


def display_students():
    print("\n--- All Students ---")

    if not students:
        print("No student records are available.")
        return

    for reg_no, student in students.items():
        print("\nRegistration Number:", reg_no)
        print("Name:", student["Name"])
        print("Course:", student["Course"])
        print("CGPA:", student["CGPA"])
        print("State:", student["State"])


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
