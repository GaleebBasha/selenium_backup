"""
1. Python is Dynamically datatypd
in c
----
int a = 10    

in py
-----
a = 10
s1 = "Hello"

2. Memory Manager
in c
-----
its dev resp to create the mem for the var
int a = 10    
int *p = &a

in py/java
----------
a = 10, Memory Manager    

3. Garbage Collector
dev has to free the mem, otherwise the dead vars still occupy the mem blocks
GC - he takes the resp to cleanup the mem blocks at the end

4. OOPs
5. Interpreter

interpretr-Py,shell,groovy, tcl - Scripting
python abc.py
sh abc.sh

compiler - C,CPP,Java,node, JS - Programming Lang
main.java -> compile -> main.Class -> execute -> op

6. Platform independent - OS
7. py has a huge colx of packages/libraries - 200k
 - web dev django,flask
  - interract db
  - datascience - AI/ML/NN/DL
8. Simple
9. open source
10. integrated with robot framework RPA  


Topics Coverage
1. Features
2. Data Types
3. Condition Statements - if,else and elig
4. Loops - for/while
5. Break and continue
6. Functions
7. args and kwargs
8. OOPs
  a. Inheritance
  b. Abstraction
  c. Poly
  d. Data Encapsulation
9. Exception Handling
10. File handling


Structure of a website
11. Xpaths
12. Check box/radio
13. Dropdowns - 
14. Mouse action
   a. double click
   b. drag and drop
   c. right click
   d. mouse hover
15. Tables
16. Frames
17. Alers/popups
18. Windows
19. A POM 
"""
# {}, indents
# comments

# data types 
# priittive - int, bool, float
# str, list, dict, tuple and set

# String - ',","""

# s1 = "Hello"

# s2 = 'Hello'

# s3 = '''hello how are you all

# ots been a long seen you'''
# text = "tod12ay Is Sunday"

# # indexing - 0 - []
# print(text[-3])

# # slicing - capture a substring

# print(text[2:-1]) # exclusing end index

# print(text[::-1]) # reverse a string using slicing

# # on list, tuple and set 

# # Manipulations
# ind = text.index("Is")
# print(ind)

# occ = text.count("Z")
# print(occ)

# res = text.replace("Is1","IZ")
# print(res)


# res = text.capitalize()
# print(res)

# res=text.split("ddgf") # str to list
# print(res)

# res=text.lstrip(" ")
# print(res)

# text = "Hellowwe"
# res = text.isalnum()
# print(res)

# res=text.isalpha()
# print(res)
# text = "6454353443675a654"
# res=text.isdigit()
# print(res)

# # startswith and endswith
# text = "Hello How are you doing"
# res=text.startswith("Hello Howare")
# print(res)

# res=text.endswith("ing")
# print(res)

# print(len(text))


# name = "Raj"
# age = "25"

# print("I am {1} of {0} yrs old".format(name,age))

# l1=["a","b","c","d"]
# # join can convert a list to a string
# s1 = "=".join(l1)
# print(s1)

# s2 = "Hello wordl"
# # ['H','e','l','l','o'.......]
# l2 = list(s2)
# print(l2)

# s3 = s1+s2
# print(s3)


# s1 = "Hello,word"
# s2 = s1.replace(","," ")
# print(s2)


# # list - heterogenous - having diff data types - []

# l1 = [1,"1",1.1,True,[12,3,4]]
# print(l1)

l1 = [22,33,11,23,13,45]
# # index and slicing

# #manipulation funcs

# l1.append(100) # always keeps new rec at the end
# print(l1)

# l1.insert(3,123) # index can be selected
# print(l1)

# # extend to merge two lists
# l2 = [1,2,3,4]
# l2.extend(l1)
# # print(l2)

# # delete entry from a list
# # pop
# l1.pop(0) # end index
# print(l1)

# l1.remove(13) # by value
# print(l1)
# l1.sort(reverse=True)
# print(l1)

# l1.reverse()
# print(l1[::-1])
# ind = l1.count(33)
# print(ind)

