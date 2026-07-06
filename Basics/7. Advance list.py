# What is an Object? = Everything in Python is an object.
# What is Aliasing? = Aliasing means two or more variables refer to the same object.

    # Part 1: Aliasing vs Copying
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
    # Shallow Copy vs Deep Copy
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