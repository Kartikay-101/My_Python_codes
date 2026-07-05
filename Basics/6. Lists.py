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
marks[4] = 'Null'
print(marks)
print()