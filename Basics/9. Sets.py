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


# Set Operations

# Interview Notes
# | → Union
# & → Intersection
# - → Difference
# ^ → Symmetric Difference
# <= → Subset
# >= → Superset

print('\n\t Set Operations \n\t----------------')


# 1. Union = Meaning: Combine both sets. Duplicates appear only once

A = {1, 2, 3}
B = {3, 4, 5}
print(f'\nUnion of A and B is {A.union(B)}  or {A|B}\n')


# 2. Intersection = Meaning: Only the common elements.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"Intersection of A and B {A.intersection(B)} or {A & B}\n")

# 3. Difference = This is where beginners often get confused. as Elements in A but not in B.

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"Difference of A and B {A.difference(B)} or {A - B}\n")
print(f"Difference of B and A {B.difference(A)} or {B - A}\n")

# 4. Symmetric Difference : Take elements that are not common.

print(f"Symmetric Difference of A and B is {A.symmetric_difference(B)} or {(A ^ B)}\n")

# 5. Subset = A set is a subset if every element of it exists in another set.

A = {1, 2}
B = {1, 2, 3, 4}

print(A.issubset(B))
print(A <= B)
print()

# 6. Superset = Opposite of subset.

A = {1, 2, 3, 4}
B = {1, 2}

print(A.issuperset(B))
print(A >= B)
print()

# 7. Disjoint = Two sets are disjoint if they have no common elements.

A = {1, 2}
B = {3, 4}

print(A.isdisjoint(B))
print()

print('\n\t Another Example\n\t------------')

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference:", A - B)
print("Difference:", B - A)
print("Symmetric Difference:", A ^ B)

print({1, 2}.issubset(A))
print(A.issuperset({1, 2}))
print({10, 20}.isdisjoint(A))

