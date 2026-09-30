from student_data import students


def delete_student():
    print("\n--- Delete Student ---")
    reg_no = input("Enter registration number: ").strip()

    if reg_no in students:
        del students[reg_no]
        print("Student record deleted successfully.")
    else:
        print("Student record not found.")
