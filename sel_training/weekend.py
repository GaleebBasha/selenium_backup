"""
1. Dynamically Datatyped
in c
int a = 10
in java
int x = 10 

in python
a = 10

2. Memory Manager
in c - pointers -stores the mem of another vars
int a = 10
int *p = &a    

in java/py - memory manager

3. Garbage Collector

4. Interpreter

compiler - C,CPP,JAVA,JS,Node JS - Programming
interpreter - Py, Sh, TCL, Grrovy, powershell - Scripting
python file.py, sh test.sh

5. OOPs - modularity, maintain and understand
6. Packages/Library - 200k, java - 30

7. Py is PF independent 
8. Simple
9. Open sourse
10. Pluggable
11. Robust

pip install selenium

- Venv - docker - k8s
"""

# indentation and comments - {} - 

# Data Types - int, float,char, bool ------ String, List, Tuple, Dict and Sets
# String

a = 10
a = "fdsf6fdv6@#$z7"
a = 'dfddfgfssdbffdds'
a = '''I am fro Infadn,
ndkncbjkd
kznckj
njakj'''

# text = "Today Is Sunday"
# # index and slicing
# print(text[-1])

# # slicing
# print(text[2:6]) # exclude the end index
# print(text[:8])
# print(text[:-1]) # reverse a string using slicing ops

# # manipulation - string
# ind = text.index(" Sun")
# print(ind)


# occ = text.count("days")
# print(occ)


# res = text.replace("ay", "AY")
# print(res)

# op = text.split("Is") # returns list op 
# print(op)
# text = "today Is Sunday"
# res = text.lstrip(" ")  # ends
# print(res)

# up = text.capitalize()
# print(up)

# name = "234567543"
# age = 33
# print("I am {} of {}".format(name,age))

# res = name.islower()
# print(res)


# res = name.isdigit()
# print(res)

# name = "I am from India"
# res = name.endswith("India")
# print(res)



# # List -heterogenous - mutable - []
# # l1 = [1,"1", 1.1, [1,2,3]]
# l1 = [23,21,26,54,34,5]
# # index and slicing
# print(l1[-2])
# print(l1[:-1])



# org = "TCS"
# print(org)
# new_ord = org.replace("C", "S")
# print(new_ord, org)

# l1.reverse()
# print(l1)

# l2 = l1.copy()
# print(l2)

# ind = l1.index(5)
# print(ind)

# # l1.count()

# l1.append(100) # always at the end
# print(l1)

# # specific
# l1.insert(len(l1), 200)
# print(l1)

# l2 = [1,2,3,4]
# # extend - merge
# l2.extend(l2)
# print(l2)

# l1.pop()
# print(l1)

# l1.remove(54)
# print(l1)

# # keyword
# del l1[0]
# print(l1)
# # l1.clear()
# # print(l1)

# # l1 = [23,45,33,"Name"]
# l1.sort(reverse=True)
# print(l1)
# text = "i am from India"

# # convert a string to a list - split()
# l3 = list(text)
# print(l3)

# # list to a string
# l3 = ['a','b','c','d']
# s2 = ",".join(l3)
# print(s2)

# # tuple - heterogenous - immutable - no manipulations
# t1 = (1,"1",1.1, True)
# t2 = (1,2,3,4)
# t3=t1+t2
# print(t3[2:20])

# # Dictionary - KV pair - unordered - no index/slicing - mutable - {}
# d1 = {"1":"Ajay", "2": "@#@", "3": 'Charlie', "4": "Danny"}
# print(d1["3"])


# d1[6] = "Emma"
# print(d1)

# d1.update({"7":"Farhan", "8": "George"})

# print(d1)

# d1.pop("4")
# print(d1)

# d1.popitem()
# print(d1)


# # from collections import OrderedDict

# k = d1.items() # list of tuples
# print(k)


# d1.clear()
# print(d1)


# d1.setdefault("1","Zoya")
# print(d1)

# l1=[1,2,3,4]
# val = [11,22,33,44]
# d2 = d1.fromkeys(l1, val)
# print(d2)


# sets - merely - unordered - {} - mutable

# s1 = {1,1,1,1,2,2,2,2,3,3,3}
# print(s1)

# l1 = [1,2,3,1,2,3,4]
# # get a unique list
# s = list(set(l1))
# print(s)


# s3 = {3,4}
# s2 = {3,4,5,6}

# comm = s2.issuperset(s3)
# print(comm)

# str, list, dict
# control stamement / if,elif, else / for and while / functions


# blocks - if,elif,else, class,def,try,except,finally,with,for, while
# first line of the block should end with :, the following lines should have proper indents

# age = 21

