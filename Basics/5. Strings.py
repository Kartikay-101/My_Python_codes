# What is a String? = A string is a sequence of characters enclosed in quotes.
# A character can be: Letters, Numbers, Symbols, Spaces.

# Strings are Immutable || Immutable means: Once a string is created, its characters cannot be changed.

name = 'kartikay nautiyal'

address = """\n
House No. 10
Greater Noida
Uttar Pradesh\n"""

print("\n--- Strings ---")
print(name[0])      # String Indexing = Every character in a string has a position number.
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

print(address)
print(type(address))
print(f"Length of '{name}' = {len(name)}")  # String Length len()
print(f"Length of 'address' = {len(address)}")  # String Length len()

print('\n')

# What is String Slicing? = Slicing means extracting a portion (part) of a string.

print(name[0:3])
print(name[1:-1])
print(name[:-5])    # First 5 characters
print(name[5:])     # Last 5 characters
print(name[0:8:2])  # string[start:end:step] tells Python how many positions to move each time.

language = "Python"     # reverse a string
print(language[::-1])   # Reverse
print(language[::-2])   # Reverse every second character

# What are String Methods? = A method is a built-in function that belongs to an object.

print('\nString Methods :- \n')
print(name.upper())     # Converts all letters to uppercase.
print(name.lower())     # Converts every letter into lowercase.
print(name.capitalize())# Only the first letter becomes uppercase.
print(name.title())     # Capitalizes the first letter of every word.
print(address.swapcase())# Uppercase becomes lowercase. & Lowercase becomes uppercase.

text = "    Python    "
print(text)
print(text.strip())     # Removes spaces (or specified characters) from both the beginning and the end of a string.
print(len(text.strip()))
print(len(text))
print(text.lstrip())    # Removes spaces only from the left.
print(text.rstrip())    # Removes spaces only from the right.

print(text.replace("Pyt","R"))  # Replaces one value with another.

print(name.find('n'))   # Finds the index of the first occurrence.
print(name.count('a'))  # Counts how many times something appears.