# l3 = l1.copy()
# print(l3)
# l1.clear()
# print(l1)


# dictionary - k,v - {}

d1 = {1:"ajay", 2: "vijay", 3:"jay"}

# no index and slicing with dict

# v = d1.get(3)
# print(v)

# print(d1[3])

# d1.update({2: 'jay', 3:"vijay"})
# print(d1)

# d1[2]="jay"
# d1[3]="vijay"
# d1[4] = "Sanjay"

# d1.pop(2)
# d1.clear()
# d2 = d1.copy()
# k = d1.items() # for loop
# print(k)


# d1.setdefault(1,"DJ")
# if the key is not present then it creates a new kv pair else does nothing
# print(d1)

# l1 = [1,2,3,4]
# val = [11,22,33,44]
# d2 = d1.fromkeys(l1,val)
# print(d2)


# d1.popitem()
# print(d1)


# tuple - () - paranthesis - looks and acts almost like a list - tuple is immutable

# t1 = (1,"1",1.11,False)
# print(t1[1:3])
# t2 = (1,2,3,4)
# t3 = t1+t2
# print(t3)


# Set - {} - only unique elements
# s1 = {1,1,1,2,2,2,3,3,3}
# print(s1)

# l1 = [1,1,1,2,2,2,3,3,3]
# s2 = list(set(l1))
# print(s2)


# condition statements - if,else,elif
# block - if,else,elif,for,while,def,class,with, try,except
# 1. the first line of the block should end with a colon :
# 2. the further line should have proper indents


# marks = int(input("enter marks\t:"))

# if(age>18):
#   print("Eligible for voting")

# else:
#   print("Need to wait")

# if(marks>85):
#   print("Grade A")
  
# if(marks>75):
#   print("Grde B")
# elif(marks>60):
#   print("Grade C")
# elif(marks>40):
#   print("Grade D")
# else:
#   print("Fail")
  
  

#nested if
# country = "India"
# state = "Andhra"
# city = "Vizag"

# if(country=="India"):
#   print("Welcome India")
#   if(state=="Andhra"):
#     print("Welcome Andhra")
#     if(city=="Guntur"):
#       print("Welcome Vizag")
#     else:
#       print("Not in Vizag")
#   else:
#     print("not in AP")
# else:
#   print("Not in India")


# loops - for - while

# s1 = "H1el2lo W3or4ld"


# for i in s1:
#   if(i.isdigit()):
#     print(i,end="-")


# l1 = (1,2,3,4,5,6,7,8,9,10,11,12)
# l1 = range(1,51)
# for i in l1:
#   if(i%3==0):
#     print(i,end=",")

# l1 = range(0,51,15)
# print(list(l1))
# d = {"ajay":45, "vijay": 54, "jay":38, "jaya":55, "lattha":50}

# for i,j in d.items():
#   # print(i, d[i])
#   if(j>=45 and "jay" in i):
#     print(i,j)


# s1 = "GJHJ ghjhkjnbHJJHKJ JHKJK hjjh!kj$mad@sdsbnm322nb,n,m32133bmn,m32jjk2m32"
# #op = {"upper": [G,J,H,J,....], "lower":[g,h,j,h,....], "spl": [","," "], "digit": [2,1,3,3,2,3,2]}
# u_c = []
# l_c = []
# spl_c = []
# dig_l = []

# for i in s1:
#   if(i.isupper()):
#     u_c.append(i)
#   elif(i.islower()):
#     l_c.append(i)
#   elif(i.isdigit()):
#     dig_l.append(i)
#   else:
#     spl_c.append(i)
  
# # print(u_c,l_c,spl_c, dig_l)
# op = {"upper": u_c, "lower": l_c, "digit": dig_l, "spl": spl_c}
# print(op)


# break and continue
# l1 = range(1,30)
# for i in l1:
#   if(i==5):
#     # break # loop will be terminated
#     continue # skips the condition
#   print(i,end=",")


# while
s1 = "hello world"
# for i in s1:
#   print(i)

# count = 0
# while(count<len(s1)):
#   print(s1[count])
#   count+=1

