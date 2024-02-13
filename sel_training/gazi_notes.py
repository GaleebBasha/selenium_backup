# """
# 1. Dynamically Datatyped
# in c
# -----
# char a = 'P'

# in Py
# -----
# a = 12.23

# 2. Memory Management
# in c
# ----
# int a = 10
# Pointers

# in Py: Py has a deamon called Memory Manager
# ----    
# a = "hrllo"

# 3. Garbage Collector
# in c
# ----
# dev resp to clear the memory once the execution is done
# in py
# -----
# GC is also a deamon, that deallocates the mem as soon as execution

# 4. OOPs - 
# 5. OS independent
# 6. Interpret based Lang
# compiler: C,CPP,Java, Node, JS -- Programming
# test.java -> test.class -> OP
# interpreter: Python, Shell, Grovy, TCL.. --> Scripting
# python test.py -> OP

# 7. Easy to understand
# 8. Librarys/Packages - 200k
# """

# # indentations - 
# # comments - single and multi line

# # Data Types - int, float,bool, char ----- String, List, Dict, Tuple and Set

# # string - 
# a = '10'
# b = "10"
# c = '''heloo I  ambkasn k
# bjkjasndhkjd
# nbjkjnsf'''

# text = "Hello, Today Is Sunday"
# # indexing and slicing - []
# print(text[-1])

# # slicing
# print(text[::-1]) # rev a string using slicing

# """
# 1. Data Types
# 2. Conditional Statemenet - if,elif, else
# 3. Loops - For, While
# 4. Break and Continue
# 5. Functions
# 6. args and kwargs
# 7. OOPs
# 8. Class
# 9. Obj
# 10. Constructor
# 11. Self
# 12. INheritance
#     a. Single 
#     b. Multiple
#     c. Multi Level
#     d. Hybrid
# 13. Poly Morphsim
#     a. Overloding
#     b. Overriding
# 14. Abstraction
# 15. Data Encapsulation
# 16. Super

# 17. File Handlings
# 18. Exception Handling
# 19. Special Func - Zip, Map, Filter and reduce
# 20. Generators and Decorators
# """
# text = "Hello Today Is Sunday"
# ind = text.index("d")
# print(ind)

# occ = text.count('h')
# print(occ)


# new = text.replace("a", "e")
# print(new)


# caps = text.capitalize()
# print(caps)


# ret = text.split("abc") #  split ret a list
# print(ret)

# re = text.rstrip("Xyz")
# print(re)

# # text = "ABCDFHGDNS"
# res = text.isupper()
# print(res)

# # text = "ABcdafsfv"
# res = text.isalpha()
# print(res)

# res = text.endswith("dy")
# print(res)


# res = text.find('IS')
# print(res)

# age = 30
# name = "John"
# stmt = "HI I am {0} of {1} years".format(name, age)
# print(stmt)
# print("Hello I am {} years old".format(age))

# text.isdigit()

# res = text.rfind('a', 16,-1)
# res = text.find('a')

# print(res)

# res = text.zfill(30)
# print(res)


# # list - mutable - editable
# # l1 = [1,1.1,"1", True]
# l1 = [22,33,11,23,54,53,27]
# # index and slicing

# # ways of adding
# l1.append(121) # at the end 
# print(l1)

# #insert
# l1.insert(2, 100)
# print(l1)


# # extend
# l2 = [1,2,3,4]
# l1.extend(l2)
# print(l1)

# l1.pop()
# print(l1)

# l1.remove(121)
# print(l1)

# del l1[2]
# print(l1)


# l1.sort(reverse=True)
# print(l1)

# l1.reverse()
# print(l1)

# l3 = l1.copy()

# # tuple -- hetero - immutable
# t1 = (1,2,3,4)
# t2 = (11,22,33,44)
# t3 = t1+t2
# print(t3)

# t1 = (1,2,3,[1,2])
# t1[3].append(111)
# print(t1)

