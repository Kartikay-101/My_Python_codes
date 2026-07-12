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

for i in range(10):
    print(f"Employee {i+1}")
    emp_id = input('Enter Employee ID :- ').strip()
    name = input('Enter Employee Name :- ').strip().title()
    age = int(input("Enter Age : ").strip())
    mail = input('Enter Mail ID :- ').strip().casefold()
    phone_number = input('Enter Phone Number :- +91 ').strip()
    salary = float(input("Enter Salary : ").strip())

    valid = True

    if "@" not in mail or mail.count("@") != 1 or not mail.endswith(".com"):
        print("❌ Invalid Email.")
        valid = False

    if not(phone_number.isdigit() and len(phone_number) == 10 and phone_number[0] in '6789'):
        print("❌ Invalid Phone Number")
        valid = False

    if valid:
        employee = {
            "id": emp_id,
            "name": name,
            "age": age,
            "mail": mail,
            "phone": phone_number,
            "salary": salary
        }
        print("✅ Employee Registered Successfully.")
        print(employee)
    else:
        print("❌ Employee Registration Failed.")