# d = {"ajay":45, "vijay": 54, "jay":38, "jaya":55, "lattha":50}

# count = 0
# keys = list(d.keys()) # keys is a list so that we can iterate
# while(count<len(d)):
#   print(keys[count],d[keys[count]])
#   count+=1


# fuctions - def

# def sayhi():
#   print("Hello, Good Morning")

# sayhi()
# sayhi()
# sayhi()
# sayhi()
# sayhi()

# def sayhi(name, age):
#   print("Good Morning", name, age)

# sayhi("ajay",23)


# def ret_sqr(n):
#   if(n%2==0):
#     res = n*n
#   else:
#     res = n*n*n
#   return res,n

# res = ret_sqr(30)
# print(res)



# def filter_caps(s1):
#   caps = []
#   for i in s1:
#     if(i.islower()):
#       caps.append(i)
#   return caps

# res = filter_caps("Hello Good Morning")
# print(res)



# def filter_by_factor(l1,n1):
#   factors = []
#   for i in l1:
#     if(i%n1==0):
#       factors.append(i)
#   return factors

# res = filter_by_factor([12,22,33,13,15,17,23,25,27], 3)
# print(res)


# res1 = filter_by_factor([1,2,3,4,5,6,7], 2)
# print(res1)



# def ret_eldest(d1):
#   max_age = 0
#   eldest = ""
#   for i,j in d1.items():
#     if(j>max_age):
#       max_age = j
#       eldest = i
#   return eldest, max_age

# res = ret_eldest({"ajay":23, "priya":45, "john":32, "mohan":21})
# print(res)



# args - as a tuple
# def test(*args):
#   print(args)

# test(1,1,2)
# test(1,2)
# test(1,1,2,3,4)
# test()


# named  args
#kwargs - dictionary
# def test(name="john",age=22, org="TCS"):
# def test(**kwargs):
#   print(kwargs)

# test(name="Robert",age=30, org="HCL")
# test(city="Hyd")



# OOPs -
"""
1. Class
2. Obj
3. Self
4. Init
5. Inheritance and types  
"""


# class Test():
#   def sayhi(self):
#     print("hello")
  
  # def saybye(self):
  #   print("Good Bye")

# object - name can be user defined

# obj = Test()
# obj.sayhi()
# obj.saybye()

# obj1 = Test()
# obj1.sayhi()
# obj1.saybye()



# calculator class

# class Calculator():
#   def __init__(self,a,b):
#     self.a = a
#     self.b = b  
#     print("Im a constructor")  
#   def add(self):
#     print("Adding:",self.a+self.b)
#   def sub(self):
#     print("Sub:",self.a-self.b)
#   def mul(self):
#     print("Mul:",self.a*self.b)
#   def div(self):
#     print("Div",self.a/self.b)

# obj = Calculator(12,2)
# obj.add()
# obj.sub()
# obj.mul()
# obj.div()

# Inheritance - min two classes 

# SINGLE INHERITANCE

# class Parent():
#   def assets(self):
#     print("20M$ Assets")
  
#   def borrowings(self):
#     print("5M$ Borrowings")

# class Child(Parent):
#   def degrees(self):
#     print("Masters")

# obj = Child()
# obj.borrowings()
# obj.assets()
# obj.degrees()

# obj1 = Parent()



# Multple Inheritance - when a child has morethan 1 parent

class A():
  def a(self):
    print("Class A")

class B():
  def b(self):
    print("Class B")

class C(A,B):
  def c(self):
    print("Class C")

# obj = C()
# obj.b()



# Multi Level Inheritance
class A():
  def a(self):
    print("Class A")

class B(A):
  def b(self):
    print("Class B")
    
class C(B):
  def c(self):
    print("Class C")

class D(C):
  def d(self):
    print("Class D")


# Hybrid - combo of any two inheritances
class A():
  def a(self):
    print("Class A")

class B(A):
  def b(self):
    print("Class B")
    
class C():
  def c(self):
    print("Class C")

class D(C,B):
  def d(self):
    print("Class D")

