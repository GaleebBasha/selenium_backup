"""
Features


1. Py is dynamically data typed

in c/java
int a = 10
String s1 = "Hello"

in Py
a=10
s1="Hello"

2. Python is compiler based
Programming-C,CPP,Java,Node,.Net - Compiler - executes the code in blocks(many lines together)
test.c --> compile --> gcc test.c --> test.obj --> execute --> OP


Scripting-bash,tcl,Py,groovy,psh - Interpreter - executes line by line
python file.py --> op

3. Memory Manager
in c
----
int a = 10
*p = &a --> assigning mem to a var

in java/Py
---------
dev dont need to worry about memory allocation, py has a deamon called Memory Manager


4. Garbage Collector
in c
its again dev resp to clear the memory at the end of exec

in py
a deamon called GC - it takes care of deallocation of memory


5. Platform independent - py,java
6. Packages/Libraries - 200k
7. OOPs - CPP, Java, Python, Node JS
8. Easy to understand and enhancements

# comments  - two reasons
# 
"""
# IDEs - PyCharm, VS Code, Intellij, Eclipse

# this is to print hello world
# print('Hello World')
# Quotes ',", """

a = "Hello everyone"
b = 'Hello everyone'

s1 = '''heloo im galeeb from AP and I havejk,shj
hkjlkdnfjjknmndsb
hjnmnbjj
bjn nmbmnjk
hjnmbjjk'''


# Data Types - int,float, str, bool - List, String, Tuple, Dictionary and set


# String - quotes are the blind code

# a = 10
# a1 = "True"

# print(type(a))


s1 = "hello, Today Is Friday"
    # 0123456789....
# index 
# print(s1[-5])
# print(s1[100])

# slicing - to pick sub string from a str
# print(s1[4:]) # exludes the dest index
# print(s1[::-1]) # reversing using slicing

# Manipulations
# ind = s1.index('Is')
# print(ind)

# occ = s1.count("az")
# print(occ)

# l1 = s1.split("are") # returns a list
# print(l1)

# res = s1.find('Iz')
# print(res)

# print(s1)
# res = s1.rstrip(" ")
# print(res)

# s1 = "hel1lo w2orl3d we53locme"
# res = s1.islower()
# s1 = "HELLO ALL, WELCOME"
# res = s1.isupper()
# s1 = "gjhkjkjghhhkgjhlkdsdaaljnvhjGHJHBJHGHKv"
# res = s1.isalpha()

# s1 = "HelloWelcome"
# res = s1.isalnum()
# s1 = "324354643456"
# res = s1.isdigit()
# print(res)


# s1 = "Hello How are you"
# up = s1.upper()
# print(up)

# low = up.lower()
# print(low)

# format
# name = "John"
# age=29
# print("Hi I am {} of {} from AP".format(name,age))


# name = input("Enter your Name\t:")
# age = input("Enter Your Age\t:")
# username = "HDFC_{}_{}".format(name,age)
# print(username)

# res = s1.startswith("Hello, T")
# res = s1.endswith("y")
# print(res)

# res = s1.swapcase()
# res = s1.replace("day", "XYZ")


# print(res)

# List - data tpe - heterogeneous - []

l1 = [1,1.11,False, "John"]

l2 = [2,3,4,5,6,7,11,12,43,25,43,43]

# index and slicing

# print(l2[-3]) # it can fetch only one elem at a time

# slicing - fetching a sub list from a list


# print(l2[2:6]) # dest/end index is excluded

# print(l2[::-1]) # reversing a list using slicing

# manipulation functions

# l2.append(123) # it always keeps ur data at the end of the list
# print(l2)

# l2.insert(2, 222) # can keep ur data at a specific index
# print(l2)
# l2 = ["aab","aba","bba","bab"]

# l2.sort(reverse=True) # homogeneous
# print(l2)

# l2.reverse()
# print(l2)
# l3 = [111,222,333]
# l3.extend(l2)
# print(l3)

# l2.remove(43) # by value
# print(l2)

# l2.pop(5) # by index
# print(l2)

# l2.clear()
# print(l2)

# occ = l2.count(1212)
# print(occ)

# ind = l2.index(43)
# print(ind)


# type casting

# s1 = "I am doing Good"
# # connvert string to list
# l1 = list(s1)
# print(l1)


l1 = ["a","c", "d", "f","s"]
# op = "acdfs"

# s1 = "".join(l1) 
# print(s1)


# string - manipulations
s1 = "Today Is Monday"

# ind = s1.index("Ten")
# print(ind)

# occ = s1.count("dy")
# print(occ)


# res = s1.replace('dy','Day')
# print(res)


# upper_s1 = s1.lower()
# print(upper_s1)

# l1 = s1.split("xyz")
# print(l1)

