# pattern 1
num1 = int(input("Enter the number of rows for Pattern 1: "))

for i in range(1, num1 + 1):
    print('*' * i)


for i in range(num1 - 1, 0, -1):
    print('*' * i)


# pattern 2
num2 = int(input("Enter the number of rows for Pattern 2: "))

for i in range(1, num2 + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()


#pattern 3
num3 = int(input("Enter the number of rows for Pattern 3: "))

for i in range(num3, 0, -1):
    for j in range(i):
        print(chr(65 + i - j - 1), end=' ')
    print()








