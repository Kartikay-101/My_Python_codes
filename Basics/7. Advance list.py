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