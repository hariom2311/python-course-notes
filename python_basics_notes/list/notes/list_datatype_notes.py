"""
A list is a versatile data structure in Python that can store a collection of elements.
Lists are ordered, mutable (can be changed), and allow duplicate values.
Lists are created by enclosing elements in square brackets [ ] and separating them with commas.
"""

# Creating a List:
fruits = ['apple', 'banana', 'orange', 'mango']


# Accessing List Elements:
print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'orange'




# Modifying List Elements:
fruits[1] = 'grape'
print(fruits)  # Output: ['apple', 'grape', 'orange', 'mango']



# List Length:
length = len(fruits)
print(length)  # Output: 4




# Adding Elements to a List:
fruits.append('kiwi')
print(fruits)  # Output: ['apple', 'grape', 'orange', 'mango', 'kiwi']

fruits.insert(2, 'pear')
print(fruits)  # Output: ['apple', 'grape', 'pear', 'orange', 'mango', 'kiwi']




# Removing Elements from a List:
fruits.remove('orange')
print(fruits)  # Output: ['apple', 'grape', 'pear', 'mango', 'kiwi']

popped_fruit = fruits.pop()
print(popped_fruit)  # Output: 'kiwi'
print(fruits)  # Output: ['apple', 'grape', 'pear', 'mango']




# List Concatenation:
numbers = [1, 2, 3]
combined_list = fruits + numbers
print(combined_list)  # Output: ['apple', 'grape', 'pear', 'mango', 1, 2, 3]


# ===========================================================================

# Slicing a List:

# Basic Slicing: Retrieve a sublist from a list.
sliced_fruits = fruits[1:3]
print(sliced_fruits)  # Output: ['grape', 'pear']




# Negative Indexing: Retrieve elements from the end of the list using negative indices.
fruits = ['apple', 'banana', 'grape', 'pear', 'orange']
sliced_fruits = fruits[-3:-1]
print(sliced_fruits)  # Output: ['grape', 'pear']




# Step Size: Retrieve elements with a specified step size.
fruits = ['apple', 'banana', 'grape', 'pear', 'orange']
sliced_fruits = fruits[::2]
print(sliced_fruits)  # Output: ['apple', 'grape', 'orange']




# Slice Assignment: Modify elements in a sublist using slicing.
fruits = ['apple', 'banana', 'grape', 'pear', 'orange']
fruits[1:3] = ['kiwi', 'melon']
print(fruits)  # Output: ['apple', 'kiwi', 'melon', 'pear', 'orange']





# Slicing with Stride: Retrieve elements with a specified step size and direction.
fruits = ['apple', 'banana', 'grape', 'pear', 'orange']
sliced_fruits = fruits[4:0:-1]
print(sliced_fruits)  # Output: ['orange', 'pear', 'grape', 'banana']




# Omitted Indices: Retrieve elements from the beginning or end of the list.
fruits = ['apple', 'banana', 'grape', 'pear', 'orange']
sliced_fruits = fruits[:3]  # Equivalent to fruits[0:3]
print(sliced_fruits)  # Output: ['apple', 'banana', 'grape']

sliced_fruits = fruits[3:]  # Equivalent to fruits[3:len(fruits)]
print(sliced_fruits)  # Output: ['pear', 'orange']




# Reversed List: Retrieve the list in reverse order using slicing.
fruits = ['apple', 'banana', 'grape', 'pear', 'orange']
sliced_fruits = fruits[::-1]
print(sliced_fruits)  # Output: ['orange', 'pear', 'grape', 'banana', 'apple']

# list methods demonstration

# append(element): Adds an element to the end of the list.
fruits = ['apple', 'banana', 'orange']
fruits.append('mango')
print(fruits)  # Output: ['apple', 'banana', 'orange', 'mango']



# insert(index, element): Inserts an element at a specific position in the list.
fruits = ['apple', 'banana', 'mango']
fruits.insert(1, 'orange')
print(fruits)  # Output: ['apple', 'orange', 'banana', 'mango']



# remove(element): Removes the first occurrence of the specified element from the list.
fruits = ['apple', 'banana', 'orange', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange', 'banana']




# pop(index): Removes and returns the element at the specified index.
fruits = ['apple', 'banana', 'orange']
popped_fruit = fruits.pop(1)
print(popped_fruit)  # Output: 'banana'
print(fruits)  # Output: ['apple', 'orange']



# index(element): Returns the index of the first occurrence of the specified element in the list.
fruits = ['apple', 'banana', 'orange']
index = fruits.index('banana')
print(index)  # Output: 1



# count(element): Returns the number of occurrences of the specified element in the list.
fruits = ['apple', 'banana', 'orange', 'banana']
count = fruits.count('banana')
print(count)  # Output: 2



# sort(): Sorts the elements of the list in ascending order.
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 8, 9]



# reverse(): Reverses the order of the elements in the list.
fruits = ['apple', 'banana', 'orange']
fruits.reverse()
print(fruits)  # Output: ['orange', 'banana', 'apple']



# len(list): Returns the number of elements in the list.
fruits = ['apple', 'banana', 'orange']
length = len(fruits)
print(length)  # Output: 3
