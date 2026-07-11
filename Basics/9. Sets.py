# Sets are used to store multiple values in a single variable.
# A set does not allow duplicate values and does not maintain any specific order.

# A set is an unordered collection of unique elements.

# Unlike lists and tuples:

# ❌ No duplicate values
# ❌ No indexing
# ❌ No slicing
# ✅ Very fast searching
# ✅ Mathematical operations (union, intersection, difference)


fruits = {"apple", "banana", "cherry", "mango", "banana", "cherry"}  # it remove duplicate values stored in Sets.

print(type(fruits))
print(fruits)


for fruit in fruits:
    print(fruit)

# Set Methods
print('\n\t Set Method\n\t-------------------')

# 1. add() = Adds one element to the set.

fruits.add('carrot')
print(fruits)
print()

# 2. update() = Adds multiple elements.

numbers = {1, 2, 3}

numbers.update([4, 5, 6])

print(numbers)

a = {1, 2}

b = {3, 4}

a.update(b)

print(a)
print()

# 3. remove() = Removes a specific element.

fruits.remove("banana") # - If the value doesn't exist Output will be KeyError

print(fruits)


# 4. discard() = Also removes an element.

fruits.discard("applee") # - If the value doesn't exist Output will be no Error.

# 5. pop() = Removes and returns one arbitrary element.

numbers = {10, 20, 30}

value = numbers.pop()

print(value)
print(numbers)

# 6. clear() = Removes every element.

numbers = {1, 2, 3, 4}

numbers.clear()

print(numbers)


# 7. copy() = Creates a shallow copy of the set.

a = {1, 2, 3}

b = a.copy()

print(a)
print(b)