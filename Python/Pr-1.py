name = input("Enter your name :")
age = int(input("enter age :"))
string = input("enter your coures :")
graduation = int(input("enter year :"))
left = graduation - (2024 - (18  - age))

print("------ Student Enrollment Form ------")  

print("Name : ", name)
print("Age :", age)
print("Course:", string)
print("Expected Graduation Year : ", graduation)
print("Years left Until Graduation :", left)

print("-------------------------------------")