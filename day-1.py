# This is a Python class for Day 1.

# Below is a multiline comment or docstring explaining the purpose of the code.
"""
This is a Python class
that focuses on learning variables.
"""

# Variables in Python
a = 1       # Assigns an integer value to variable 'a'
b = "Python"    # Assigns a string value to variable 'b'
c = 2.11    # Assigns a float value to variable 'c'

# To determine the type of a variable, we use the 'type()' method.
print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'str'>
print(type(c))  # Output: <class 'float'>

# Variables in Python are case-sensitive
a = 5     # Updates the value of variable 'a' to 5

A = "Python"   # Assigns a string value to variable 'A'
a = "Python"   # Updates the value of variable 'a' to "Python"
print(a)   # Output: Python
print(A)   # Output: Python

# Variable name formats
myname = "Sahil"      # Lowercase with no separators
my_name = "Sahil"     # Lowercase with underscores
_my_name = "Sahil"    # Lowercase with a single leading underscore
__my_name = "Sahil"   # Lowercase with two leading underscores
MYVARIABLE = "Sahil"  # Uppercase with no separators
MY_VARIABLE = "Sahil" # Uppercase with underscores

# The following variable name formats are incorrect:
2_name = "Sahil"     # Starts with a number
my-name = "Sahil"    # Contains a hyphen
my name = "Sahil"    # Contains a space

# Assigning multiple variables in a single line
a = 1
b = 2
c = 3
print(a, b, c)

# Using multiple variable assignment technique
a, b, c = 1, 2, 3
print(a, b, c)

# Assigning the same value to multiple variables
a = b = c = 5
print(a)
print(b)
print(c)

# Assigning list values to individual variables
lang_list = ['Python', 'C++', 'C', 'Go']
python = lang_list[0]
cpp = lang_list[1]
c = lang_list[2]
go = lang_list[3]
print(python)
print(cpp)
print(c)
print(go)

# Assigning list values to individual variables using a single line
python, cpp, c, go = lang_list
print(python)
print(cpp)
print(c)
print(go)

# Data types in Python
# 1. String
# 2. Numeric: int, float, complex
# 3. Sequence: list, tuple
# 4. Mapping: dict
# 5. Set
# 6. Boolean

# Explaining string data type with examples and methods
print("Hello Python \n'Language...'")
name = "sahil"
a = """Hey, I am Python Programming Lang
Use me for data science"""
first_name = "Sahil"
last_name = "Sharma"
print(first_name + last_name)

# Strings in Python are immutable, so you cannot replace individual characters
first_name = "Sahil"
first_name[0] = "n"  # This will result in an error since strings are immutable
print(first_name)

# Strings are iterable, so you can loop through each character
for char in "Python":
    print(char)

# The len() function returns the length of a string
name = "sahil sharma"
print(len(name))

# Check techniques in strings
name = """My name is sahil
my name is sonal
my name is pratik
"""
print("sahil" in name)    # Output: True
print("sonal" in name)    # Output: True
print("pratik" in name)   # Output: True
name = "my name is sahil"
print("sahil" not in name)   # Output: False

# Slicing in Python strings
name1 = "my name is sahil khanna"
name2 = "my name khanna"
print(name1[17:23])    # Output: khanna
print(name2[17:23])    # Output: ""

# Negative slicing in Python strings
print(name1[-6:])     # Output: khanna
print(name2[-6:])     # Output: khanna
print(name[-6:-8])    # Output: Empty string (since the start index is greater than the end index)

# Slicing forward with a step of 1
print(name[4:1:1])    # Output: Empty string (since the start index is greater than the end index)

# Slicing backward with a step of -1
print(name[4:1:-1])   # Output: emy

# Interview
print(name[:30])    # Output: my name is sahil

# Methods in Python strings or string modification using string methods
name = "my name is \"Sahil\" and branch is 'cs'"
print(name.upper())           # Output: MY NAME IS "SAHIL" AND BRANCH IS 'CS'
print(name.lower())           # Output: my name is "sahil" and branch is 'cs'
print(name.capitalize())      # Output: My name is "sahil" and branch is 'cs'
print(name.title())           # Output: My Name Is "Sahil" And Branch Is 'Cs'
print(name.split(':'))        # Output: ['my name is "Sahil" and branch is ', "'cs'"]
name = "  sahil  khanna    "
print(name.strip())           # Output: sahil  khanna
print(name.lstrip())          # Output: sahil  khanna
print(name.rstrip())          # Output:   sahil  khanna
print(name.count("m"))        # Output: 2
print(name.islower())         # Output: True
print(name.isupper())         # Output: False

# Concatenation in Python strings
first_name = "Sahil"
last_name = "Khanna"
full_name = first_name + " " + last_name
print(full_name)              # Output: Sahil Khanna

# String formation using format() method
b = 24232
role_no = "my role number is {}, and marks are {}, {}, {}"
print(role_no.format(b, 99, 98, 97))   # Output: my role number is 24232, and marks are 99, 98, 97


