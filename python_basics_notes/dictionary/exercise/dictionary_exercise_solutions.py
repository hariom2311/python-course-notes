# Question 1: Write a Python program to count the frequency of elements in a given list and store the results in a dictionary.

# Solution 1
def count_frequency(lst):
    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    return frequency

# Example usage:
my_list = [1, 2, 1, 3, 2, 4, 1]
result = count_frequency(my_list)
print(result)


# Question 2: Write a Python program to merge two dictionaries into a single dictionary.

# Solution 2
def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result = merge_dictionaries(dict1, dict2)
print(result)


# Question 3: Write a Python program to find the key with the maximum value in a dictionary.

# Solution 3
def get_key_with_max_value(dictionary):
    max_value = max(dictionary.values())
    for key, value in dictionary.items():
        if value == max_value:
            return key

# Example usage:
my_dict = {'a': 10, 'b': 20, 'c': 15}
result = get_key_with_max_value(my_dict)
print(result)


# Question 4: Write a Python program to remove a key from a dictionary.

# Solution 4
def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
remove_key(my_dict, 'b')
print(my_dict)


# Question 5: Write a Python program to check if a key exists in a dictionary.

# Solution 5
def key_exists(dictionary, key):
    return key in dictionary

# Example usage:
my_dict = {'a': 1, 'b': 2, 'c': 3}
result = key_exists(my_dict, 'b')
print(result)
