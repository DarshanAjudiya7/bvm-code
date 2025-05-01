temp = float(input("Enter the temperature(in celsius): "))

if(temp < 15):
    print("It is cold")
elif(temp >= 15 and temp < 30):
    print("It is warm")  
elif(temp > 30):
    print("It is hot")
else:
    print("Something else")    