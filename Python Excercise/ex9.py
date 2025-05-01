'''
Exercise 9: Arithmetic Operations
Problem Statement: Write a Python program that performs the following operations on two
user-provided numbers:
1. Calculates and prints their sum, difference, product, and division result.
2. Finds and displays the remainder when the first number is divided by the second.
3. Calculates and prints the result of raising the first number to the power of the second.
'''

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print(f"Sum: {num1 + num2}")
print(f"Difference: {num1 - num2}")
print(f"Product: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Remainder: {num1 % num2}")
print(f"Power: {num1 ** num2}")
