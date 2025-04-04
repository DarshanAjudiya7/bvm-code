def item_bill():
    print()

import datetime
import pandas as pd
import os
import numpy as np
q={}
r=[]
names=[]
w=[]
y = {}  
ti=[]



d = {
    "ch": "Chinese Puff",
    "no": "Normal Puff",
    "je": "Jeera Soda",
    "bu": "Butter Dabeli",
    "cd": "Cheese Dabeli",
    "pi": "Pizza",
    "te": "Tea",
    "do": "Dosa",
    "sa": "Samosa",
    "va": "Vadapav",
    "co": "Coffee"
}

g={  "ch":20,
     "no":15,
     "je":10,
     "bu":30,
     "pi":60,
     "te":10,
     "do":90,
     "sa":30,
     "va":35,
    "co":20,
    "cd":40
}



print("------------------------------")
for  u in range(1, 16):
    u = input("Enter item name: ") 
    f = input("Enter Qty: ")
    print("------------------------------")

    


    if(u=="d"):
      print("------------------------------")
      print(y)
      print("------------------------------")
      z=sum(r)

      print(f"              Total Bill--{z}")
      print("------------------------------")
     
      
      

      break
        



    elif(u in d ):
    
        value = d.get(u)  
        total = g[u] *int(f) 
        q[d[u]] = g[u]
        print(f"   price of {value}--  {g[u]}")
      
        print("                  -----------")
        print(f"         Qty  --      {f}")
        print("                  -----------")
        
        print(f"         Total--     {total}")
        print("------------------------------")
        
        y.update({value:f})
        r.append(int(total))
        w.append(int(f))
        names.append(str(value))


    

    else:

         print(f"Item '{u}' is not available!")
         print("------------------------------")

