

# String Basics
"""
- Strings are sequences of characters enclosed in single (' ') or double (" ") quotes.
- They are immutable, meaning they cannot be changed once created.
- Strings can be accessed using indexing and slicing.
- Various methods are available for string manipulation.
"""

# Creating a string:
text = "Hello, World!"



# Accessing characters in a string:
print(text[0])  # Output: 'H'
print(text[7])  # Output: 'W'



# Modifying characters in a string:
# Strings are immutable, so we need to create a new string
new_text = text[:7] + 'Python!'
print(new_text)  # Output: 'Hello, Python!'




# String Length:
length = len(text)
print(length)  # Output: 13



# Concatenating strings:
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name + "!"
print(message)  # Output: 'Hello, Alice!'



# String Formatting:
age = 25
formatted_message = "My name is {} and I am {} years old.".format(name, age)
print(formatted_message)  # Output: 'My name is Alice and I am 25 years old.'



# String Methods:
# capitalize(): Converts the first character of a string to uppercase.
text = "hello, world!"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: 'Hello, world!'




# upper(): Converts all characters in a string to uppercase.
text = "hello, world!"
uppercased_text = text.upper()
print(uppercased_text)  # Output: 'HELLO, WORLD!'




# lower(): Converts all characters in a string to lowercase.
text = "Hello, World!"
lowercased_text = text.lower()
print(lowercased_text)  # Output: 'hello, world!'




# split(): Splits a string into a list of substrings based on a delimiter.
text = "apple, banana, orange"
fruits = text.split(", ")
print(fruits)  # Output: ['apple', 'banana', 'orange']




# join(): Concatenates elements of a list into a single string using a delimiter.
fruits = ['apple', 'banana', 'orange']
text = ", ".join(fruits)
print(text)  # Output: 'apple, banana, orange'




# replace(old, new): Replaces all occurrences of a substring with another substring.
text = "Hello, World!"
new_text = text.replace("World", "Python")
print(new_text)  # Output: 'Hello, Python!'




# find(substring): Returns the index of the first occurrence of a substring in a string.
text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7




# count(substring): Returns the number of occurrences of a substring in a string.
text = "Hello, World!"
count = text.count("o")
print(count)  # Output: 2




# strip(): Removes leading and trailing whitespace characters from a string.
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: 'Hello, World!'




# isdigit(): Checks if a string contains only digits.
text = "12345"
is_digit = text.isdigit()
print(is_digit)  # Output: True




# isalpha(): Checks if a string contains only alphabetic characters.
text = "Hello"
is_alpha = text.isalpha()
print(is_alpha)  # Output: True




# len(string): Returns the number of characters in a string.
text = "Hello, World!"
length = len(text)
print(length)  # Output: 13