# obj = D()
# obj.c()


# Abstraction

# from abc import ABC, abstractmethod

# class ATM(ABC):
#   @abstractmethod
#   def withdrawmoney(self):
#     pass
  
#   # def dosome(self):
#   #   print("hello")
  
# class BackEnd(ATM):
#   def withdrawmoney(self):
#     print("Implementation")
  

# obj = BackEnd()
# obj.withdrawmoney()


# Poly Morphism - + - over loading and overriding

# class Parent():
#   def do_some(self):
#     print("In First Impl")
  
#   def do_some(self,a,b):
#     print("In Second Impl")


# obj = Parent()
# obj.do_some(12,21)


# Overriding - between two classes with Inheritanace

# class Parent():
#   def do_some(self):
#     print("In Parent Impl")

# class Child(Parent):
#   def do_some(self,a,b):
#     print("In Child Impl")

# obj = Child()

# obj.do_some()


# Exception Handling - 

# ip = int(input("Enter a number\t"))

# try:
#   rem = 100/ip
#   print(rem)
# except Exception as e:
#   print(e)

try:
  d = {1:"Ajay"}
  print(d[2])
except Exception as e:
  print(e.with_traceback)

print("Hello")
print("Hello")
print("Hello")
print("Hello")

# Selenium - web testing framework
# website - FE, BE and DB
# FE - html+CSS+js


from selenium import webdriver # to open a tab
from selenium.webdriver.common.by import By # to select the locator
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 


import time

# webdriver
# driver = webdriver.Chrome() # opens a chrome tab
# driver.implicitly_wait(10)
# driver.maximize_window()

# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.get('https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India#Citations')
# driver.get('https://www.academia.edu/35511864/ANCIENT_INDIA?hb-g-sw=34690658')
# driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin") # 10s
# driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123") # 10s

# driver.find_element(By.XPATH,'//button[@type="submit"]').click()

# driver.find_element(By.XPATH, '//span[text()="My Info"]').click()

# driver.execute_script("window.scrollTo(0, 300)")
# driver.execute_script("window.scrollBy(0, 500)", "")
# time.sleep(2)
# driver.find_element(By.XPATH,'(//div[@class="oxd-select-text-input"])[2]').click()
# time.sleep(2)
# driver.find_element(By.XPATH,'(//div[@class="oxd-select-text-input"])[2]').send_keys('oth')
# time.sleep(5)
# driver.find_element(By.XPATH,'(//div[@class="oxd-select-text-input"])[2]').send_keys('Others')
# driver.find_element(By.XPATH,'//div[text()="Other"]').click()
# action = ActionChains(driver)
# time.sleep(3)
# action.move_to_element(driver.find_element(By.XPATH, '//i[@class="oxd-icon bi-question-lg"]')).perform()
# driver.execute_script("window.scrollTo(0, 300)")
# action.scroll_to_element(driver.find_element(By.XPATH,'//select[@id="RESULT_RadioButton-3"]')).perform()

# driver.back()
# title = driver.title
# print("Title is",title)
# time.sleep(3)
# driver.forward()
# title = driver.title
# print("Title is",title)

# driver.refresh()

# url = driver.current_url
# print("name url", url)

# driver.execute_script("window.open('https://gmail.com');")

# driver.execute_script("window.open('https://facebook.com');")


# handlers=driver.window_handles
# print(handlers, len(handlers))

# for each in handlers:
#   driver.switch_to.window(each)
  
#   if("Orange" in driver.title):
#     print(driver.title)
  

# Explicit wait

# WebDriverWait(driver, 30, 3, ignored_exceptions=['NoSuchElementException']).until(EC.presence_of_element_located((By.XPATH, '//h6[text()="Personal Details"]')))



# driver.find_element(By.ID,"male").click()
# driver.find_element(By.ID,"sunday").click()
# driver.find_element(By.ID,"saturday").click()
# driver.find_element(By.ID,"friday").click()

