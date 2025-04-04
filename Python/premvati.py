import datetime
import random
import pandas as pa


from s import  item_bill,r,w,names
u= item_bill()
f= item_bill()



ww=input("enter counter no:")
print("\n\n")

i=6

print("\n           APC Chhatralay           ")
print("             Sardar Patel Marg,")  
print(" Vallabh Vidyanagar  , Gujarat  388120\n")

print("Date:",end=" ")
print(datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S"))
print(end="                                   ")

print("station:",i)

a=random.randint(1,500)
print("Token #:",end=" ")
print(a)
print(end="                                   ")
print("Quick Sell")
print("---------------------------------------------")
print("Qty",end="       ")
print("Item",end="                         ")
print("Amount")
print("---------------------------------------------")


for qty, name, amt in zip(w, names, r):
    print(f"{qty:<10}{name:<30}₹{amt}")


print("                               --------------")
print("                               --------------")
print(f"Total Charge:                       {sum(r)}")
print(f"Visa Card:                          {sum(r)}")

print("*")

print("            GST NO:24AABTP2866J1ZC              ")
print("               Jay Swaminarayan              \n\n")




print("     THANK YOU FOR VISIT !........\n\n")
print(f"                 Counter:{ww}            \n")
print("Server : Cashier 2",end="                   ")
print("Station: 6")
print("TOKEN #",a)
print("---------------------------------------------")
print("Qty",end="       ")
print("Item",end="                         ")
print("Amount")
print("---------------------------------------------")


for qty, name, amt in zip(w, names, r):
    print(f"{qty:<10}{name:<30}₹{amt}")

print("*\n\n\n")