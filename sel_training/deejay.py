# data types - String, List, Tuple, Dict and set

# String - immutable

s1 = "Welcome to The First Session"

#index
# print(s1[-15])

# substring/slicing
# print(s1[2:5]) #lco
# print(s1[:8])
# print(s1[2:-1])
# print(s1[::-1]) # reverse a string using slicing


# manipulation funcs / methods

# res = s1.index('First')
# print(res)

# ind = s1.find("Fist") 
# print(ind)


# s2 = s1.replace("First", "1st")
# print(s2)



# s2 = s1.capitalize()
# print(s2)


# format
# name = "John"
# city = "Kansas"
# # print("hello I am {}. I am from {}".format(name, city))

# # split - separating

# # res = s1.split("xyz") # split returns always a list
# # print(res)

# # strip - 
# # print("Before strip", s1)
# # res = s1.strip("p")
# # print("After strip", res)


# # is related func
# # s1 = "he1l2l3o4w5o6rldfdasg"
# s1 = "2456a4356"
# res = s1.isnumeric()
# print(res)




# # List - mutable - heterogeneous data type - []

# # l1 = [1,1.123, True, "Hello"]
# # l1 = [1,2,3,4,5]
# # l1 = ['a','b','c']
# l1 = [21,23,14,32,20,19]
# # index and slicing
# print(l1[::-1])

# # list manipulations
# l1.append(100)
# print(l1)

# l1.insert(2,222)
# print(l1)
# l2 = [1,1,1,1]

# to merge two lists
# l1.extend(l2)
# print(l1)

# remove by index
# l1.pop(2)
# print("After pop", l1)

# remove by value
# l1.remove(100)
# print("After remove", l1)


# # l1 = [1,"hello", True]
# l1.sort(reverse=True)
# print("sorted list",l1)


# l1.reverse()
# print("reversed",l1)

# l1.clear()
# print("clear", l1)


# l2 = l1.copy()
# print(l2)


# ind = l1.count(1)
# print(ind)

# string to a list
# s1 = "Hello World"
# l1 = list(s1)
# print(l1)


# llist to string
# l1 = ["a","b","d","g"]
# s1 = "".join(l1)
# print(s1)


# Dictionary - mutable - {} - index and slicing - unordered

d1 = {"apple": 5, "banana":3, "mango":5, "orange":7}
# print(d1)
# manipulations

# d1['pineapple'] = 9
# print(d1)


# d1.update({'xyz':11, 'pqr':20})
# print(d1)

# d1.pop("mango") # removes the mango kv pair
# print("After POP", d1)

# d1.popitem() # removes the last kv pair
# print("After popitem", d1)

# k = d1.keys()
# print(k)

# v = d1.values()
# print(v)

# i = d1.items()
# print(i)

# d1.clear()
# print(d1)

# does nothing if the key already exists; else it will create a new kv pair
# d1.setdefault("ssiw", 22)
# print(d1)

# d2 = d1.fromkeys([1,2,3,4], "xyz")
# print(d2)




# tuple - immutable - () - index and slicing

# t1 = (2,3,1,5,7,11)

# print(t1[2:5])
# occ = t1.count(2)
# t1.replace(12)


# condition statemenets - if, elif and else
# blocks - if,elif,else,for,while,try,catch,def,class
# block first line should end with colon and from second line its housld have indents


age = 15
# if(age>18):
#     print("Eligible")
#     print("Congrats")
# else:
#     print("Not Eligible")

marks = 55
if(marks>85 and marks<=100):
   print("Grade A")
elif(marks>70 and marks<=85):
    print("Grade B")
elif(marks>45 and marks<=70):
    print("Grade C")
else:
     print("Grade D")

"""
1. Else/elif needs an IF before them
2 one If can have mul elifs but onlyy single else    
3. If one of the block in if/elif/else is executed, all others blocks will bypass    
    """
# age = 20
# if(age>9):
#     print("bye")
# elif(age>10):
#     print("Hello")
# elif(age>12):
#     print("Good morning")
# else:
#     print("Welcome")


country = "India"
state = "KN"
city = "Hubli"

#  Nested If conditions

