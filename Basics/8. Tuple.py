# what is Tuple? = Tuples are used to store multiple values in a single variable, similar to lists.
# The key difference is that tuples are ⭐immutable, which means their values cannot be changed after creation.

print("\n\tLearning Tuple\n\t-----------------")
items = ("apple", "banana", "orange")
print(items)

# Converting Between List and Tuple
list1 = list(items)
print(f'\nTuple now converted into a List: {list1}')

list2 = tuple(list1)
print(f'List now converted into a Tuple: {list2}\n')

# Single Element Tuple

num = (10,)

print(num)

# Q1. Why is (10) not a tuple?

# Because parentheses alone are used for grouping expressions. A single value inside parentheses remains its original type (int in this case).


# Accessing Tuple Elements (Indexing)
print("\n\tAccessing Tuple Elements (Indexing)\n\t-----------------------------------")
fruits = ("apple", "banana", "orange", "grape", "kiwi")

print(fruits)  # Printing the entire tuple

print(f'\nAccessing Tuple Elements (Indexing):\n{fruits[0]}')  # Accessing the first element
print(fruits[2])  # Accessing the third element
print(fruits[-1])  # Accessing the last element
print(fruits[-3])  # Accessing the third-to-last element

tuple1 = [(index, fruit) for index, fruit in enumerate(fruits)]

print(tuple1)  # Printing index and corresponding fruit

for rows in range(len(fruits)):
    print(tuple1[rows])

# Tuple Slicing
print("\n\tTuple Slicing\n\t-----------------")

print(fruits)  # Printing the entire tuple
print(fruits[1:4])  # Printing elements from index 1 to 3
print(fruits[:3])  # First three elements
print(fruits[-2:])  # last two elements
print(fruits[2:5])  # Printing elements from index 2 to 4


# Tuple Packing and Unpacking

# What is Tuple Packing? = Packing means putting multiple values into a single tuple.

print("\n\tTuple Packing\n\t-----------------")

student = "Kartikay", 23, "Python"

print(student)
print(type(student))

# what is Tuple Unpacking?  = Unpacking means extracting the values from a tuple into individual variables.
print("\n\tTuple Unpacking\n\t-----------------")

name, age, course = student

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Course: {course}")

# Using * (Star Unpacking) = The * operator collects multiple values into a list.

numbers = (10, 20, 30, 40, 50)

a, *age = numbers

print(a)
print(age)