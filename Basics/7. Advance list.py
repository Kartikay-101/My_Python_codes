# What is an Object? = Everything in Python is an object.
# What is Aliasing? = Aliasing means two or more variables refer to the same object.

    # Part 1: Aliasing vs Copying
print('\nAliasing vs Copying\n------------------')
numbers = [10, 20, 30]

new_numbers = numbers # Aliasing

print(numbers)
print(new_numbers)

numbers[1:1] = [15]
print(numbers)
print(new_numbers)

    # id() = It returns the memory identity of an object.
print(id(numbers))
print(id(new_numbers))

print(numbers is new_numbers)


numbers = [10, 20, 30]

new_numbers = numbers.copy() # Copy
numbers.extend([40,50,60])

print(numbers)
print(new_numbers)

print(id(numbers))
print(id(new_numbers))

    # is vs ==
a = [1, 2, 3]

b = a.copy()

print(a == b)   # Compares values.
print(a is b)   # Compares identity (memory location).
print()

    # Part 2: Shallow Copy vs Deep Copy
print('\nShallow Copy vs Deep Copy\n------------------')
    # One question remains: If copy() creates a new list, why do we need deepcopy()?

numbers = [10, 20, [30, 40]]

new_numbers = numbers.copy()    # What is a Shallow Copy? = A new outer list , But the inner objects are shared.
numbers[2].append(50)
print(numbers)
print(new_numbers)
print()
    # Deep Copy
import copy # Python provides the copy module.
numbers = [10, 20, [30, 40]]

new_numbers = copy.deepcopy(numbers)

numbers[2].append(50)

print(numbers)
print(new_numbers)

    # Part 3: List Operators
print('\nList Operators\n------------------')
# 1 Concatenation (+) = The + operator joins two or more lists.
list1 = [10, 20, 30]
list2 = [40, 50]

list3 = list1 + list2

print(list1)
print(list2)
print(list3)
print()
# 2 Repetition (*) = Repeats the elements of a list.

numbers = [1, 2]

print(numbers * 3)
print()

# 3 Membership Operator (in) = Checks whether a value exists in the list.

numbers = [10, 20, 30]

# numbers.remove(20)
print(numbers)
if 20 in numbers:
    print(f"20 is available in list 'numbers' {numbers}")
else:
    print(f"20 is not available in list 'numbers' {numbers}")

print(20 not in numbers) 
print()

# 5. Comparison Operators = Python compares lists element by element (lexicographical comparison).

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a != b)

a = [1, 2]
b = [1, 3]

print(a < b)
print(a > b)

# 6. Identity Operators = These compare objects, not values.

a = [1, 2]

b = a

print(a is b)
print('a - ',id(a),'b - ', id(b))

a = [1, 2]

b = a.copy()

print(a is b)

print('a - ',id(a),'b - ', id(b))
print()

# Part 4: Built-in Functions for Lists = These are functions, not list methods.

# 1. len() = Returns the total number of elements.

print("Len()")
numbers = [10, 20, 30, 40]

print(len(numbers))

# 2. min() = Returns the smallest element.

print("Min()")
numbers = [45, 12, 87, 5, 30]

print(min(numbers))

# 3. max() = Returns the largest element.

print("Max()")
numbers = [45, 12, 87, 5]

print(max(numbers))

# 4. sum() = Returns the total of all numeric elements.

print("Sum()")
numbers = [10, 20, 30]

print(sum(numbers))

# 5. sorted() = Unlike sort(): Returns a new sorted list


numbers = [30, 10, 20]

new_numbers = sorted(numbers)

print(numbers)
print(new_numbers)

print(sorted(numbers, reverse=True))

# 6. any() = Returns True if at least one element is truthy.

print("Any()")

numbers = [0, 0, 5, 0]

print(any(numbers))

# 7. all() = Returns True only if every element is truthy.

print("All()")
numbers = [1, 2, 3]

print(all(numbers))

# 8. enumerate() = Instead of manually keeping track of indexes.

# Without enumerate():
fruits = ["Apple", "Banana", "Mango"]

index = 0

for fruit in fruits:
    print(index, fruit)
    index += 1
print()

# With enumerate():
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# 9. zip() = Combines multiple iterables.

print("Zip()")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

result = zip(names, ages)

print(list(result))

for name, age in zip(names, ages):
    print(name, age)
print()

# Part 5: Iterating Through Lists = Iteration means visiting each element of a collection one by one.

# 1. Using a for Loop (Recommended
print("Learning List using loops\n-----------------")
numbers = [10, 20, 30, 40]

for index, values in enumerate(numbers):
    print(index,values, numbers)
print('\n')

# 2. Using range() and Indexes

for i in range(len(numbers)):
    print(i,numbers[i])

# 3. Using enumerate() (Best for Index + Value)
print()
for index, value in enumerate(numbers, start=10):
    print(index, value)

# 4. Using a while Loop = Sometimes required when the stopping condition is dynamic.
print()
print('while loop')
numbers = [10, 20, 30]

i = 0

while i < len(numbers) :
    print(numbers[i])
    i += 1

# 5. Modifying Elements During Iteration
print()
for num in numbers:
    num *= 10
    print(num)

# 6. Iterating in Reverse

print()
numbers = [10, 20, 30]

for number in reversed(numbers):
    print(number)

# 7. Nested Loops = Useful for nested lists (matrices).

print()
matrix = [
    [1, 2],
    [3, 4]
]

for row in matrix:
    for value in row:
        print(value)

# 8. Using zip() = Iterate over multiple lists simultaneously.
print()

names = ["Rahul", "Aman"]

marks = [85, 92]

for name, mark in zip(names, marks):
    print(name, mark)

# Part 6: Nested Lists = A nested list is a list that contains one or more lists as its elements.
print()
print('Nested Lists')
matrix = [
    [10, 20],
    [30, 40],
    [50, 60]
]

print(matrix[0])
print(matrix[2])
print(matrix[1][0])
print('nested loop')
for row in matrix:
    print(row)

for row in matrix:
    for value in row:
        print(value)


print('\n\nAnother Example\n----------------')

employees = [
    [101, "Rahul", 50000],
    [102, "Aman", 65000],
    [103, "Priya", 70000]
]

print('Emp ID |  Emp Name  |  Emp Salary')
for emp_id, emp_name, emp_salary in employees:
    print(f' {emp_id}  -   {emp_name}    -    {emp_salary}')

# Part 7: What is a List Comprehension? = A list comprehension is a concise way to create a new list from an iterable.

print()
print('List Comprehension\n------------------')
# Example 1: Create a list of squares of numbers from 1 to 5.
squares = []

for x in range(1,6):
    squares.append(x**2)

print(squares)

numbers = [i for i in range(5)]

print(numbers)

fruits = ["apple", "banana", "mango"]

upper_fruits = [ fruit.upper() for fruit in fruits]

print(upper_fruits)

print('\n Ever Numbers\n ----------------\n')

even = []

lists = [ i for i in range(100) if i % 2 == 0]

print(lists)


print('\n Odd Numbers\n ----------------\n')

even = []

lists = [ i for i in range(100) if i % 2 != 0]

print(lists)

