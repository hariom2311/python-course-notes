# Dictionary

"""
Definition: A dictionary is an unordered collection of key-value pairs, where each key is unique and
used to access its corresponding value.
Creation: Dictionaries can be created using curly braces {} or the dict() constructor.
"""


# Creating a dictionary
student = {"name": "John", "age": 20, "grade": "A"}




# Accessing values using keys
print(student["name"])  # Output: John




# Updating a value
student["age"] = 21




# Removing a key-value pair
del student["grade"]




# Accessing all keys
keys = student.keys()
print(keys)  # Output: dict_keys(['name', 'age'])




# Accessing all values
values = student.values()
print(values)  # Output: dict_values(['John', 21])




# Accessing all key-value pairs
items = student.items()
print(items)  # Output: dict_items([('name', 'John'), ('age', 21)])




# Getting a value with default
grade = student.get("grade", "Unknown")
print(grade)  # Output: Unknown




# Updating with another dictionary
student.update({"grade": "A", "city": "New York"})
print(student)  # Output: {'name': 'John', 'age': 21, 'grade': 'A', 'city': 'New York'}




# Removing and returning a value
name = student.pop("name")
print(name)  # Output: John




# Getting the number of key-value pairs
size = len(student)
print(size)  # Output: 3
