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

# 2. Nested if Statements = A nested if means writing an if statement inside another if statement.

# Example (ATM)

user_name = input('\n\t ⭐ Enter User Name here :- ').strip().title()
print()
print("="*50)
print('\t Most Welcome to MKB ATM')
print("="*50)

print(f"\n\t  Hello {user_name}!!, Nice to see you again.\n")

pin_code = 1234

pin = int(input('Enter Pin = '))

balance = 100000

if pin == pin_code:
    print("\n ✅ Verified Customer")
    print("\n\t Do you want to withdraw money from your account? \n\t-----------------")
    withdraw = float(input("Enter Withdrawl Amount in 'Rs' - "))
    if withdraw <= balance:
        print(f'\n Your account has been debited by {withdraw} amount')
        print(f"\nNow Your bank balance is {balance - withdraw}")
        if (balance - withdraw) % 2 == 0:
            print(f"\nYour bank balance is even number {balance - withdraw}")
        else:
            print(f"\nYour bank balance is odd number {balance - withdraw}")
    else:
        print('You Have not sufficient balance to withdraw from you account')
else:
    print("\n ❌ Unknown Customer")