# import copy
# a = 10
# b = copy.copy(a)
# b = 20
# print(a)


# # dictionary - {} - kv assocn - unordered

# reg = {1:'Ajay', 2: 'balu', 3: 'Charlie', 4: "Danny"}

# # slicing and indexing are not allowed
# print(reg)

# print(reg[1])

# v = reg.get(3)
# print(v)

# reg.update({5: 'Emma', 6: "Farhan"})
# print(reg)

# reg[7] = "Gazi"
# print(reg)

# reg[2] = "Bimbra"
# print(reg)
# reg.update({5: 'Eagle'})
# print(reg)

# # reg.clear()
# # print(reg)


# k = reg.keys()
# print(k)

# v = reg.values()
# print(v)

# kv = reg.items()
# print(kv)

# reg.pop(4)
# print(reg)

# reg.setdefault(3, "Yonus") # if key not present the creates a nwe kv else do nothing
# print(reg)

# l1 = [1,2,3,4]
# v1 = [11,22,33,44]
# d2 = reg.fromkeys(l1, v1)
# print(d2)

# # Set - {} - only allows uniques - set is unodered

# # s1 = {1,2,3,1,2,3}
# s1 = {1,2,3}
# s2 = {3,4,5}
# print(s1)

# # l1 = [1,2,3,4,4,5,45,3,4]
# # # we need a unique list
# # s1 = set(l1)
# # l2 = list(s1)
# # print(l2)

# l1 = [1,2,3,4]
# l2 = [2, 3,4,5,6]
# res = list(set(l2).difference(set(l1)))
# print(res)

# s1.update({2,3,4})
# print(s1)



# ################################ Functions ############
# # block rules - if,elif,else, def, class, try, with, except, finally
# # 1. end of the first line of any block should have a colon, 2. next lines should follow proper indentation

# def say_hello(name):
#     print("Good Morning", name)

# say_hello("Arun")



# def filter_even(l1):
#     even_list = []
#     for i in l1:
#         if(i%2==0):
#             even_list.append(i)
#     return even_list
            
# res = filter_even([1,2,3,4,5,6])
# print(res)

# # args - tuple

# def test_me(*nine):
#     print(nine)

# test_me()


# # named args

# def employee_data(name="Rahul", age=28, city="NYC"):
#     print(name,age,city)

# # employee_data(org="Apple")
    
# def emp(**kwargs):
#     print(kwargs)

# emp(gender="Male")


# # OOPS
# class Test():
#     def test1(self):
#         print("I am test1")
#     def test2(self):
#         print("I am test2")

# obj = Test()
# obj.test1()


# # self, constructor... 

# class Calculator():
#     def __init__(self,a,b):
#         print("Im in INIT")
#         self.a = a
#         self.b = b
#     def add(self):
#         print("Sum",self.a+self.b)
#     def sub(self):
#         print("Sub",self.a-self.b)
#     def mul(self):
#         print("Mul",self.a*self.b)
#     def div(self):
#         print("Div",self.a/self.b)

# obj = Calculator(12,10)
# # obj.add()
# # obj.sub()
# # obj.mul()
# # obj.div()

# # inheritance - process of inhertitnig all the parent properties to child
# # single

# class Parent():
#     def assets(self):
#         print("10M$")
#     def loans(self):
#         print("500k$")

# class Child(Parent):
#     def degrees(self):
#         print("Masters")

# # obj = Child()
# # obj.assets()
# # obj.loans()

# # obj = Parent()


# # multiple - a child will have more than one parent
# class A():
#     def a(self):
#         print("Class A")

# class B():
#     def b(self):
#         print("Class B")

# class C(B,A):
#     def c(self):
#         print("Class C")

# obj = C()
# obj.b()


# # multi level
# class A():
#     def a(self):
#         print("Class A")

# class B(A):
#     def b(self):
#         print("Class B")

# class C(B):
#     def c(self):
#         print("Class C")

