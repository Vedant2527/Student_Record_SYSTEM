# Student Record Management System

**Student Name:** Vedant Verma  
**Registration Number:** 26BAI10984  
**Date:** 30 September 2026

## Overview

This project is a simple command-line Student Record Management System written in Python. It uses a nested dictionary to store student information and provides a menu-driven interface for performing basic operations.

The system allows users to add, search, update, delete, and display student records. All data is maintained in memory during program execution, so the project is lightweight and does not require external files or databases.

The project is intended for beginners who want to understand Python fundamentals such as functions, dictionaries, loops, and basic data handling.

## Features

- Add a new student record
- Search for a student using their registration number
- Update the details of an existing student
- Delete a student record
- Display all stored student records
- Menu-driven interface for user interaction
- Nested dictionary structure for storing student information
- Separate functions for individual operations

## Technologies and Tools Used

- Python 3.8 or above
- No external libraries required
- Windows, macOS, and Linux
- Compatible with text editors and IDEs such as VS Code, IDLE, and PyCharm

## How to Install and Run the Project

### Step 1: Install Python

Make sure Python 3.8 or above is installed on your computer. Check the installed version by running:

```bash
python --version
```

On some systems, you may need to use:

```bash
python3 --version
```

### Step 2: Open the Project Folder

Open the folder containing the Python source file in a terminal or in an IDE such as VS Code.

### Step 3: Run the Program

Run the following command:

```bash
python student_record_system.py
```

If your system uses `python3`, run:

```bash
python3 student_record_system.py
```

Once the program starts, a menu appears with options for managing student records. Enter the number for the operation you want to perform and follow the prompts.

## Instructions for Testing the System

### 1. Test Adding Students

1. Start the program and choose **1. Add Student**.
2. Enter a registration number and the student's details.
3. Add another student using a different registration number.
4. Try adding a student with a registration number that already exists.

**Expected result:** The program should add new records and show a message if a registration number is already in use.

### 2. Test Searching for Students

1. Choose **2. Search Student**.
2. Enter the registration number of an existing student.
3. Search again using a registration number that has not been added.

**Expected result:** The program should display the matching student's details or show a not-found message.

### 3. Test Updating Records

1. Choose **4. Update Student**.
2. Enter the registration number of an existing student.
3. Change one or more fields.
4. Press Enter without typing anything for a field to keep its current value.
5. Try updating a registration number that does not exist.

**Expected result:** The program should update the entered fields, retain unchanged values, and show a message if the student is not found.

### 4. Test Deleting Records

1. Choose **3. Delete Student**.
2. Enter the registration number of an existing student.
3. Try deleting the same registration number again.

**Expected result:** The first attempt should delete the record. The second should show a not-found message.

### 5. Test Displaying All Students

1. Add two or more student records.
2. Choose **5. Display All Students**.
3. Check that the records appear and that any updates or deletions are reflected.
4. Try this option when no records are stored.

**Expected result:** The program should display all available records or indicate that no records are available.

### 6. Test Exiting the Program

Choose **6. Exit**.

**Expected result:** The program should close cleanly.

## Data Storage

Student records are stored in a Python dictionary while the program is running. The information is not saved permanently, so all records are cleared when the program is closed.

## Summary

This project demonstrates the use of Python dictionaries, functions, loops, conditional statements, and user input in a simple menu-driven application. It can be run from the command line and does not require any additional dependencies.