# # driver.find_element(By.XPATH, '//button[text()="Alert"]').click()
# driver.find_element(By.XPATH, '//button[text()="Confirm Box"]').click()
# driver.switch_to.alert.accept()
# msg = driver.find_element(By.XPATH, '//p[@id="demo"]').text
# print(msg)
# time.sleep(5)
# driver.find_element(By.XPATH, '//button[text()="Confirm Box"]').click()
# driver.switch_to.alert.dismiss()
# msg = driver.find_element(By.XPATH, '//p[@id="demo"]').text
# print(msg)

# driver.find_element(By.XPATH, '//button[text()="Prompt"]').click()

# driver.switch_to.alert.send_keys("Hello")
# print(driver.switch_to.alert.text)

# driver.switch_to.frame("frame-one796456169") # handle frame

# select_obj = Select(driver.find_element(By.ID,"RESULT_RadioButton-3"))
# select_obj.select_by_index(1)
# time.sleep(2)
# select_obj.select_by_value("Radio-3")
# time.sleep(2)
# select_obj.select_by_visible_text("Developer")

# action = ActionChains(driver)

# action.double_click(driver.find_element(By.XPATH,'//button[text()="Copy Text"]')).click().perform()

# action.context_click(driver.find_element(By.XPATH,'//button[text()="Copy Text"]')).click().perform()

# action.send_keys(Keys.ARROW_DOWN).perform()
# driver.execute_script("window.scrollTo(0, 300)")
# time.sleep(2)
# src = driver.find_element(By.XPATH,'//p[text()="Drag me to my target"]')
# dest = driver.find_element(By.XPATH,'//p[text()="Drop here"]')

# # action.move_to_element(src).perform()

# action.drag_and_drop(src,dest).perform()

# action.scroll_to_element(driver.find_element(By.XPATH,'//h2[text()="Pagination Table"]')).perform()



# row_count = len(driver.find_elements(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr'))

# col_count = len(driver.find_elements(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr[1]/td'))



# (//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr[1]/td[5]
# dict_data = {}
# for row in range(1, row_count+1):
#   row_data = []
#   for col in range(1, col_count+1):
#     data = driver.find_element(By.XPATH, '(//table[@class="wikitable sortable jquery-tablesorter"])[1]/tbody/tr[{}]/td[{}]'.format(row, col)).text
#     row_data.append(data)
#   dict_data[row_data[0]] = row_data[1:]
  


# print(dict_data)



# act = ActionChains(driver)
# # mouse hovering
# act.move_to_element(driver.find_element(By.XPATH, '//span[text()="Fashion"]')).perform()
# act.move_to_element(driver.find_element(By.XPATH, '//a[text()="Winter"]')).perform()
# driver.find_element(By.XPATH, '//a[text()="Kids SweatShirts"]').click()

# driver.execute_script("window.open('https://gmail.com');")

# driver.execute_script("window.open('https://facebook.com');")

# driver.execute_script("window.open('https://twitter.com');")

# driver.execute_script("window.open('https://instagram.com');")


# windows = driver.window_handles
# for each in windows:
#   driver.switch_to.window(each)
#   print(driver.title)  
#   if(driver.title=="Gmail"):
#     break


# driver.find_element(By.XPATH, '(//button[@class="ds-secondary-button js-swp-download-button text-download-button "])[1]').click()

# # driver.switch_to.frame('som-link')
# driver.find_element(By.ID,'user_email').send_keys("shaikgaleebbasha@gmail.com")
# driver.find_element(By.ID,'user_email').click()
# driver.find_element(By.ID,'user_first_name').send_keys("Galeeb")
# driver.find_element(By.ID,'user_last_name').send_keys("Shaik")
# driver.find_element(By.ID,'user_password').send_keys("test123")
# driver.find_element(By.XPATH, '(//button//div[text()="Download PDF for Free"])').click()


# import os
# os.remove("C:/Users/Lenovo/OneDrive/Documents/xyz.txt")
# res = os.path.isfile('C:/Users/Lenovo/OneDrive/Documents/xyz.txt')
# print(res)
# time.sleep(15)
# driver.quit()

























































