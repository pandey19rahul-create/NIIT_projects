#for i in range(0,6):
#    print(i)
##numbers=tuple(range(0,5,1))
##print(numbers)
##for i in range(1,11,2):
##    print(i)
#for i in  range(10,0,-1):
#    print(i)
'''
alogoritm
    
algorithm is a step by step process to list down all steps  that is required to  solve a specific problem

flow chart
flow chart is pictorial representation of our algorithm

'''
'''
WAP to find the maximum number from two number
step 1:create two variable
step 2:compare both the variable.
If first variable greater than second variable tha go to step 3 or
if second variable is greater than go to step 4
step 3:print first number is max
step 4: print second number is max
'''
#WAP if a person is capable of voting or not
'''
age=int(input("Enter your age:"))
if age>18:
    print("You are eligible to vote")
elif age<18:
    print("You are not eligible to vote")
else:
    print("You are also eligible of vote")
'''
#ternary statment
'''syntax:
true_part if condition else false_part

'''
# nested if else

# wap to compare three number and find the maximum number
'''
a=int(input("Enter the first number:"))
b=int(input("Enter the seconmd number:"))
c=int(input("Enter the third number:"))

if a==b  and b==c:
    print("all is same")
else:
    if a>b:
        if a>c:
            print("a is maximum")
    else:
        if b>c:
            print("b is maximum")
        else:
            print("c is maximum")
'''        

##
##day=input("Enter the day code(M,t,W,T,F,S,s) :")
##match day :
##    case "M":
##        print("Monday")
##    case "t":
##        print("Tuesday")
##    case "W":
##        print("Wednesday")
##    case "T":
##        print("Thursday")
##    case  "F":
##        print("Friday")
##    case  "S" :
##        print("Saturday")
##    case  "s":
##        print("Sunday")
##    case  _:
##        print("Invalid Option")

#WAP create a menu driven program for fastfood order
##
##print("Press 1 for Burger")
##print("Press 2 for Pizza")
##print("Press 3 for Sandwich")
##choice=int(input("Enter your choice:"))
##match choice :
##    case 1:
##        print("You ordered Burger")
##    case 2:
##        print("Press 1 for Cheese Burst Pizza")
##        print("Press 2 for Thin Crust Pizza")
##        print("Press 3 for Fresh Dough Pizza")
##        choice =int(input("Enter your choice:"))
##        match choice :
##            case 1:
##                print("You ordered Cheese Burst Pizza ")
##            case 2:
##                print("You ordered Thin crust pizza")
##            case 3:
##                print("You ordered Fresh Dough Pizza")
##                
##    case 3:
##        print("you ordered Sandwitch")
##        

#WAP to print  1 to 10
##i =1
##while i<=10:
##    print(i)
##    i+=1
    
##string="Hello I am Rahul Pandey"
##vowel="aeiou"
##no_vowel=[char for char in string if char.lower() not in vowel]
##
##print("".join(no_vowel))
##

##even_no=[num for num in range(51) if num%2==0 ]
##print(even_no)
##
##list=["apple","banana","cherry","date"]
##length=[len(i) for i in list ]
##print(length)

##string="Python porgramming"
##vowel="aeiou"
##list1=[char.upper() for char in string if char not in vowel]
##print(list1)


##list=[1,2,3,4,5,6,7,8,9,10]
##square_list=[num*num for num in list]
##print(square_list)
##
###Create a list of uppercase words from a list of words
##words=["apple","banana","cherry"]
##upper=[word.upper() for word in words ]
##print(upper)


#Create a list of uppercase words from a list of words
##matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
##flat_list=[item for sub_list in matrix for item in sub_list]
##print(flat_list)
##
##numbers=[-5,10,-3,22,-1,0,7]
##new_list=[num for num in numbers if num>0]
##print(new_list)
##fruits=["apple","banana","kiwi","mango"]
##char="a"
##a_list=[c for c in fruits if char  in c]
##print(a_list)
##n1=int(input("Enter the first number:"))
##n2=int(input("Enter the second number:"))
##for i  in range(n1,n2+1):
##    for j in range(1,11):
##        print(i,"x",j,"=",i*j)
##        
##matrix=[[1,2,3],[4,5,6],[7,8,9]]
##sum=0
##for i in range(len(matrix)):
##    for j in matrix[i]:
##         sum=sum+j        
##print(sum)
##
##for i in range(1,6):
##    for j in range(1,6):
##        print(j,end=" ")
##    print()    

"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
##for i in range(1,6):
##    for j in range(1,i+1) :
##        print(j,end=" ")
##    print()    
####        
##str="Rahul Pandey"
##age=28
##formatted_str="The person name %s having age %d is very great trainer."%(str,age)
###print(formatted_str)
##formatted_str1="The person name {} having age {} is very greaty trainer".format(str,age)
###print(formatted_str1)
##formatted_str2="The person name {0} having age {1} is very great trainer".format(str,age)
###print(formatted_str2)
##formattted_str3="The Person age {age} having name {str} is very great trainer".format(str=str,age=age)
###print(formattted_str3)
##formatted_str4="The person age {umar} having name {name} is very greaty trainer".format(umar=age,name=str)
###print(formatted_str4)
##print("DHRUV".center(10,"*"))


