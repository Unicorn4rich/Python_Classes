my_list: list[int] = [1,2,3,4,5,6,7,8,9,10]

#                   k_word  parameter
new_list = list(map(lambda num: num * 3, my_list)) # One line function => lambda => Arrow function

print(new_list) # Output => [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]


#<------------------------------------------------------------------------------------>
# lambda function => no name function

# store function in variable
add_function = lambda num1, num2: num1 + num2

def add_function(num1: int, num2: int):
    return num1 + num2

print(add_function(10, 4)) # Output: 14


#<------------------------------------------------------------------------------------>

def my_addition_function(num1: int, num2: int)-> int: # return int dega
    return num1 + num2

print(my_addition_function(3,10)) # 13


#<------------------------------------------------------------------------------------>
# Collection of Data

# 1.list   = [] => ["Shoaib", "Azlaan", "Khan"] => we store data in list
# 2.Tuple  = () => ("Shoaib", "Azlaan", "Khan") => Constatnt list mean fix data => values cant change in tuple after initializ => value reassign ho sakti hai iski matlab aik value ki jagah dosri value replace kar sakty hain list conversion se.
# 3.Set    = {} => {"Shoaib", "Azlaan", "Khan"} => Unorderd, unindexed, no dublicate => dublivcation se bachne keliye set bnaya or ye squence mein nahi hota.
# 4.Dict   = {}


# Tuplle cant add, remove, update => apply no methods

my_tuple = ("Shoaib", "Azlaan", "Khan")
my_tuple.remove("Azlaan") # methods not working in tuples
print(my_tuple)


#<------------------------------------------------------------------------------------>
# tupple conversion in list for modifications and again convert in tuple after modification

my_tuple = ("Shoaib", "Azlaan", "Khan") # fix data

my_list_list = list(my_tuple) # now convert in list data for modification
my_list_list.remove("Khan")   # perform action

my_tuple_update = tuple(my_list_list) # again return to tuple after modification



#<------------------------------------------------------------------------------------>
# Set =>  Unorderd, unindexed, no dublicate
# aik jesei values dublicat nahi chahiye to (set) ka use krenge.

my_set = {"Shoaib", "Azlaan", "Khan", "Azlaan", "Khan"}

# print(my_set) # Output => {"Shoaib", "Azlaan", "Khan"}  => (no dublicate) => automatic remove dublicates

# print(my_set[0]) # => Error kiyun ke isme jo values hain unka index hai hi nahi


# example 2

my_set2 = {"Shoaib", "Azlaan", "Khan"}

# print(my_set2) # isme values change hoti rehti hain kiyun ke inke pass index nahi (unindexed) => {'Azlaan', 'Shoaib', 'Khan'}

my_set2.add("sid")  # set mein modification kar sakty hain
# print(my_set2)      # start mein add hua => {'sid', 'Khan', 'Azlaan', 'Shoaib'}
 

#<------------------------------------------------------------------------------------>
# list dublication data remove after conversion in (set)

set_data = ["Shoaib", "Azlaan", "Khan", "Azlaan", "Khan", "sid", 123, 384]
print(set_data)

set_New = set(set_data)
set_data = list(set_New)

print(set_data) # remove all dublicates => [384, 'sid', 'Khan', 'Shoaib', 123, 'Azlaan'


