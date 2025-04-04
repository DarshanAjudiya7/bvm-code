from gmail import create_gmail
h= create_gmail()
with open("gmail.txt","r") as f:
 w=f.read()

 
 
 print("          ------Example How to  make a password------\n")
print("          --**** password should minimum 8 digit**--\n",end="  ")
print("     &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n")
print("  (1)               small and capital latter \n ",end=" ")
print("(2)               charater use to password (%,$,@,#,&,*)\n",end="  ")
print("(3)               number to use in password\n",end="  ")
print("\n      &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
s=[]
f=open("gmail.txt","a")

print("   ------------------------------")
a=input("     Enter password  :")
print("   ------------------------------")
s.append(a)
def has_upper_and_lower(s):
    has_upper = any(c.isupper() for c in s)
    has_lower = any(c.islower() for c in s)
    return has_upper and has_lower
for i in s:
  

 
   if (len(i)>=8):
       if has_upper_and_lower(i):
           if(i.count("@")>=1 or i.count("%")>=1 or i.count("$")>=1 or i.count("#")>=1 or i.count("&")>1 or i.count("*")>1 and i.count(int)>=1):
              
               if( i.count("1")>=1 or i.count("2")>=1 or i.count("3")>=1 or i.count("4")>=1 or i.count("5")>=1 or i.count("6")>=1 or i.count("7")>=1 or i.count("8")>=1 or i.count("9")>=1 or i.count("0")>=1):
                  
                  f.write(i)
                  f.close()
                

                  with   open("password.txt","r") as f:
                   
                    e=f.read()
                  print("") 
                  print("      you are Email-id:",w)
                  print("      you are password:",e)
                  print("") 
               else:
                     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
                     print("       ----enter the number----") 
                     print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")

           else:
               print("   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")      
               print("    ---- charater  should  to use password (%,$,@,#,&,*)----")
               print("   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
       else:  
          print("   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")         
          print("     ----small and capital latter----")
          print("   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
   else: 
        print("   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")         
        print("        ----please password should minimum in 8 digit----")
        print("   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")