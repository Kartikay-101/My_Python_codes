# Dictionaries = Dictionaries are used to store data in key-value pairs.
# Each key is linked to a value, making dictionaries ideal for structured data.

print("\t Dictionary\n\t-------------------")

student = {
    "name": "kartikay",
    "age": 23,
    "course": "python"
}
# or
# student = dict(
#     name="Kartikay",
#     age=23,
#     course="Python"
# )

print()
print(student)
print(student['name'])
print(student['age'])
print(student['course']) # What if the Key Doesn't Exist? it give output KeyError.

print(student.get('date of birth'))
print(student.get('date of birth', "This Key Is not Present"))  # You can also provide a default value:


# Dictionary is Mutable = You can change values.

student['name'] = "Shivam"
student['age'] = 17
student['course'] = "Java"

print(student)

# Add a New Key

student['city'] = 'greater noida'
print(student)

# Dictionary Methods

print("\t Dictionary Methods\n\t-------------------")

# 1. keys() = Returns all the keys of the dictionary.

print(student.keys())
print(list(student.keys()))  # Converted to a list.
print()

# 2. values() = Returns all the values.

print(student.values())
print()

# 3. items() = Returns both keys and values as tuples.

print(student.items())

for i in student.items():
    print(i)

for key, value in student.items():
    print(key, value)

# 4. get() = You've already seen it, but let's review.

print(student.get("name"))
print(student.get("city", 'not available'))


# 5. update() = Adds new multiple key-value pairs or updates existing ones.

student.update({
    "course": "Python",
    "marks": 95
})
print(student)

# 6. pop() = Removes a key and returns its value.

student.pop("age")
print(student)

# 7. popitem() = Removes the last inserted key-value pair and returns it as a tuple.

print(student)
print(student.popitem())
print(student)

# 8. clear() = Removes every key-value pair.


# student.clear()

# print(student)

# 9. copy() = Creates a shallow copy.

student2 = student.copy()

student2["name"] = "Rahul"

print(student)
print(student2)

# 10. setdefault() = It returns the value for a key if it exists. Otherwise, it creates the key with a default value.

print(student.setdefault("name", "Rahul"))
print(student.setdefault("religion", "Hindu"))
print(student)

# 11. fromkeys() = reates a new dictionary using a sequence of keys and one common value.

keys = ["Math", "Science", "English"]

marks = dict.fromkeys(keys, 0)

print(marks)

students = dict.fromkeys(["A", "B", "C"], "Absent")

print(students)

# Summary Table
# Method	Purpose
# keys()	Returns all keys
# values()	Returns all values
# items()	Returns key-value pairs as tuples
# get()	Gets a value safely
# update()	Adds or updates key-value pairs
# pop()	Removes a specific key
# popitem()	Removes the last inserted item
# clear()	Empties the dictionary
# copy()	Creates a shallow copy
# setdefault()	Returns value or creates key with default
# fromkeys()	Creates a new dictionary from a list of keys