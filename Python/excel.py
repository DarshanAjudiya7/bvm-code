import random
import pandas as pd
import os



id=[]
a=[]
i=[]
r=[]
h=[]
l=[]

k={"id":id,
"name":a,
"city":i,
"birth":r,
"phone":h,
"blood":l}

print("----------------------------------------")
for j in range(1,2):
    j=print("ID card ",j)
    print("----------------------------------------")
    idb=random.randint(1,300)
    ab=input("Enter your name:")
    ib=input("city name:")
    rb=(input("birth Date:"))
    hb=int(input("Enter your phone Number:"))
    lb=input("Enter blood grupo:")
    dd=hb/1000000000
    ss=int(dd)
    ddd=str(idb)
    dddd=str(hb)
    
   


    if(ab!="d" ):
       if(ib ):
         
           if( rb ):
              
               if(ss==1 or ss==2 or ss==3 or ss==4 or ss==5 or ss==6 or ss==7 or ss==8 or ss==9  ):
                 
                 
                  if( lb=="" or lb):
                      
                      id.append(ddd)
                      a.append(ab)
                      i.append(ib)
                      r.append(rb)

                      h.append(dddd)
                      l.append(lb)

                      print("----------------------------------------")
                      print("ROLL NUMBER:",idb)
                      print("----------------------------------------")
                      print("Susesfully")
                      print("----------------------------------------")
                      
                     
                  else:
                     print()
               else:
                print("enter 10 digit number")
           else:
             print("please enter your birth date")
       else:
        print("Enter city name")
    else :
        print("please enter you full name")

df=pd.DataFrame(k)
df.to_excel("darshit.xlsx",index=False)
                        
                 
os.startfile("darshit.xlsx")