# if(age>18):
#     print("Eligible")
# else:
#     print("Need to wait")
    
# marks = 80
# if(marks>90 and marks<100):
#     print("Grade A")
# if(70<marks<90):
#     print("Grade B")
# elif(marks>50 ):
#     print("Grade C")
# else:
#     print("Grade D")

# # nested if
# country = "India"
# state = "Andhra"
# city = "Guntur"
# if(country=="India"):
#     print("Welcome to India")
#     if(state=="Andhra"):
#         print("Welcome to Andhra")
#         if(city=="Vizag"):
#             print("Welcome to the city of Destiny")
#         else:
#             print("Not in Vizag")
#     else:
#         print("Not In Andhra")        
# else:
#     print("You are not in India")

# # Loops - repeated action for a finite no of time - For and While
# # s1 = "Today Is Monday"
# s1 = {1,2,3,4}
# # str, list, tuple, dict, set
# # bool, int, float
# for i in s1:
#     print(i,"\n")
#     # print("\n")
    

# # s1 = [1,2,3,4,5,6,7,8,9,10,11]
# # range
# l1 = tuple(range(0,101,7))
# print(l1)
# # for i in l1:
# #     if(i%2==0):
# #         print(i,end=" ")

# s1 = "Tod1ay I2s M3onday"
# for i in s1:
#     if(i.isdigit()):
#         print(i)

# d1 = {"john":54, "benny": 45, "charlie":55, "danny":48}
# # max = 0
# # oldest = ""
# # for i,j in d1.items():
# #     if(j>max):
# #         max = j
# #         oldest = i
    
# # print(oldest,max)

# min = 1000000
# youngest = ""
# for i,j in d1.items():
#     if(j<min):
#         min = j
#         youngest = i
# print(youngest,min)



# l1 = [22,33,44,12,23,64,34]

# max = 0
# for i in l1:
#     if(i>max):
#         max = i
# print(max)

# # while
# l1 = [1,2,3,4]
# # for i in l1:
# #     print(i)

# count = 0
# while(count<len(l1)):
#     print(l1[count])
#     count+=1

# d1 = {"john":54, "benny": 45, "charlie":55, "danny":48}
# count = 0
# keys = list(d1.keys())
# while(count < len(d1)):
#     print(keys[count], d1[keys[count]])
#     count+=1


# while(0):
#     print("hello")


# # break and continue
# l1 = list(range(1,100))
# for i in l1:
#     if(i==20):
#         # break # termination of loop
#         continue # skip that cond
#     print(i)

# check if a number is prime
# number = 13
# factors = 0
# for i in range(1,number+1):
#     if(number%i==0):
#         factors+=1
# if(factors==2):
#     print("its a prime number")
# else:
#     print("not a prime number")

#  print all prime number under 100

# l1 = [2,3,4,5,6,7,5,11,22,33,44] get a new list of even numbers from l1
# get first 10 multiples of 17 as list 
# op = [17,34,51,....,170]

# functions - def

# def say_hi(name):
#     print("Hello",name)
    
# say_hi("John")
# say_hi("Mike")
# say_hi("Tina")
# say_hi("Yonus")
# say_hi("Arul")

# cap_list = []

# def cap_filter(s1):
#     for i in s1:
#         if(i.isupper()):
#             # print("{} is upper".format(i))
#             cap_list.append(i)
#     return cap_list
# res = cap_filter("Today Is a Good Day")
# print(res)



# def test_num(n):
#     if(n%9==0):
#         pass
#         # return 1223
#     else:
#         pass
#         # return 2345

# print(test_num(18))


# def filter_older(d1):
#     age = 0
#     # name = ""
#     for j in d1:
#         if(d1[j]>age):
#             age=d1[j]
#             # name=i
#     return age

# resp = filter_older({'ajay':32,'vijay':23, 'mark':48, 'reena':31})
# print(resp)



# # *args and **kwargs

# def test(*args):
#     print(args, type(args))

# test(1,2,3,4,5)


# # named args
# # def em?
# # emp_data(city="NYC")


# def emp_data(**kwargs):
#     print(kwargs)

# emp_data(city="NYC", age=22, gen="M")

# OOPs - Object Oriented
"""
class
obj
self
init-constructor
inheritance
types of inh
polymorph    
"""
# class Test():
#     def say_hi(self, name):
#         print("hello",name)
    
#     def say_bye(self,name):
#         print("Good Bye",name)
#     def do_add(self,a,b):
#         print(a+b)

# obj = Test()
# obj.say_hi("John")
# obj.say_bye("john")
# obj.do_add(12,23)

# obj1 = Test()
# obj1.say_hi("sheela")
# obj1.say_bye("sheela")
# obj1.do_add(44,33)

