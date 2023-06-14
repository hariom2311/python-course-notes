# Quiz Questions and Answers - Dictionary Data Type

quiz_questions = [
    {
        "question": "Q1. Which symbol is used to access a value in a dictionary?",
        "options": ["a) .", "b) :", "c) [", "d) ("],
        "answer": "c) ["
    },
    {
        "question": "Q2. How do you check if a key exists in a dictionary?",
        "options": ["a) using the in keyword", "b) using the exists() method", "c) using the find() method", "d) using the has_key() method"],
        "answer": "a) using the in keyword"
    },
    {
        "question": "Q3. What happens when you try to add a new key-value pair to a dictionary using an existing key?",
        "options": ["a) The new value overwrites the existing value", "b) The new value is appended to the existing value", "c) An error is raised", "d) The existing value is deleted and replaced with the new value"],
        "answer": "a) The new value overwrites the existing value"
    },
    {
        "question": "Q4. How do you remove a key-value pair from a dictionary?",
        "options": ["a) using the remove() method", "b) using the delete() method", "c) using the discard() method", "d) using the del keyword"],
        "answer": "d) using the del keyword"
    },
    {
        "question": "Q5. What will be the output of the following code?\nmy_dict = {'apple': 2, 'banana': 3, 'cherry': 1}\ndel my_dict['banana']\nprint(my_dict)",
        "options": ["a) {'apple': 2, 'banana': 3, 'cherry': 1}", "b) {'apple': 2, 'cherry': 1}", "c) {'banana': 3, 'cherry': 1}", "d) Error"],
        "answer": "b) {'apple': 2, 'cherry': 1}"
    },
    {
        "question": "Q6. How do you retrieve all keys from a dictionary?",
        "options": ["a) using the keys() method", "b) using the values() method", "c) using the items() method", "d) using the get() method"],
        "answer": "a) using the keys() method"
    },
    {
        "question": "Q7. What is the difference between the get() method and the [] operator when accessing values in a dictionary?",
        "options": ["a) The get() method returns None if the key doesn't exist, while the [] operator raises an error", "b) The get() method returns the value if the key exists, while the [] operator raises an error", "c) The get() method allows you to specify a default value if the key doesn't exist, while the [] operator returns None", "d) The get() method and the [] operator are equivalent and can be used interchangeably"],
        "answer": "c) The get() method allows you to specify a default value if the key doesn't exist, while the [] operator returns None"
    },
    {
        "question": "Q8. How do you merge two dictionaries into one?",
        "options": ["a) using the combine() method", "b) using the append() method", "c) using the merge() method", "d) using the update() method"],
        "answer": "d) using the update() method"
    },
    {
        "question": "Q9. What is the time complexity of accessing a value in a dictionary by its key?",
        "options": ["a) O(1)", "b) O(log n)", "c) O(n)", "d) O(n^2)"],
        "answer": "a) O(1)"
    },
    {
        "question": "Q10. What will be the output of the following code?\nmy_dict = {'apple': 2, 'banana': 3, 'cherry': 4}\nmy_dict.pop('banana', 0)\nprint(my_dict)",
        "options": ["a) {'apple': 2, 'banana': 3, 'cherry': 4}", "b) {'apple': 2, 'cherry': 4}", "c) {'banana': 3, 'cherry': 4}", "d) Error"],
        "answer": "b) {'apple': 2, 'cherry': 4}"
    }
]
