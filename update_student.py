from student_data import students


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