# if(country=="India"):
#     print("Welcome to India")
#     if(state=="KN"):
#         print("Welcome to KN")
#         if(city=="Bangalore"):
#             print("Welcome to Bangalore")
#         else:
#             print("Not in Bangalore")
#     else:
#         print("Not In KN")
# else:
#     print("You are outside of India")

# Loops - for and while


# ip = "Hello World Welcome To The World Of Coding"

# for i in ip:
#     if(i.isupper()):
#         print(i,end=" ")


# l1 = [21,23,33,24,32,18]

# for i in l1:
#     if(i%2==1):
#         print(i)


# d = {'john':23, 'madhie': 27, 'lilly':31, 'rob': 30, 'calres': 28}

# for i in d:
#     if(d[i]>25):
#         print(i, d[i])


# l1 = [1,2,3,4,5,6,7,8,9,10]
# #create another list with only even numers
# even_list = []
# odd_list = []
# for i in l1:
#     if(i%2==0):
#         even_list.append(i)
#     else:
#         odd_list.append(i)
# print(even_list)
# print(odd_list)


# l1 = [2,3,6,5]
# # create another list that stores squares of the numbers
# # op = [4,9,36,25]

# op = []
# for i in l1:
#     op.append(i*i)
# print(op)


# s1 = "Hello1, How2 are4 Yo5u Do6ing To7day"
# # caps = ['H','H','Y','D', 'T'], lowers = [], numbers = []
# caps = []
# lowers = []
# numbs = []
# spl_chars = []
# for i in s1:
#     if(i.isupper()):
#         caps.append(i)
#     elif(i.islower()):
#         lowers.append(i)
#     elif(i.isnumeric()):
#         numbs.append(i)
#     else:
#         spl_chars.append(i)
# print(caps, lowers,numbs,spl_chars)

# while
# l1 = [1,2,3,4]

# for i in l1:
#     print(i)

# count=0
# while(count<len(l1)):
#     print(l1[count])
#     count+=1


# break and continue
# l1 = [2,1,3,4,5,6,7,8,4,5,6]

# for i in l1:
#     if(i==7):
#         # break # terminating the loop on  a condition
#         continue # will just skip the contition but not terminates
#     print(i)


# Functions - code reuse - def

# def say_hi(name):
#     print("Hello",name)

# say_hi("Peter")
# say_hi("Rob")
# say_hi("Rina", "Tina")
# say_hi()
# say_hi()



# write a function that checks if a number is multiple of 15

# def check_15(num):
#     if(num%15==0):
#         print("{} is perfect divisible of 15".format(num))
#     else:
#         print("{} is NOT a perfect divisible of 15".format(num))

# check_15(19)
# check_15(60)
# check_15(30)



# def check_division(num, divi):
#     if(num%divi == 0):
#         print("{} is perfect divisible of {}".format(num, divi))
#     else:
#         print("{} is NOT A perfect divisible of {}".format(num, divi))
# check_division(100,5)
# check_division(12,6)
# check_division(30,4)


# def check_age(age):
#     if(age>18):
#         status = "Eligible"
#     else:
#         status = "Not Eligible"
#     return status,age

# xyz = check_age(15)
# print(xyz)



# def filter_text(s1):
#     upper_list = []
#     lower_list = []
#     num_list = []
#     for i in s1:
#         if(i.isupper()):
#             upper_list.append(i)
#         elif(i.islower()):
#             lower_list.append(i)
#         elif(i.isnumeric()):
#             num_list.append(i)
#     return upper_list,lower_list,num_list


# up, low, num = filter_text("Hello 123 How Are you 4 Today")
# print(up,low,num)

# args and kwargs

# def my_fun(*args):
#     print(args, type(args))

# my_fun(1,2,3,4,4)
# my_fun(2,1)
# my_fun()



# named arguments
# def emp_data(name="John", age= 29, city="NYC", org="TCS"):
#     print(name,age,city,org)

# emp_data(name="Peter", org="IBM")


# kwargs

def emp_data(**kwargs):
    print(kwargs, type(kwargs))

emp_data(name="Peter", org="IBM", salary="100K", dept="QA")































