# What is a List? = A list is a collection of multiple values stored in a single variable. List is Mutable

students = ['kartikay', 'rahul', 'prateek', 'chetan', 'dron', 'sambhav']
marks = [54, 34, 64, 34, 64, 43, 34]
subjects = [
    ['python', 'sql', 'r'],
    ['excel', 'sql', 'power bi'],
    ['statistics', 'r', 'python'],
    ['tableau', 'sql', 'excel'],
    ['python', 'machine learning', 'sql'],
    ['power bi', 'tableau', 'excel']
]

print()
print('Students Name :- ',students,'\n')
print('Marks :- ', marks,'\n')
print('Students Subjects :- ', subjects,'\n')

# Indexing in Lists
print('Indexing in Lists\n')
print(students[0])
print(marks[-3])
print(subjects[3])
print(marks[::-1])
print(students[::-1])
print(subjects[::-1])


# List are Mutable
print('\nMutable\n ---------------')
students[2] = 'shivam'
print(students)
subjects[1] = 'No subjects'
print(subjects)
marks[4] = None
print(marks)
print()

# List Slicing - list_name[start : stop : step]

print(students[1:-1])
print(subjects[0:-1:2])
marks[1:1]=[12,12] #Insert Values Using Slice Assignment
print(marks)
marks[1:8] = [] #Delete Elements Using Slice Assignment
print(marks)

# List Methods = A method is a function that belongs to an object.
print('\n List Method :- \n ------------------------')

print(students)
students.append('karan')  # It adds one element to the end of a list.
print(students)
students.append(['dhruv','krish'])
print(students)
marks.append(True)
print(marks)

print()
numbers = [10, 20, 30]
numbers.extend([40, 50, 60])    #It adds multiple elements from another iterable (such as a list) to the end of the existing list.

print(numbers)

letters = []
letters.extend("Python")
print(letters)

print()
students.insert(1,'varun') #insert() inserts one element at a specified index.
print(students)

print('\n',students)
students.remove('kartikay') # remove() removes the first occurrence of the specified value.
print(students,'\n')

print('\n',students)
students.pop(1) # It removes an element by its index. Pop only return delete value in list methods.
print(students,'\n')

print('\n',students)
# students.clear() # It clear() removes all elements from a list, but the list itself still exists.
# students[0:10] = []
print(students,'\n')

print(students.index('dron')) # It returns the index of the first occurrence of the specified value.

print(marks.count(54))

print()
fruits = ["Mango", "Apple", "Banana", "Orange"]

fruits.sort()

print(fruits)

fruits.sort(reverse = True)
print(fruits)

fruits.reverse() # It reverses the current order of the elements.
print(fruits)

print()
numbers = [10, 20, 30]

new_numbers = numbers.copy() # It creates a shallow copy of the list.

print(numbers)
print(new_numbers)