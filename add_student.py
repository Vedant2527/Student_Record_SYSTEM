from student_data import students


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