# class Calculator():
#     def add(self,a,b):
#         print("Add", a+b)
#         self.a = a
#         self.b=b
    
#     def sub(self):
#         print("Sub", self.a-self.b)

#     def mul(self):
#         print("Mul", self.a*self.b)

#     def div(self):
#         print("Div", self.a/self.b)

# obj = Calculator()
# obj.add(12,10)
# obj.sub()
# obj.mul()
# obj.div()

# class Calculator():
#     def __init__(self,a,b):
#         print("This is a constructor")
#         self.a = a
#         self.b = b
        
#     def add(self):
#         print("Add", self.a+self.b)

    
#     def sub(self):
#         print("Sub", self.a-self.b)

#     def mul(self):
#         print("Mul", self.a*self.b)

#     def div(self):
#         print("Div", self.a/self.b)

# obj = Calculator(12,10)
# obj.add()
# obj.sub()
# obj.mul()
# obj.div()


# Inheritance - aquiring one class prop by another - single, multple, multi-level and hybrid inheritance

# class Parent():
#     def assets(self):
#         self.money = 100
#         print(self.money)
#     def loans(self):
#         print("1M$")

# class Child(Parent):
#     def degrees(self):
#         print("Masters")

# obj = Child()
# obj.assets()


#multiple inh

# class A():
#     def a(self):
#         print("Class A")

# class B():
#     def b(self):
#         print("Class B")

# class C(A,B):
#     def c(self):
#         print("Class C")

# # obj = B()
# # obj.

# # multi level inh

# class A():
#     def a(self):
#         print("Class A")

# class B(A):
#     def b(self):
#         print("Class B")

# class C(B):
#     def c(self):
#         print("Class C")

# class D(C):
#     def d(self):
#         print("Class D")
# obj = D()
# obj.c()

# obj1 = C()
# obj1.a()


# hybrid - combination of any two inheritances - [multiple+multi level or single+multiple or single+multilevel]
# class A():
#     def a(self):
#         print("Class A")

# class B():
#     def b(self):
#         print("Class B")
    
# class C(A,B):# multiple inh 
#     def c(self):
#         print("Class C")

# class D(C): # mul level
#     def d(self):
#         print("Class D")

# obj = D()
# obj.a()


# Exception Handling - try and except


# try:
#     numb = int(input("Enter a denominator value\t:"))
#     rem = 100//numb
#     # 100/10=10.0 (float)
#     # 100//10=10 (int)
#     print(rem)
#     l1 = [1,2,3,4]
#     print(l1[2])

# except Exception as exe:
#     print("Exception Occurred\t:",exe)

# print("hello")




# file handling - RWA

# w mode - it will crate a new file if no file is existed before, else it will overwrite
# fp = open("C:/Users/Lenovo/OneDrive/Documents/xyz.txt", "a")
# l1 = ["abc\n","xyz\n","pqr\n"]
# fp.writelines(l1)
# fp.write("This is My Fourth line\n")
# fp.close()
# fp = open("C:/Users/Lenovo/OneDrive/Documents/xyz.txt", "r")
# text = fp.read()
# print(text)
# text = fp.readlines()
# print(text)
# fp.close()


# context manager - with keyword

# with  open("C:/Users/Lenovo/OneDrive/Documents/xyz.txt", "r") as fp:
#     data = fp.read()
#     print(data)

# Packages or Libraries

# os - operating system

# import os # direct impoprt - imports all funcs od OS pkg

from os import getppid # specific/selective import

# os.rmdir("pqr")
# os.chdir("C:/Users/Lenovo/OneDrive/")
# res = os.getcwd()
# id = os.getpid()
# print(id)
# s_id = getppid()
# print(s_id)


# Selenium
# website - 
# python seleniuim code -- chrome driver -- chrome browser


from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

from selenium.webdriver.common.action_chains import ActionChains 
import time

driver = webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.get("https://www.flipkart.com/")
# driver.get('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India')
driver.implicitly_wait(20)

driver.maximize_window()

# driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")

# driver.find_element(By.NAME, "password").send_keys("admin123")


# driver.find_element(By.XPATH, '//button[@type="submit"]').click()

# driver.execute_script("window.scrollTo(0, 300)")
# driver.find_element(By.XPATH, '//input[@id="male"]').click()

# driver.find_element(By.XPATH, '//label[text()="Tuesday"]').click()
# driver.find_element(By.XPATH, '//label[text()="Thursday"]').click()
# driver.find_element(By.XPATH, '//label[text()="Saturday"]').click()

# driver.switch_to.frame('frame-one796456169')