# obj = C()
# obj.a()



# # Hybrid - combo of any two inh types

# class A():
#     def a(self):
#         print("Class A")

# class B():
#     def b(self):
#         print("Class B")

# class C(B,A):
#     def c(self):
#         print("Class C")


# class D(C):
#     def d(self):
#         print("Class D")


# obj = D()
# obj.b()


# # polymorphism-having same name but diff properties
# """
# two types
# 1. Overloading
# 2. Overriding
# """

# class Parent():
#     def assets(self):
#         print("10M$")
#     def loans(self):
#         print("500k$")



# class Child(Parent):
#     def degrees(self):
#         print("Masters")
    
#     def assets(self,a):
#         print("Child Assets")

# obj = Child()
# # obj.assets()


# # +
# a = "10"
# b = 20
# print(a*b)


# # Exception Handling
# num = 100
# denom = int(input("Enter denom value:\t"))
# try:
#     rem = num/denom
#     print(rem)
# except Exception as e:
#     print("Exception Handled", e.with_traceback)

# print("Hello")
# print("Hello")
# print("Hello")



# Abstraction

# class A():
#     def some(self):
#         pass

# class B(A):
#     def some(self):
#         print("Business Logic")

# obj = B()

# obj.some()





# from abc import abstractclassmethod,ABC
# class A(ABC):
#     @abstractclassmethod
#     def mylogic(self):
#         pass

# class B(A):
#     def mylogic(self):
#         print("Buss Logic")
    
# obj = B()
# obj.mylogic()

# file handlings
# write, read and append
# write mode overwrites the older data
# we need to use append mode to retain the older data

# fp = open("demo.txt", "a") 
# # fp.write("\nThis is my fourth line")
# l1 = ["\nHello\n","Good Morning\n", "Nice Meeting you\n", "Good Bye\n"]
# fp.writelines(l1)
# fp.close()

# fp = open("demo.txt", "r")
# # for i in fp.readlines():
# #     print(i)

# print(fp.readlines())
# fp.close()




# with open("demo.txt", "r") as fp:
#     data = fp.readlines()
#     print(data)


# import io

# f = io.open("demo.txt", "r")
# data = f.read()
# print(data)
# f.close()


# write a infinte loop, that throws 4 options to the user
"""
1. Enter A to add a new entry
2. Enter V to view the file content
3. Enter D to remove an entry from file       
4. Enter Q to quit the infinite loop
"""
# while(1):
#     ip = input("""
# 1. Enter A to add a new entry
# 2. Enter V to view the file content
# 3. Enter D to remove an entry from file       
# 4. Enter Q to quit the infinite loop\n\t:""")
#     if(ip=="Q"):
#         break
#     elif(ip=="A"):
#         msg = input("Whats your message?\t:")
#         with open("demo123.txt", "a") as fp:
#             fp.write(msg+"\n")
#     elif(ip=="V"):
#         with open("demo123.txt", "r") as fp:
#             data=fp.read()
#             print(data)
#     elif(ip=="D"):
#         # msg = input("Which entry do you want to delete?\t:")
#         # new_data = []
#         # with open("demo123.txt", "r") as fp:
#         #     data=fp.readlines()
#         # for i in data:
#         #     if(msg in i):
#         #         continue
#         #     new_data.append(i)
#         # with open("demo123.txt", "w") as fp:
#         #     fp.writelines(new_data)
        
#         line_no = int(input("Enter the line number you want to delete?\t:"))
#         with open("demo123.txt", "r") as fp:
#             data=fp.readlines()
#         print(data)
#         del data[line_no-1]
#         with open("demo123.txt", "w") as fp:
#             fp.writelines(data)

# import os
# os.chdir("TEST123")
# os.remove("demo.txt")
# os.remove("TEST123")
# cwd = os.getcwd()
# print(cwd)

# os.rmdir("TEST123")

