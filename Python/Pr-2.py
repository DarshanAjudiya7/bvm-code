print("<--------Coffee shop menu-------->")
print("\nCoffee - 70Rs.\nTea - 50Rs.\nSandwich - 100Rs.")
item_choise = input("Enter item as your choise : ")
print(item_choise)
item_q = int(input("Enter item quentity : "))
print(item_q)

if item_choise == "coffee":
    print("you have to pay this amount : ",item_q* (70 + 1.8))
elif item_choise == "tea":
    print("you have to pay this amount : ",item_q* (50 + 1.8))
elif item_choise == "sandwich":
    print("you have to pay this amount : ",item_q* (100 + 1.8))  
else:
    print("wrong input by you")    

import datetime
now = datetime.datetime.now()
formatted = now.strftime("%A, %B %d, %Y %H:%M:%S")
print("Date and Time:", formatted) 

print("\n----------------------------------")
