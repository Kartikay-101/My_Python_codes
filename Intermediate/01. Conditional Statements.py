# What is a Conditional Statement? = A conditional statement allows a program to make decisions. Instead of executing every line of code, Python checks whether a condition is True or False and executes the appropriate block.

# ⭐ Notice the : after the condition and the indentation (typically 4 spaces). Indentation defines the block of code controlled by the if.

# 1. The if Statement = The if statement checks a condition. If the condition is true, the code inside the block runs.

    # Q1) Check if a number is positive.

print('\n\t Check if a number is positive.\n\t--------------------')
number = input("\nEnter a 'Number' :- ")

if int(number) > 0:
    print(f'\n---- {number} is positive number\n')
elif int(number) < 0:
    print(f'\n---- {number} is negative number\n')
else:
    print(f'\n---- {number} is Zero\n')

    # Q2) Check if a person is eligible to vote.

print ('\n\t Check if a person is eligible to vote.\n\t----------------------------------')
age = int(input("Enter your Age :- "))
    
if  age >=18:
    print(f'\nPerson having age "{age}" is eligible to vote\n')
else:
    print(f'\nPerson having age "{age}" is not eligible to vote\n')