# cwd = os.getcwd()
# print(cwd)
# f = io.open("demo.txt", "w")
# f.write("Hello")
# f.close()


# os.system("rm -rf TEST123")


#  Pckages/Librarues - 200k - 

# command Line Args

# import sys # direct import

# from sys import argv,exit

# argv = argv
# while(True):
#     print("hello")
# if(argv[1].isdigit() or argv[1].isnumeric()):
#     num = float(argv[1])
# else:
#     print("Wrong Input")
#     sys.exit(0)
# try:
#     num = float(argv[1])
# except Exception:
#     print("Wrong Input", Exception.with_traceback)
#     sys.exit(1)
    


# if(num%15==0):
#     print("Accepted")
# else:
#     print("Not Accepted")

# elements = argv[1:]
# print(elements)
# int_list = [float(i) for i in elements]
# even_list = [i for i in int_list if(i%5==0)]
# print(even_list)

# comprehesnsion
# int_list = []
# for i in elements:
#     int_list.append(int(i))
# print(int_list)

# int_list = [float(i) for i in elements]
# print(int_list)

# l1 = [12,23,45,67,89,54]

# l2 = [j for i in l1 for j in range(1,i+1) if i%j==0]
# print(l2)


# l2 = tuple(i if i%2==0 else i*i for i in l1)
# print(l2)



# reg = {15:'Ajay', 21: 'balu', 31: 'Charlie', 24: "Danny"}

# res = [(i,reg[i]) for i in reg if(i>20)]
# print(res)
# for i,j in reg.items():
#     if(i>20):
#         print(i,j)




# from os import getpid
# res = os.system("dir ")
# print("op is",res)


# # map,filter,reduce and zip
# def filter_caps(s1):
#     if(s1.isupper()):
#         return True
#     return False

# res = set(filter(filter_caps, "Hello World"))
# print(res)


# from functools import reduce

# def do_sum(*args):
#     print(len(args), args)
#     return args[0]+args[1]

# res = reduce(do_sum,['a','b','c'])
# print(res)


# # can you create a dict with two list

# l1 = [1,2,3,4,5]
# l2 = [11,22,33]
# l3 = [111,222,333,444,555]
# #op = {1:11}
# op = {}
# for i,j,k in zip(l1,l2,l3):
    
#     op[i]={j:k}
# print(op)

# # how do we comine two dicts

# d1 = {1:"Ajay", 2:"Binu"}
# d2 = {3:"Charmi", 4: "Dolly"}
# # print(d1+d2)
# # d1.update(d2)
# # print(d1)

# d3 = {}
# for i,j in zip(d1,d2):
#     d3[i] = d1[i]
#     d3[j] = d2[j]
# print(d3)

# # decorators
# def decor(func):
#     def inner(*args, **kwargs):
#         print("First")
#         func(*args, **kwargs)
#         print("Last")
#     return inner

# def decor1(func):
#     def inner(*args, **kwargs):
#         print("First1")
#         func(*args, **kwargs)
#         print("Last1")
#     return inner

# def decor2(func):
#     def inner(*args, **kwargs):
#         print("First2")
#         func(*args, **kwargs)
#         print("Last2")
#     return inner

# @decor
# @decor1
# @decor2
# def do_some():
#     print("This is the main func")

# do_some()



# recursion

# def fact(n):
#     res = 1
#     while(True):
#         if(n>=1):
#             res = res*fact(n-1)
#             # n=n-1
#         else:
#             break
#     return res


# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     if(n<0):
#         return 0
#     return n*fact(n-1)

# print(fact(1))        


# request

# import requests
# import json
# headers = {"Accept": "JSON", "Content-type": "text"}
# payload = {
#     "name": "Raj",
#     "job": "QA"
# }
# url="https://reqres.in/api/users/create"
# res = requests.post(url=url,  verify=False, json=payload)
# print(res)
# url="https://reqres.in/api/users"
# res = requests.get(url=url, verify=False, headers=headers)
# dict_data = json.loads(res.content)
# print(dict_data)


