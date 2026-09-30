# Student Record System

**Student Name:** Vedant Verma  
**Registration Number:** 26BAI10984  
**Date:** 30 September 2026

## Overview
A simple command-line Student Record Management System made with basic Python.
The project is split into separate modules to keep each operation organized.

## Modules
- `main.py` - Displays the menu and calls the selected function.
- `student_data.py` - Stores student records in a dictionary.
- `add_student.py` - Adds a student record.
- `search_student.py` - Searches for a student by registration number.
- `delete_student.py` - Deletes a student record.
- `update_student.py` - Updates existing student details.
- `display_students.py` - Displays all stored student records.

## Requirements
- Python 3.8 or above
- No external libraries required

## How to Run
1. Extract the ZIP file.
2. Open the extracted folder in VS Code or a terminal.
3. Run the following command from that folder:

   ```bash
   python main.py
   ```

   If needed, use `python3 main.py` instead.
4. Select an option from the menu and follow the prompts.

## Testing
Try each menu option:
1. Add a student, then try adding the same registration number again.
2. Search for an existing and a non-existing registration number.
3. Delete a student and then try deleting the same record again.
4. Update one field and press Enter for the fields you want to keep unchanged.
5. Display all students, including when the dictionary is empty.
6. Choose Exit to close the program.

## Note
Student records are stored in memory and are cleared when the program is closed.
