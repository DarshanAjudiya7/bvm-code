'''
 Exercise 5: Check Variable Types
Problem Statement: Write a program to check the type of a variable using type().'''




int = 5 #integer data type
float_ = 5.5 #float data type
string = "Hello" #string data type
list_ = [1, 2, 3, 4, 5] #list data type
tuple_= (1, 2, 3, 4, 5)  #tuple data type
set_= {1, 2, 3, 4, 5}   #set data type
dict_ = {1: 'one', 2: 'two', 3: 'three'} #dictionary data type
bool_ = True #boolean data type




print(f"Integer: {type(int)}")
print(f"Float: {type(float_)}")
print(f"String: {type(string)}")
print(f"List: {type(list_)}")
print(f"Tuple: {type(tuple_)}")
print(f"Set: {type(set_)}")
print(f"Dictionary: {type(dict_)}")
print(f"Boolean: {type(bool_)}")

a = input("Enter data: ")
check = eval(input(print(f"{type(a)}")))