# res = requests.get(url="https://dummy.restapiexample.com/api/v1/employees", headers=headers, verify=False)
# resp = res.content
# print(type(resp))
# dict_data = json.loads(resp)
# print(type(dict_data))
# url="https://reqres.in/api/users/2"

# res = requests.delete(url=url, headers=headers, verify=False)
# print(res.cookies)


# PyTest
# import pytest
# def test_sum():
#     a = 10
#     b = 20
#     assert a+b==30

# def test_sub():
#     a = 10
#     b = 20
#     assert a-b==-10

# @pytest.mark.failed    
# def test_mul():
#     a = 10
#     b = 20
#     assert a*b==20
    
# def test_div():
#     a = 10
#     b = 20
#     assert b/a==2

# @pytest.mark.failed    
# def test_conf(input_value, input_string):
#     print(input_string)
#     assert input_value==39

import pytest

@pytest.mark.parametrize(('a', 'b'),[[1, 1],[2,3],[4,5]])
def test_1(a,b):
    # res = test_somcond(a,b)
    assert a*b>0

"""
pip install pytest-html
python -m pytest .\gazi_notes.py --html=report.html 
pip install pytest-html-reporter
python -m pytest .\gazi_notes.py --html-report=report.html    
"""

# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )

# print(mydb)


# curser = mydb.cursor()

# curser.execute("select * from table;")
# res = curser.fetchall()
# curser.execute("alter table t1 add column Ages int;")
# mydb.commit()


# import threading
 
# import time
# def print_cube(num):
#     time.sleep(10)
#     print("Cube: {}" .format(num * num * num))
 
 
# def print_square(num):
#     time.sleep(5)
#     print("Square: {}" .format(num * num))
 
 
# if __name__ =="__main__":
#     t1 = threading.Thread(target=print_square, args=(10,))
#     t2 = threading.Thread(target=print_cube, args=(10,))
 
#     t1.start()
#     t2.start()
 
#     t1.join()
#     # t2.join()
 
#     print("Done!")


from multiprocessing import Process


def print_func(continent='Asia'):
    print('The name of continent is : ', continent)
# print(__name__)
# import os
# import test as t
# os.system("python test.py")
# print(t.__name__)
# print("Out of the Mul Processing")

# if __name__ == "__main__":  # confirms that the code is under main function
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     proc = Process(target=print_func)  # instantiating without any argument
#     procs.append(proc)
#     proc.start()

#     # instantiating process with arguments
#     for name in names:
#         # print(name)
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()

#     # complete the processes
#     for proc in procs:
#         proc.join()


# def testme():
#     print("hello")

# testme()


import pandas as pd

# d1 = {"names":["Ajay","vijay","john","rina","divya"], "ages":[21,23,31,25,33], "city":["Moscow","Delhi","Tokyo", "Mumbai", "hyderabad"]}

# df = pd.DataFrame(d1)
# # print(df)

# df.to_csv("student_data.csv")
# # df.to_xml("test.xml")


# df = pd.read_csv("student_data.csv")
# dict = df.to_dict()
# # del dict['Unnamed']
# print(dict)
# dict.pop("Unnamed: 0")
# print(dict)



# static and class method
# class Student:
 
#     # create a variable
#     name = "Geeksforgeeks"
 
#     # create a function
#     def print_name(obj):
#         print("The name is : ", obj.name)
    
#     def test_me(self):
#         print("testme", self.name)
 
# Student.print_name = classmethod(Student.print_name) # declaring
# Student.print_name()


# obj = Student() # 
# obj.test_me()




class Calculator:
    name = "India"
    def addNumbers(x, y):
        return x + y

# create addNumbers static method
Calculator.addNumbers = staticmethod(Calculator.addNumbers)

print('Product:', Calculator.addNumbers(15, 110))

assert {"name":"ram", "age":21} == {"age":21, "name":"ram"}








