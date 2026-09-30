from student_data import students


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
