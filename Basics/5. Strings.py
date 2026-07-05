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
print(name.startswith('kartikay'))  # Checks whether a string starts with a given value.
print(name.endswith('nautiyal'))    # Checks whether a string ends with a given value.
print(name.split(','))  # It converts a string into a list.⭐
print(name.split('a'))

email = "kartikay@gmail.com"
print(email.split("@"))

languages = ["Python", "SQL", "Excel"]  # It joins list elements into a string.
print(" ".join(languages))
print(",".join(languages))
print("-".join(languages))

print(language.isalpha());  # Checks whether all characters are letters.
print(address.isalpha());

print(name.isdigit())   # Checks whether all characters are Numbers.

print(address.isalnum())   # Checks whether the string contains only letters and numbers.

print(language.isspace()) # Checks whether the string contains only spaces.

print(name.casefold())  # casefold() is similar to lower(), but it's more aggressive and is intended for case-insensitive comparisons.


            # Difference between lower and  casefold.
text = "Straße"
    #here ß is called Eszett (sharp S).
print(text.lower())
print(text.casefold())

print('\n')

# Before leaving Strings, try writing a small program without looking at notes.

name = input("Enter your Name :- ").title().strip()

gmail = input("Enter your Gmail :- ").casefold().strip()

print(f"Your mentioned Name is '{name}'")
print(f"Your mentioned Gmail is '{gmail}'")
print()
print(f'Name = {name.split()}')
print(f'Gmail = {gmail.split('@')}')
print()
print(f'Length of the Name = {len(name)}')
print(f'Length of the Name = {len(gmail)}')

print(email.endswith(".com"))

print(name[::-1])
print(gmail[::-1])