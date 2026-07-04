# Operators = Operators are symbols used to perform operations on values and variables.
        # Types of Operators in Python

        # 1. Arithmetic Operators =      +, -, *, /, //, %, **
        # 2. Assignment Operators =     =, +=, -=, *=, /=, //=, %=, **=
        # 3. Comparison Operators =     ==, !=, >, <, >=, <=
        # 4. Logical Operators    =     and, or, not
        # 5. Identity Operators   =     is, is not
        # 6. Membership Operators =     in, not in
        # 7. Bitwise Operators    =     &, |, ^, ~, <<, >>

# Assignment operators are used to assign values to variables.
x = 10
x += 5
print(x)

# Logical Operators
    # Q) Check if a person is eligible to vote (18–100).
age = int(input("\n\tEnter you age : "))

if age >= 18 and age <= 100:
    print("\nPerson with this age " + str(age) + " is eligible\n")
else:
    print("\nPerson with this age " + str(age) + " is not eligible\n")

# Identity Operators = It check whether two variables refer to the same object in memory, not just whether their values are equal.
x = 10
y = 10

print(x is y)

# Membership operators = Its check whether a value exists inside a sequence.

fruits = ["Apple", "Mango", "Banana"]

print("Apple" in fruits)

fruits = ["Apple", "Mango", "Banana"]

print("Orange" not in fruits)