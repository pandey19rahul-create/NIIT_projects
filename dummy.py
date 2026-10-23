#operator

10/5

#Q what is the actual use of assignment operators
'''
a=12*6/((2-10)+4)
print(a)
'''
"""
a=input("Enter the class in which u study:")
print(a)
a=int(a)
print(f"{int(a)}-------{type(a)}")
a=float(a)
print(f"{float(a)}-----{type(a)}")
a=bool(a)
print(f"{bool(a)}------{type(a)}")
"""
'''f1=float(input("Enter the float number:"))
i1=int(f1)
print(i1)
print(f"{f1}------{i1}---the first value is of decimal number where the number after decimal appear but in integer it is only showing the value before the decimal point")
'''
'''
b1=bool(input("Enter the boolean value:"))
i1=int(b1)
s1=str(b1)
print(b1)
print(i1)
print(s1)
'''
'''
int1=45
flt1=67.89
str1="Arvind"
list=[1,2,"I","am"]
tup1=(1,2,"I","am")
dict={"name":"Rahul","place":"VNS"}

print(int1,"----",type(int1),"-----",id(int1))
print(flt1,"----",type(flt1),"-----",id(flt1))
print(str1,"----",type(str1),"-----",id(str1))
print(list,"----",type(list),"-----",id(list))
print(tup1,"----",type(tup1),"-----",id(tup1))
print(dict,"----",type(dict),"-----",id(dict))
'''
'''
a=10
b=10

print(id(a))
print(id(b))
b=9
print(id(a))
print(id(b))
'''
'''
print("Welcome to the proghramming",end="&")
print("Rahul")
'''

name="Rahul"
#print(name[0])
#print(name[-1:-4:-1])
#print(name[-1:-6:2])
#print(len(name))

'''
name=" Rahul Pandey "
name1="sakshi pandey"
print(name.lower())
print(name1.upper())
print(name1.capitalize())
print(name1.title())
print(name.strip())
print(name1.split())
word=[" Sakshi","Pandey"]
print(' '.join(word))
print(name.find("Pandey"))
print(name1.replace("sakshi","Lado"))
'''
'''
from string import Template

name="Alice"
age=30
template=Template("My name is $name and I am $age year old.")
formatted_str=template.substitute(name=name,age=age)
print(formatted_str)
'''
num=10

if num>0:
    print("The number is positive")
    
print("This statment always runs")    


age=int(input("Enter the age:"))
if age>=18:
    print("You are eligible to vote")
print("Program ended")