s1 = "Today Is Monday"
# print("bfore strip", s1)
# s2 = s1.strip(" ")
# print("after strip,", s2)


# s1 = "jklkjhgggjhjcgxcggjhhkj"
# res = s1.isalpha()
# s1 = "1234 56"
# res = s1.isalnum()

# s1 = "7867877"
# res = s1.isdigit()

# startswith and endswith --- return Bool
# res = s1.startswith("Tod") # case sensitive
# print(res)

# res = s1.endswith(" Mnday") # case sensitive
# print(res)

# format

# name = "Ken"
# age = "32"

# print("Hello I am {} of {} years old".format(name,age))



# res = s1.capitalize()
# print(res)


# res = s1.find('fhcg')
# print(res)


# Dictionary - k,v - {}

d1 = {"ajay": 75, "vijay": "65", "jay":71, "jaya":59, "ajay":45}

# print(d1)

# we dont have index and slicing for Dict


# maniulations
# res = d1.get("xyz")

# k = d1.values()

# res = d1.items() # FOR loop
# print(res)


# add new elem to dict
# d1['priya'] = 66
# print(d1)
# d1.update({"priya":66, "rob":78})

# d1.pop("jay")
# d1.popitem()


# d2=d1.copy()
# d1.clear()
d1 = {"ajay": 75, "vijay": "65", "jay":71, "jaya":59}
# d1.setdefault("ajay", 77) # makes no change when the key is already present
# d1.setdefault("zoya", 67)
# l1 = [1,2,3,4]
# val = "xyz"
# d2 = d1.fromkeys(l1, val)
# print(d1)


# Tuple - () - looks almost similar to a list - tuple is immutable - we cant make any write ops on tuple

t1 = (1,1.11,False, "abc")
t2 = (2,3,1,6,4,9)
# occ=t2.index(91)
# print(occ)

# tuple allows index and slicing
# print(t2[4])
# print(t2[2:5])

# t3 = t1+t2
# print(t3)

# t3 = (1,2,3,[11,22,33])

# t3[3].sort(reverse=True)
# print(t3)

# Set - {}
# s1 = {1,1,1,1,2,3,4,1,1,1,1,1,"abc","abc","abc"}

# l1 = [1,1,12,2,2,2,3,3,3,1,1,2,3,3,4,5,6,6,7,7,7,8]
# s1 = list(set(l1))
# print(s1[3])

# s1 = {1,2,3,4}
# s2 = {3,4,6,5}
# print(s2)
# res = s2.difference(s1)
# print(res)


################ Condition Statements ##############
# if, elif and else
# if,eliff,else,for,while,def,class,with,try,catch,finally
# have a colon at the end of the first line of block and maintain indents from next lines of the block
# age = 11
# if(age>=18):
#    print("Eligible for voting")
#    print("Just to test")
# else:
#    print("Not Eligible yet")
   
# marks = 95
# if(marks>85):
#    print("Grade A")
# elif(marks>70):
#    print("Grade B")
# elif(marks>55):
#    print("Grade C")
# elif(marks>35):
#    print("Grade D")
# elif(marks<35):
#    print("Fail")
# else:
#    print("xz")

# print("out of Ifs")

# nested - if inside if
country="India"
state = "AP"
city = "Vizag"

# if(country=="India"):
#    print("Welcome to India")
#    if(state=="AP"):
#       print("Welcome to AP")
#       if(city=="Guntur"):
#          print("Welcome to Guntur")
#       else:
#          print("In AP but not in Guntur")
#    else:
#       print("In India but not in AP")
# else:
#    print("You are not in India")


# print("Rest code")


# loops - very imp

# marks = 98
# if(marks>18):
#    print("A")
# else:
#    print("B")


# text = "Hel12lo, Go23od Mo434rning"

# for i in text:
#    if(i.isdigit()==True):
#       print(i, end=" ")

# print("End of the loop")


# l1 = (21,11,14,20,17,31,25)
# for i in l1:
#    if(i%2==0):
#       print(i, end=" ")


# for loop can be applied only on iterable - str, list, tuple, dict
# cant be aplpied on bool, int, float

# for i in False:
#    print(i)




# d1 = {"ajay": 75, "vijay": 65, "jay":71, "jaya":59}


# # for i in d1:
# #    print(i, d1[i])

# for i,j in d1.items():
#    if(j>60):
#       print(i,j)



# range function


# l1 = [1,2,3,4,5,6,7,8,9,10,11,1]
# l1 = list(range(1,101))

# print(l1)
# for i in l1:
#    if(i%3==0):
#       print(i,end=" ")


# l1 = list(range(0,501,15))
# print(l1)




# break and continue
# l1 = range(1,11)
# for i in l1:
#    if(i==5):
#       # break # terminates the loop
#       continue
#    print(i)


