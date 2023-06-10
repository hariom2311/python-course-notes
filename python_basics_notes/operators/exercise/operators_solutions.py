# Exercise Questions Solutions:

# Question 1: Write a Python program to calculate the area of a triangle using the formula: area = (base * height) / 2. Take user input for the base and height.

# Solution 1:
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = (base * height) / 2
print("Area of the triangle:", area)


# Question 2: Write a Python program to calculate the circumference and area of a circle using the formulae: circumference = 2 * π * radius and area = π * radius^2. Take user input for the radius.

# Solution 2:
import math

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2
print("Circumference of the circle:", circumference)
print("Area of the circle:", area)


# Question 3: Write a Python program to calculate the square root of a given number using the math module. Take user input for the number.

# Solution 3:
import math

number = float(input("Enter a number: "))
square_root = math.sqrt(number)
print("Square root of the number:", square_root)


# Question 4: Write a Python program to check if a given number is divisible by both 3 and 5. Take user input for the number and print "Divisible" if it is divisible, otherwise print "Not divisible".

# Solution 4:
number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 == 0:
    print("Divisible")
else:
    print("Not divisible")


# Question 5: Write a Python program to perform bitwise operations on two integers. Take user input for the two numbers and perform bitwise AND, OR, and XOR operations on them.

# Solution 5:
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
bitwise_and = number1 & number2
bitwise_or = number1 | number2
bitwise_xor = number1 ^ number2
print("Bitwise AND:", bitwise_and)
print("Bitwise OR:", bitwise_or)
print("Bitwise XOR:", bitwise_xor)

