from student_data import students


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
