print("emter student's physics,chemistry and maths marks.")

phy = int(input("Enter physics marks between 0 to 100:"))
if phy<= 0 or phy>=100:
    print("error") 
chem = int(input("Enter chemistry marks between 0 to 100:"))
if chem<= 0 or chem>=100:
    print("error")
maths = int(input("Enter maths marks between 0 to 100:"))
if maths<= 0 or maths>=100:
    print("error")

avg = (phy + chem + maths) / 3

print("average marks of three subjects are :", avg)

if avg >= 75:
    print("Eligible for Admission")
    if avg >= 90:
        print("You qualify for a scholarship")
else:
    print("Not Eligible")