# for i in range(1,6):
#    for j in range(1,i+1):
#       if(i==4):
#          break
#       print("*",end=" ")
#    print("\n")



# s1 = "Hello World"

# # for i in s1:
# #    print(i)

# count = 0
# while(count<len(s1)):
#    print(s1[count],end=" ")
#    count+=1

# d1 = {"ajay": 75, "vijay": 65, "jay":71, "jaya":59}
# print(d1.keys())
# xyz = list(d1.keys())
# count = 0
# while(count<len(xyz)):
#    print(d1[xyz[count]], xyz[count])
#    count+=1

# functions 
# def age_checker(age):
#    if(age>=18):
#       print("Eligible for Voting")
#    else:
#       print("Need to wait for {} years".format(18-age))

# # def height_checker(ht):
# #    if(ht>=150):
# #       print("Eligible for Voting")
# #    else:
# #       print("Need to wait few more years")

# age = int(input("Enter ur age\t:"))
# age_checker(age)



# def perfect_divisible(num,fact):
#    if(num%fact==0):
#       return True
#    else:
#       return False

# res = perfect_divisible(21,13)   
# print(res)



# def filter_caps(s1):
#    caps_list = []
#    for i in s1:
#       if(i.isdigit()):
#          caps_list.append(i)
#    print("Inside Fubc",caps_list)
#    return caps_list

# res = filter_caps("Hel1l2o3, Ho4w5 A7re9 0Yo-u5 D3oing?")
# print("outside of the func", res)





# def find_topper(d1):
#    max = 0
#    topper = ""
#    for i,j in d1.items():
#       if(j>max):
#          max = j
#          topper = i
#    return topper, max  

# topper, marks = find_topper({"ajay": 75, "vijay": 65, "jay":71, "vivek": 81, "jaya":59})
# print(topper, marks)




# def get_min_max(l1):
#    max = float('-inf')
#    for i in l1:
#       if(i>max):
#          max = i
#    min = float('+inf')
#    for i in l1:
#       if(i<min):
#          min = i
         
#    return max,min


# max,min=get_min_max([2,3,1,32,11,34,27.00])
# print(max,min)

# max,min = get_min_max([-2,-4,-100.34,-23])
# print(max,min)

# *args
def sample(*args):
   print(args)

# sample(1)
# sample(1,2)
# sample(1,2,3)
# sample([1,2,3,4])

# named args
# *kwargs
# def employee(name="John", age=21, org="TCS"):
# def employee( name="john", **kwargs):
#    print(kwargs, name)

# employee(name="Ram", org="HCL", city = "Hyd")
# employee(gender="M", salary=30000)
# employee()

# OOPs - Object Orient Programming
"""
1. class
2. Object
3. Self
4. Constructor
5. Types of inheritances
6. POly Morphism
7. Abstraction
8. Data Encaspulation   
9. Super function   
"""

# class Test():
#    def wishme(self):
#       print("Hello, Good Morning")
   
#    def saybye(self):
#       print("Good Bye")

# obj = Test()
# obj.wishme()
# obj.saybye()

class Calculator():
   def __init__(self,a,b):
      self.a=a
      self.b=b
      print("Im in constructor")
   def add(self):
      print("Add", self.a+self.b)
   
   def sub(self):
      print("Sub",self.a-self.b)
   
   def mul(self):
      print("Mul",self.a*self.b)
      
   def div(self):
      print("Div", self.a/self.b)

# obj = Calculator(12,10)
# obj.add()
# obj.sub()
# obj.mul()
# obj.div()

# Inheritance - concept of aquiring on class properies by another class

# Single Inheritance
# class Parent():
#    def assets(self):
#       print("Bonds: 5Cr\nDeposits: 2Cr")
   
#    def debts(self):
#       print("Loans: 20L")

# class Child(Parent):
#    def degrees(self):
#       print("Bachelors")
   
# obj = Child()
# obj.debts()
# obj.assets()
# obj.degrees()

# Multiple Inheritance
# class A():
#    def a(self):
#       print("Im class A")

# class B():
#    def b(self):
#       print("Im class B")

# class C(A,B):
#    def c(self):
#       print("Im class C")

# obj = C()
# obj.a()


# Multi Level Inheritance

# class A():
#    def a(self):
#       print("Im class A")

# class B(A):
#    def b(self):
#       print("Im class B")

# class C(B):
#    def c(self):
#       print("Im class C")

# class D(C):
#    def d(self):
#       print("Im class D")
# obj = C()
# obj.b()

# Hybrid Inheritance - 

# class A():
#    def a(self):
#       print("Im class A")

# class B():
#    def b(self):
#       print("Im class B")

# class C(A,B): # multiple inh
#    def c(self):
#       print("Im class C")

# class D(C):  # single inh/ multi level
#    def d(self):
#       print("Im class D")

# obj = D()
# obj.b()


