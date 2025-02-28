# lambda function

# lambda "paramater": "code body"

# example 1
multiply_function = lambda num : print(num * 2 )
multiply_function(7)


# example 2
multiply_function = lambda num : num * 2 
print(multiply_function(7))


# example 3
multiply_function = lambda num, num2 : num * num2
print(multiply_function(3, 5))

# example 4 => bina naame ke nahi chalega
lambda : print("hello World") # not error because ye chala nahi.

#<------------------------------------------------------------------------------------>
# map

my_names: list[str] = ["shoaib", "iqbal", "ahsan", "Aleem", "Mitho", "azlaan"]

# new_names = map("func", "list")
new_names = map(lambda name : name+ " khan",  my_names)

print(new_names) #not show values =>  <map object at 0x000002585AACB1C0>
print(list(new_names)) # after convert in list =>  ['shoaib khan', 'iqbal khan', 'ahsan khan', 'Aleem khan', 'Mitho khan', 'azlaan khan']


#<------------------------------------------------------------------------------------>
# filter

number_list: list[int] = [3, 33, 54, 7, 8, 2, 89, 23]

#                filter( "function" ,                    "list")
new_list = list( filter( lambda num : num % 2 == 0 ,    number_list) )
print(new_list) # [54, 8, 2]


#<------------------------------------------------------------------------------------>
# reduce

from functools import reduce


number_list: list[int] = [3, 8, 4]

# reduce(      "function",  total   first_val    0   first_val   "list")
total = reduce( lambda       num1,   num2     : num1 + num2,   number_list)
# print(total) # 15


# example 2
storage = 0
for num in number_list:
    storage = storage + num
    
print(storage)  # 15


#<------------------------------------------------------------------------------------>
# functions

def hello(name: str, age: int)-> None:
    print(f"My name is {name} and my age is {age}")     # My name is shoaib and my age is 23 
    
# hello("shoaib", 23) # positional argument
# hello(name="shoaib", age=23) # My name is shoaib and my age is 23
hello(age=23, name="shoaib")  # keyword argument


# # example 2
def func(pos1, pos2, *args):
    print(pos1, pos2) # first second
    print(args)       # ('extra1', 'extra2') => extra argumrnts recevid in tuple.
    
# func("first", "second")    
func("first", "second", "extra1", "extra2")


# # example 3                  keyword reciver double staric
def func(pos1, pos2, pos3, *args, **kwargs):
    print(pos1, pos2) # first second
    print(args)       # ('extra1', 'extra2') => extra argumrnts recevid in tuple.
    print(kwargs)     # {'key1': 'value1', 'key2': 'value2'} => recevid in the form of dictionery
    print(pos3)       # extra1
    
# func("first", "second")    
func("first", "second", "extra1", "extra2", "extra2", key1="value1", key2="value2")



# # example 4                 keyword reciver double staric
def func(pos1, pos2, pos3, *tup, **dic):
    
    print(pos1, pos2)  # first second
    print(tup)         # () => extra argumrnts recevid in tuple.
    print(dic)         # {'key1': 'value1', 'name': 'shoaib', 'age': 23} => recevid in the form of dictionery
    print(pos3)        # extra1
    
# func("first", "second")    
func("first", "second", "extra1", key1="value1", name="shoaib", age=23)


#<------------------------------------------------------------------------------------>
# modules & imports

import math # math library se tmama cheezen import karli math ki.
# print(math.sqrt(25))  # 5.0

from math import pow # sirf aik specific function ko mangwa ry hain.
# print(pow(2, 3)) # 8.0

# alias matlab nick name dena.
import datetime as dt
print(dt.datetime.now())  # 2025-02-24 22:01:28.18984