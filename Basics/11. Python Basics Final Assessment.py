"""
==========================================================
            TechNova Solutions Pvt. Ltd.
        Employee & Project Management System
==========================================================

BACKGROUND

You recently joined TechNova Solutions as a Python Developer.

The HR department has been maintaining employee records in Excel.
Management now wants you to build the first version of their
Employee & Project Management System.

Your job is NOT to build everything at once.

The manager will keep giving you new requirements.

Complete every task in order.

Rules

✔ Don't skip tasks.
✔ Think first.
✔ Use the concepts you've already learned.

DO NOT USE
------------
Functions
Files
Exception Handling
OOP
Modules (except copy if required)

Only use the topics you've already learned.

"""


# Phase 1 - Employee Registration (Tasks 1-4)

# Task 1
# Register 10 employees using user input.
# Clean the input, convert datatypes, validate email and phone number.

employee = []

for i in range(10):
    print(f"Employee {i}")
    emp_id = input('Enter Employee ID :- ').strip()
    name = input('Enter Employee Name :- ').strip().title()
    age = input('Enter age :- +91 ').strip()
    mail = input('Enter Mail ID :- ').strip().casefold()
    phone_number = input('Enter Phone Number :- ').strip()

emp_id = int(emp_id)
age = int(age)
phone_number = int(phone_number)

if '@' in mail and mail.endswith('.com'):
    print('Valid Mail')
else:
    print("Invalid mail")

if phone_number.isdigit() and len(phone_number) == 10 and phone_number[0] in '6789':
    print("Valid Phone Number")
else:
    print("Invalid Phone Number")
