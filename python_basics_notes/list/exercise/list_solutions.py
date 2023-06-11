# Practice Questions with Solutions for List Datatype

# Question 1: Write a Python program to find the sum of all elements in a list.
# Solution 1:
numbers = [1, 2, 3, 4, 5]
sum_of_elements = sum(numbers)
print("Sum of elements:", sum_of_elements)

# Question 2: Write a Python program to find the largest element in a list.
# Solution 2:
numbers = [10, 5, 8, 12, 3]
largest_element = max(numbers)
print("Largest element:", largest_element)

# Question 3: Write a Python program to count the number of occurrences of an element in a list.
# Solution 3:
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
element = 'apple'
count = fruits.count(element)
print("Number of occurrences of", element, ":", count)

# Question 4: Write a Python program to remove all duplicates from a list.
# Solution 4:
numbers = [1, 2, 3, 2, 4, 3, 5, 1]
unique_numbers = list(set(numbers))
print("List without duplicates:", unique_numbers)

# Question 5: Write a Python program to check if a list is empty or not.
# Solution 5:
fruits = []
if not fruits:
    print("List is empty")
else:
    print("List is not empty")

# Question 6: Write a Python program to find the average of all elements in a list.
# Solution 6:
numbers = [10, 5, 8, 12, 3]
average = sum(numbers) / len(numbers)
print("Average of elements:", average)