# driver.execute_script("window.scrollTo(0, 500)")
# slct = Select(driver.find_element(By.ID, 'RESULT_RadioButton-3'))


# slct.select_by_index(2)
# time.sleep(2)
# slct.select_by_value('Radio-0')
# time.sleep(3)
# slct.select_by_visible_text('Manager')


# act = ActionChains(driver)

# act.double_click(driver.find_element(By.XPATH,'//button[text()="Copy Text"]')).perform()

# act.context_click(driver.find_element(By.XPATH,'//button[text()="Copy Text"]')).perform()
# time.sleep(2)
# act.move_to_element(driver.find_element(By.XPATH, '//p[text()="Drag me to my target"]'))

# src = driver.find_element(By.XPATH, '//p[text()="Drag me to my target"]')
# dest = driver.find_element(By.XPATH, '//p[text()="Drop here"]')
# act.click_and_hold(src).perform()

# act.drag_and_drop(src,dest).perform()

# # act.click_and_hold(src).perform()

# act.release().perform()
# time.sleep(2)
# act.move_to_element(driver.find_element(By.XPATH, '//h2[text()="Pagination Table"]')).perform()






# act.move_to_element(driver.find_element(By.XPATH, '//span[text()="Fashion"]')).perform()

# driver.find_element(By.XPATH, '//a[text()="Winter"]').click()



# (//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr[9]/td[3]

# row_count = len(driver.find_elements(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr'))
# col_count = len(driver.find_elements(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr[3]/td'))

# dict_data = {}
# import pandas
# for row in range(1,row_count+1):
#     row_data = []
#     for col in range(1, col_count+1):
#         cell_data = driver.find_element(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr[{}]/td[{}]'.format(row, col)).text
#         row_data.append(cell_data)
#     dict_data[row_data[0]] = row_data[1:]

# states_list = []
# adm_list = []
# leg_list = []
# jud_list = []
# estd_list = []
# form_cap = []
# dict_data = {"states": states_list, "Adm-cap": adm_list, "Leg_cap": leg_list, "Jud_cap": jud_list, "estd": estd_list, "form_cap":form_cap}
# for row in range(1, row_count+1):
#     row_data = []
#     for col in range(1, col_count+1):
#         cell_data = driver.find_element(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr[{}]/td[{}]'.format(row, col)).text
#     for i in row_data:
#         adm_list.append(row_data[0])
#         adm_list.append(row_data[1])
#         leg_list.append(row_data[2])
#         jud_list.append(row_data[3])
#         estd_list.append(row_data[4])
#         form_cap.append(row_data[5])

# # print(dict_data)
# dict_data['states']=states_list
# dict_data['Leg_cap'] = leg_list
# dict_data['Adm-cap'] = adm_list
# dict_data['Jud_cap'] = jud_list
# dict_data['estd'] = estd_list
# dict_data['form_cap'] = form_cap
# df = pandas.DataFrame(dict_data)
# print(df)

# df.to_excel("data_states")
# headers = driver.find_elements(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/thead/tr/th')
# print(headers)
# for i in headers:
#     print(i.text)

# time.sleep(5)

# driver.quit()


# import pandas
# d = {"names": ['ajay', 'vijay', 'raj', 'tony', 'farha'], "ages": [21,12,34,43,23], "cities": ['Delhi', "London", "NYC", "Bombay", "Karachi"]}
# df = pandas.DataFrame(d)
# df.to_excel("sample.xlsx", index=False)
# print(d)


# driver.execute_script("window.open('https://gmail.com');")
# time.sleep(2)
# driver.execute_script("window.open('https://facebook.com');")
# time.sleep(2)
# driver.execute_script("window.open('https://twitter.com');")
# time.sleep(2)
# driver.execute_script("window.open('https://instagram.com');")

# time.sleep(5)

# handles = driver.window_handles

# # print(handles)

# for each in handles:
#     driver.switch_to.window(each)
#     print(driver.title)
#     # if(driver.title == "Gmail"):
#     #     print(driver.title)
#     #     break
# time.sleep(10)




from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.find_element(By.NAME, 'username').send_keys("Admin")
driver.find_element(By.NAME, 'password').send_keys("admin123")
# time.sleep(10)

# fluent wait
# While using Fluent Wait, it is possible to set a default polling period as needed. 
# The user can configure the wait to ignore any exceptions during the polling period.


WebDriverWait(driver, 10, poll_frequency=5, ignored_exceptions=['TimeoutException','NoSuchElementException']).until(EC.presence_of_element_located((By.XPATH, '//button[@type="submi"]')))
from datetime import datetime
print(datetime.now())
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
# time.sleep(10)

# driver.find_element(By.NAME, 'password').send_keys("admin123")














 