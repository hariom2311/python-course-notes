# Question 1: Write a Python program to swap the values of two variables without using a temporary variable.

# Solution 1
a = 5
b = 10
a, b = b, a
print("Swapped values: a =", a, "b =", b)


# Question 2: Write a Python program to convert a given temperature in Fahrenheit to Celsius.

# Solution 2
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Temperature in Celsius:", celsius)


# Question 3: Write a Python program to calculate the area of a rectangle using user input for length and width.

# Solution 3
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
area = length * width
print("Area of rectangle:", area)


# Question 4: Write a Python program to check if a given number is even or odd.

# Solution 4
number = int(input("Enter a number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Question 5: Write a Python program to check if a given year is a leap year or not.

# Solution 5
year = int(input("Enter a year: "))
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
