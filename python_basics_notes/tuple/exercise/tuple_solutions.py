# Question 1: Write a Python program to create a tuple with elements "apple", "banana", and "cherry". Access the second element of the tuple.

my_tuple = ("apple", "banana", "cherry")
second_element = my_tuple[1]
print("Second element:", second_element)

# Question 2: Write a Python program to concatenate two tuples (tuple1 and tuple2) and create a new tuple.

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print("Concatenated tuple:", concatenated_tuple)

# Question 3: Write a Python program to count the number of occurrences of a value in a tuple.

my_tuple = (1, 2, 3, 2, 4, 2, 5)
value = 2
count = my_tuple.count(value)
print("Number of occurrences of", value, "in the tuple:", count)

# Question 4: Write a Python program to convert a tuple into a list.

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print("Converted list:", my_list)

# Question 5: Write a Python program to check if a given element exists in a tuple.

my_tuple = (1, 2, 3, 4, 5)
element = 3
if element in my_tuple:
    print(element, "exists in the tuple")
else:
    print(element, "does not exist in the tuple")
