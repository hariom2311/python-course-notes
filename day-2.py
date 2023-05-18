# LIST DATA TYPE IN PYTHON
name_list = ['Hariom', 'Sahil', 'Subham', 'Rohan']

# List in Python is iterable. You can loop over its elements using a for loop.
# Uncomment the code below to iterate over the elements of the list and check if a name is found.
for name in name_list:
    if name == "Hariom":
        print("Found")

# Uncomment the code below to check if "Sahil" is in the name_list using 'in' operator.
if "Sahil" in name_list:
    print("Found")

student_data = ["Sahil", 23232, 98, 97.2, True, (1, 2, 3), {"name": "sahil"}, {'a', 'b', 'a'}, [2, 3, 4]]
print(student_data)
# The student_data list contains different types of elements such as strings, integers, floats, booleans,
# tuples, dictionaries, sets, and even another list.

# Uncomment the code below to print the student_data list.

# List slicing allows you to extract a portion of the list.
# Uncomment the code below to print a slice of the integer_var list.
integer_var = [1, 2, 5, 9, 4, 6, 8, 11]
print(integer_var[2:7])  # Prints [5, 9, 4, 6, 8]

# List slicing also works with negative indices.
# Uncomment the code below to print a slice of the integer_var list using negative indices.
print(integer_var[-7:-2])  # Prints [2, 5, 9, 4, 6]

# Uncomment the code below to print a slice of the integer_var list using step size.
print(integer_var[0::2])  # Prints [1, 5, 4, 8]

# The assignment statement assigns the reference of the original list to the name_list_copy.
# Both name_list and name_list_copy point to the same list in memory.
# Uncomment the code below to print the original list and the copied list.
name_list = ["Sahil", "Hariom", [1, 2, 3]]
name_list_copy = name_list
print(name_list)  # Prints ['Sahil', 'Hariom', [1, 2, 3]]
print(name_list_copy)  # Prints ['Sahil', 'Hariom', [1, 2, 3]]

# Uncomment the code below to modify the first element of the copied list.
name_list_copy[0] = "Subham"
# The modification affects both the original list and the copied list because they refer to the same list object.
print(name_list)  # Prints ['Subham', 'Hariom', [1, 2, 3]]
print(name_list_copy)  # Prints ['Subham', 'Hariom', [1, 2, 3]]

import copy

# List Data Type in Python
name_list = ['Hariom', 'Sahil', 'Subham', 'Rohan']

# ...

# Uncomment the code below to create a shallow copy of the list using copy.copy().
name_list_copy = copy.copy(name_list)

# A shallow copy creates a new list object, but the elements inside the list are references to the original objects.
# Modifying the elements of the copied list can affect the original list if the objects are mutable.

# Uncomment the code below to demonstrate the behavior of a shallow copy.
name_list_copy[0] = "Subham"

# The modification only affects the copied list, not the original list.
print(name_list)  # Prints ['Hariom', 'Sahil', 'Subham', 'Rohan']
print(name_list_copy)  # Prints ['Subham', 'Sahil', 'Subham', 'Rohan']

# Uncomment the code below to demonstrate the behavior of a shallow copy with a nested list.
name_list_copy[2][0] = 10

# The modification affects both the original list and the copied list because they share the same nested list object.
print(name_list)  # Prints ['Hariom', 'Sahil', [10, 2, 3], 'Rohan']
print(name_list_copy)  # Prints ['Subham', 'Sahil', [10, 2, 3], 'Rohan']

# Uncomment the necessary code to see the explanations and results for each code snippet.

# Uncomment the code below to create a deep copy of the list using copy.deepcopy().
name_list_copy = copy.deepcopy(name_list)
# A deep copy creates a new list object with its own separate copy of nested objects.
# Modifying the copied list will not affect the original list.

name_list_copy[2][0] = 10
print(name_list)  # Prints ['Sahil', 'Hariom', [1, 2, 3]]
print(name_list_copy) # Prints ['Sahil', 'Hariom', [10, 2, 3]]

# Uncomment the code below to print the memory addresses of the first element of both lists.
print(id(name_list[0]))
print(id(name_list_copy[0]))



# OPERATORS IN PYTHON
# Arithmetic operators perform mathematical operations on operands.
# Uncomment the code below to see examples of arithmetic operators.
# +, -, *, //, /, %, **
# Uncomment the specific operation and print the result.
a = 5
b = 2
print(a + b) # Addition: 7
print(a - b) # Subtraction: 3
print(a * b) # Multiplication: 10
print(a // b) # Floor Division: 2
print(a / b) # Division: 2.5
print(a % b) # Modulo: 1
print(a ** b) # Exponentiation: 25


# Assignment operators are used to assign values to variables.
# Uncomment the code below to see examples of assignment operators.
# =, +=, -=, *=, //=, /=, %=
# Uncomment the specific operation and print the result.

a = 5
a += 2 # Equivalent to: a = a + 2
print(a) # Prints 7


# Comparison operators compare the values of two operands.
# Uncomment the code below to see examples of comparison operators.
# <=, >=, ==, !=, >, <
# Uncomment the specific operation and print the result.
a = 5
b = 2
print(a <= b) # Less than or equal to: False
print(a >= b) # Greater than or equal to: True
print(a == b) # Equal to: False
print(a != b) # Not equal to: True
print(a > b) # Greater than: True
print(a < b) # Less than: False


# Logical operators perform logical operations on operands.
# Uncomment the code below to see examples of logical operators.
# and, not, or
# Uncomment the specific operation and print the result.
a = True
b = False
print(a and b) # Logical AND: False
print(not a) # Logical NOT: False
print(a or b) # Logical OR: True


# The 'in' operator checks if a value exists in a sequence.
# Uncomment the code below to see an example of the 'in' operator.
name = "Sahil"
print("h" in name) # True

# The 'is' operator checks if two objects have the same identity.
# Uncomment the code below to see an example of the 'is' operator.
a = [1, 2, 3]
b = a
print(a is b) # True

# The '==' operator checks if two objects have the same value.
# Uncomment the code below to see an example of the '==' operator.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True