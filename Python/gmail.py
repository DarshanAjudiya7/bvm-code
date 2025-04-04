def create_gmail():
  print()
ar=[]
f = open("gmail.txt", "w")
print("\n")
print("           ------------------------------")
gmail=input("       please enter the Email id:")
print("           ------------------------------")
ar.append(gmail)
for j in ar:
 

 if (j.count("@gmail.com")==1 ):
     
    f.write(j)
    f.close()

    with open("gmail.txt", "r") as f:
        h= f.read()
    print("..............................")
    print("       Your email id            :",h)
    print("..............................")
    

    
   
    
 elif(len(j)==14):
    print("       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("         could you please  enter Email id\n try again")
    print("       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    break

 else:
  print("    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  print("        please and type of  @gmail.com")
  print("    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
  break