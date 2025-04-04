'''Ex 1'''
print("Hello bvmiates...!!!")

'''Ex 2'''
name = input("Enter your name:")
age = int(input("Enter youe age:"))
print("Hello...!!", name , "Your age is  ",age)

'''Ex 3'''
'''
Author Name : Darshan P Ajudiya
Work : Pythons's first programme
Date : 27/02/2025
'''
print("This is my multi line comment")

'''Ex 4'''
x = 23
y = 7.45
name = "samir"
colors = ["red", "green", "white"]
coordinates = (20,50,90)
unique_numbers = {4,5,6}
person = {"name" : "heer" , "age" : 22}
is_active = False

print("integer :", x)
print("float :", y)
print("string :", name)
print("list :", colors)
print("tuple :", coordinates)
print("set :",unique_numbers)
print("dictionary :", person)
print("boolean :", is_active)

'''Ex 5'''
x = 52
y = 45.23
is_active = True

print("Type of x :", type(x))
print("Type of y :", type(y))
print("Type of is_active :", type(is_active))

'''Ex 6'''
num_str = "345"
num_int = int(num_str)
num_float = float(num_str)

print("string : ", num_str)
print("integer :", num_int)
print("float :", num_float)

'''Ex 7'''
numbers = [4,5,6,7,8]
result = sum(numbers)

print("numbers", numbers)
print("sum", result)

'''Ex 8'''
person = {
"name": "Darshan",
"age": 17,
"city": "Rajkot"
}

print("Keys:", person.keys())
print("Values:", person.values())

'''Ex 9'''

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))

print("Sum:", n1 + n2)
print("Difference:", n1 - n2)
print("Product:", n1 * n2)
print("Division:", n1 / n2)
print("Remainder:", n1 % n2)
print("Exponentiation:", n1 ** n2)

'''Ex 10'''
f_num = float(input("Enter a floating-point number: "))

int_num = int(f_num)
print("Integer value:", int_num)

convert_float = float(int_num)

print("Converted back to float:", convert_float)

real_part = float(input("Enter the real part of the complex number: "))
imaginary_part = float(input("Enter the imaginary part of the complex number: "))

c_num = complex(real_part, imaginary_part)
print("Complex number:", c_num)
print("Real part:", c_num.real)
print("Imaginary part:", c_num.imag)
print("Conjugate of the complex number:", c_num.conjugate())

'''Ex 11'''
import datetime

now = datetime.datetime.now()
formatted_now = now.strftime("%A, %B %d, %Y %H:%M:%S")
print("Current Date and Time:", formatted_now)

user_date = input("Enter a target date (YYYY-MM-DD): ")
target_date = datetime.datetime.strptime(user_date, "%Y-%m-%d")
days_left = (target_date - now).days
print("Days left until target date:", days_left)

future_date = now + datetime.timedelta(days=45)
print("Date after 45 days:", future_date.strftime("%Y-%m-%d"))

'''Ex 12'''

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))

sum = n1 + n2 + n3
product = n1 * n2 * n3
difference = n1 - n2 - n3

print("Sum of numbers:", sum)
print("Product of numbers:", product)
print("Difference of numbers:", difference)

all_positive = (n1 > 0) and (n2 > 0) and (n3 > 0)
print("All numbers are positive:", all_positive)

is_sum_greater = sum > 100
print("Sum greater than 100:", is_sum_greater)

'''Ex 13'''

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Bitwise AND:", num1 & num2)
print("Bitwise OR:", num1 | num2)
print("Bitwise XOR:", num1 ^ num2)
print("Bitwise NOT (num1):", ~num1)
print("Bitwise Left Shift (num1 by 2):", num1 << 2)
print("Bitwise Right Shift (num2 by 2):", num2 >> 2)

a = [num1]
b = [num1]
c = a
print("a is b:", a is b) 
print("a is c:", a is c) 
print("a == b:", a == b) 