# What is Input()? = Input() allows the program to receive data from the user while it is running.
# NOTE: Everything received by input() is a string.

# -----------------------------------------------------------------------------------------------------
print('\n Welcome to Input() Function Module')

name = input("\n\t What is your Name? ")
print(f"\n\t Hello!! {name}, Kindly specify your age.") # Using f-string to print the name of the user.

age = int(input("\n Age = "))
print("\n\t Your age is " + str(age) + " years old.")         # Using string concatenation with +

salary = float(input("\n Enter salary: "))
print("\n\t Your Salary is %s" % salary)         # Using string formatting with %")

gmail = input("\n Enter your Gmail: ")
print("\n\t Your Gmail is {}".format(gmail))    # Using string formatting with .format() method

# ------------------------------------------------------------------------------------------------------

print('\nSum of Two Numbers using Input() Function')

First_Number = int(input("\n\t Enter First Number: "))
Second_Number = int(input("\t Enter Second Number: "))

Sum = First_Number + Second_Number

print("\n Addition of 2 numbers = %a\n\n"%Sum)