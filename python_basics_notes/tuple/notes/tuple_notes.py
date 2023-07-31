# TUPLES IN PYTHON
# A tuple is an ordered collection of elements, enclosed in parentheses ().
# Tuples are immutable, meaning their values cannot be changed once defined.
# You can access tuple elements using indexing or slicing.

# Create a tuple
my_tuple = (1, 2, 3, 'a', 'b', 'c')

# Access tuple elements using indexing
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'a'

# Access tuple elements using negative indexing
print(my_tuple[-1])  # Output: 'c'
print(my_tuple[-3])  # Output: 3

# Slicing a tuple
print(my_tuple[1:4])  # Output: (2, 3, 'a')
print(my_tuple[:3])   # Output: (1, 2, 3)
print(my_tuple[3:])   # Output: ('a', 'b', 'c')

# Tuple concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

# Tuple repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Tuple length
print(len(my_tuple))  # Output: 6

# Tuple iteration using a for loop
for item in my_tuple:
    print(item)

# Unpacking tuples
tuple3 = ('John', 25, 'USA')
name, age, country = tuple3
print(name)     # Output: 'John'
print(age)      # Output: 25
print(country)  # Output: 'USA'

# Tuple methods
# Tuple doesn't have many built-in methods as they are immutable, but there are a few useful ones:
# count(): Returns the number of occurrences of a value in a tuple.
# index(): Returns the index of the first occurrence of a value in a tuple.

# Example:
numbers = (1, 2, 2, 3, 4, 2)
print(numbers.count(2))    # Output: 3
print(numbers.index(3))    # Output: 3

