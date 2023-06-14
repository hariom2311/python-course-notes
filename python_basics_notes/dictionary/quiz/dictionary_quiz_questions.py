# Quiz Questions - Dictionary Data Type

# Q1. Which symbol is used to access a value in a dictionary?

"""
Options:
a) .
b) :
c) [
d) (
"""

# Q2. How do you check if a key exists in a dictionary?

"""
Options:
a) using the in keyword
b) using the exists() method
c) using the find() method
d) using the has_key() method
"""

# Q3. What happens when you try to add a new key-value pair to a dictionary using an existing key?

"""
Options:
a) The new value overwrites the existing value
b) The new value is appended to the existing value
c) An error is raised
d) The existing value is deleted and replaced with the new value
"""

# Q4. How do you remove a key-value pair from a dictionary?

"""
Options:
a) using the remove() method
b) using the delete() method
c) using the discard() method
d) using the del keyword
"""

# Q5. What will be the output of the following code?
my_dict = {"apple": 2, "banana": 3, "cherry": 1}
del my_dict["banana"]
print(my_dict)
"""
Options:
a) {"apple": 2, "banana": 3, "cherry": 1}
b) {"apple": 2, "cherry": 1}
c) {"banana": 3, "cherry": 1}
d) Error
"""

# Q6. How do you retrieve all keys from a dictionary?

"""
Options:
a) using the keys() method
b) using the values() method
c) using the items() method
d) using the get() method
"""

# Q7. What is the difference between the get() method and the [] operator when accessing values in a dictionary?

"""
Options:
a) The get() method returns None if the key doesn't exist, while the [] operator raises an error
b) The get() method returns the value if the key exists, while the [] operator raises an error
c) The get() method allows you to specify a default value if the key doesn't exist, while the [] operator returns None
d) The get() method and the [] operator are equivalent and can be used interchangeably
"""

# Q8. How do you merge two dictionaries into one?

"""
Options:
a) using the combine() method
b) using the append() method
c) using the merge() method
d) using the update() method
"""

# Q9. What is the time complexity of accessing a value in a dictionary by its key?

"""
Options:
a) O(1)
b) O(log n)
c) O(n)
d) O(n^2)
"""

# Q10. What will be the output of the following code?
my_dict = {"apple": 2, "banana": 3, "cherry": 1}
sorted_dict = dict(sorted(my_dict.items()))
print(sorted_dict)
"""
Options:
a) {"apple": 2, "banana": 3, "cherry": 1}
b) {"cherry": 1, "banana": 3, "apple": 2}
c) {"apple": 2, "cherry": 1, "banana": 3}
d) Error
"""