#slicing
##
##s="Dhruv"
##print(s[::-1])
##print(s[:len(s):1])
##print(s[::])
##print(s[0:3])
##print(s[2:5])
###print(s)
##
##
##
##l=[]
##print(l)
##total=int(input("Enter the number of element:"))
##for i in range(total):
##    ele=int(input("Enter the element:"))
##    l.append(ele)
###l.insert(1,78)
##print(l)    
###l1=[1,2,3,4,5,6]
'''l[0]=11
print(l)
##popped_element=l.pop()
##print(popped_element)

l.remove(1)
print(l)
del l[0]
'''
'''
del l[0]
print(l)
'''
'''
del l[0:3]
print(l)
'''

##t=(34,5,.78,65,32,78)
##count=t.count(34)
##print(count)
##t.clear
##
##l=[12,2,3,4,5]
##ans=[]
##for i in l :
##    ans.append(i**2)
##print(ans)

'''
List Comprehension
Syntax 
 [value for var in collection]

 '''
##ans=[i**2 for i in l ]
##print(ans)
##
##user_name=input("Enter your name :")
##age=int(input("Enter your age:"))
##print(f"Welcome {user_name} of {age} year old to the world  of quality Education")
'''
text="  Hello ,Python!  "
text=text.strip()
print(text)
str="Learning Python is fun"
str=str.title()
print(str)
'''
##str1="banana split"
##total=str1.count("a")
##print(total)
##
##sentence="Python is a powerful language"
##replace=sentence.replace("powerful","versatile")
#print(replace)
##str="apple,banana,cherry,date"
##print(str.split(sep=","))
##list=["Coding","is","awesome"]
####print(" ".join(list))
##str="Programming"
####print(str.index("ing"))
##filename="report.pdf"
#print(filename.endswith(".pdf"))
##str="Welcome2026"
##print(str.isalnum())

##msg="PYTHON"
##print(msg.lower())

##count=5
##print("You have %d unread message."%(count))
##
##text="12345"
##print(text.isdigit())

##str="Saksham is a good boy"
##print(str[::-1])
##
##filename="document.tar.gz"
##ext=filename.rfind(".")
##print(filename[ext:])
##
##print(filename[-3::])

data="name:John,age:25"
#print(dict(data))
##comma=data.split(",")
##print(comma)
##for item in comma :
##    key,value=item.split(":")
##    print(f"key:{key},value:{value}")
##          
##
##
##list=[-23,4.5,"Rahul",True]
##print(list)

##tuple=(1,2,3)
##print(tuple[1])
##
##numbers=[10,20,30,40,50,60]
##print(numbers[1:4])

##colors=["red","blue"]
##colors.append("green")
##print(colors)
##colors.insert(1,"yellow")
####print(colors)
####nums=[1,2,3,2,4,2]
####print(nums.count(2))
####print(colors.count("blue"))

##scores=[45,12,89,34,78]
##print(sorted(scores))
##letters=["a","b","c"]
##letters.reverse()
##print(letters)
##t1=(1,2)
##t2=(3,4)
##t3=t1+t2
##print(type(t3))
###print(type(tuple))

##coordinates=(10.5,20.3)
##x,y=coordinates
##print(x,y)

##
##list=[55,12,99,3]
##maximum_value=max(list)
##print(maximum_value)
##minimum_value=min(list)
##print(minimum_value)
##
##list=[10,20,30,40]
##print(sum(list))

##list1=[1,2]
##list2=[3,4]
##list1.extend(list2)
##print(list1)
##list1[0]=99
##print(list1)
####
##t1=(1,2,3,4)
##t1[0]=63
##print(t1)
##original=[1,2,3]
##copy_list=[]
##for i in original :
##    copy_list.append(i)
##
##copy_list[0]=37    
##print(original)
##print(copy_list)

##t=(1,2,[3,4])
##t[2][1]=5
##print(t)

##l=[1,2,3]
##tuple=tuple(l)
##print(tuple)
##list1=list(tuple)
##print(list1)

items=["apple","banana","cherry","banana"]
##items.remove("banana")
##print(items)
##items.pop(1)
##print(items)


##s={1,2,3,4,5,6,7,8,9,1,2,3,4,5}
##s1={2,3}
####print(s)
####s.add( 23)
####print(s)
####s.update(s1)
##print(s)
###del s
###print(s)
##
###print(s.union(s1))
####print(s.intersection(s1))
####print(s.difference(s1))
####print(s-s1)
##print(s.symmetric_difference(s1))
"""
frozen set
# it is represnted as
fs=frozeset({})
"""
##fs=frozenset({})
##fs=frozenset({34,56,89,23})
##print(fs)
##print(type(fs))
dic={"id":123,"name":"Rahul","age":20}
#print(dic)
#print(dic["school"])
#dic["name"]="Sakshi"
#print(dic)
#dic1={"id":124,"name":"Rahul","age":28}
#dic1.pop("name")
##dic.popitem()
##print(dic)

##for k, v in dic.items():
##    print(f"{k}======>{v}")
    
##a=3
##b=5
##b,a=a,b
##print(a,b)
print(list(dic.values()))