# obj = C()
# obj.b()

# Polymorphism - many -forms 
#Overloading and overriding


# class Test():
#    def add(self,a,b):
#       print("Adding two numbers",a+b)
#    def add(self,a,b,c):
#       print("Adding 3 values", a+b+c)


# obj = Test()
# obj.add(1,3,2)


# overriding
# class Test():
#    def add(self,a,b):
#       print("Adding two nums",a+b)

# class Utility(Test):
#    def add(self,a,b,c):
#       print("Adding three nums",a+b+c)

# obj = Utility()
# obj.add(1,2,3)


# operator overloading --- +,*,/

# a = 10
# b = 20
# print(a+b)



# c = "abc"
# d="def"

# # print(c+d)

# print(3*5)
# print(c*5)

# Abstraction - hiding the complexity

# TBD


# ENcapsulation - restricting the vars

# _a is protected and __a is private

# class Test():
#    def __init__(self):
#       self._a = 10 # protected
#       self.__b = 11 # private
# class Test1(Test):
#    def __init__(self):
#       Test.__init__(self)
#       self._a = 20
#       # self.__b = 21

# obj = Test1()
# print("Value of protected var", obj._a)
# print("value of Private var", obj.__b)    
      



# class Parent():
#    def __init__(self,a,b,c):
#       self.a = a
#       self.b = b
#       self.c = c
#       print("Im in parent class")
      
# class Child(Parent):
#    def __init__(self, a, b, c, d):
#       super().__init__(a,b,c)
#       self.d = d
#       print("Im in child class", self.b)
      

# obj = Child(1,2,3,4)



# class Test():
#    def __init__(self,a,b):
#       self.a = 123
#       self.b = b

# class Test1(Test):
#    def __init__(self, a, b):
#       self.a_ = a
#       super().__init__(a,b)

# obj = Test1(1,2)
# print(obj.a, obj.a_)


# Packages/ Libraries - 200k

import os

# print(os.getcwd())
# os.chdir("C:/Users/Lenovo/OneDrive/Documents/")
# print(os.getcwd())

# os.rmdir("test123")

# pid = os.getpid()
# print(pid)
# print(os.getppid())

# list_files = os.listdir("c:/")
# print(list_files)

# os.chmod('C:/Users/Lenovo/OneDrive/Documents',777)
# import shutil

# shutil.copyfile('dup.txt', 'C:/Users/Lenovo/OneDrive/Documents/dup.txt')



# import datetime

# time = datetime.datetime.now()
# print(time.strftime("%Y/%m/%d %H:%M:%S"))

# new = time-datetime.timedelta(hours=2)
# print(new)




# panda
import pandas as pd

d1 = {
   "names": ["Ajay", "Vijay", "Jay", "jaya", "Balu", "Charan"], 
   "ages": [21,23,24,25,25,26], 
   "cities": ['Bangalore', "Mumbai", "pune", "Hyd", "Chennai", "Cochin"], 
   "Orgs": ["TCS","HCL", "Cisco", "paloAlto", "Nutanix", "Extreme"]
}

# print(d1)

# df = pd.DataFrame(d1)
# print(df)

# df.to_csv("emp_data.csv", index=False)


# with open("emp_data.csv", "r") as fp:
#    # data = fp.read()
#    print(next(fp))
#    print(next(fp))
#    print(next(fp))
#    print(next(fp))
#    print(next(fp))
#    print(next(fp))
#    print(next(fp))
#    print(next(fp))
   
# df = pd.read_csv("emp_data.csv")
# print(df)
# read_data = df.to_dict(index=True)
# print(read_data)

# import csv

# with open("emp_data.csv") as fp:
#    data = fp.read()
#    print(type(data))

# Sys - command line arhumenets

# import sys # direct import

# from sys import argv, exit, args # specific/selective import

# print(argv)

# sys.exit()
# host/ip, user, pass

# ip = "192.168.2.34"
# user = "admin"

# ip = argv[1]
# username = argv[2]
# password = argv[3]

# print(ip, username, password)



# print("Hello")
# print("Hello")

# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# try:
#    denom = int(input("Enter the denominator\t"))
#    rem = 100/denom
#    print(rem)
#    print("Safe")
# except Exception as e:
   # print("Exception Found", e)
# try:
#    l1 = [1,2,3,4,5]
#    print(l1[20])
# except Exception as e:
#    print("Exception:",e)
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")


# modes - r,w,a
# with open("new_file.txt", "w") as fp:
#    fp.write("This is My Second line\n")
#    fp.write("This is My Third line\n")
#    fp.write("This is My Fourth line\n")

# with open("new_file.txt", "r") as fp:
#    data = fp.readlines()
# print(data)
# with open("new_file.txt", "a") as fp:
#    fp.write("This is My Fifth line")






