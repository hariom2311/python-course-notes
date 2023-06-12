

# Question 1: Write a Python program to count the number of characters in a string.
# Solution 1:
string = "Hello, World!"
count = len(string)
print("Number of characters:", count)




# Question 2: Write a Python program to reverse a string.
# Solution 2:
string = "Hello, World!"
reversed_string = string[::-1]
print("Reversed string:", reversed_string)




# Question 3: Write a Python program to check if a string is a palindrome.
# Solution 3:
string = "madam"
is_palindrome = string == string[::-1]
if is_palindrome:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")




# Question 4: Write a Python program to convert the first letter of each word in a string to uppercase.
# Solution 4:
string = "hello, world!"
title_case_string = string.title()
print("Title case string:", title_case_string)




# Question 5: Write a Python program to check if a string is an anagram of another string.
# Solution 5:
string1 = "listen"
string2 = "silent"
is_anagram = sorted(string1) == sorted(string2)
if is_anagram:
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
