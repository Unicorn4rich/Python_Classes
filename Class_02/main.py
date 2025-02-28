# data types => int, float, str, bool, any
# pep 8 => naming convention document website


# <--------------------------------------------------END------------------------------------------------->
#int amd float

name: str = """shoaib"""

name = 123 #python aik dynamic language hai.  

full_name: str = f"{name} khan"  # opar wali value

print(type(name))
print(full_name)


# <--------------------------------------------------END------------------------------------------------->
#int amd float


my_num: int = 10

my_num: float = 10.00

print(my_num)


# <--------------------------------------------------END------------------------------------------------->
#bool

is_raining: bool = True

print(is_raining)

# <--------------------------------------------------END------------------------------------------------->
#arthmatic operators

num_1: int = 10
totale_value: int = num_1 + 10

print(totale_value)


num_2: int = 10
num_2 = num_2  + 10

print(num_2)


# short hand method

num_1: int = 10
num_1 += 11

print(num_1)  #Output => 21

# <--------------------------------------------------END------------------------------------------------->

num_1: float = 10.9893

print(num_1)  #Output => 10.9893


num_1: float = 11.1376575

print(
    round(num_1)  #Output: => 11
)    

print(
    round(num_1, 2)  #Output: => 11.14  last ke 2 hinso ko chor dena.
)    


#<--------------------------------------------------END------------------------------------------------->

my_name: str = "shoaib "

print(
    len(my_name)  # Output: => hinsy count 6
)


# <--------------------------------------------------END------------------------------------------------->

names: list = ["shoaib", "Khan", "Awais", "Ali"]

print(names)  # ['shoaib', 'Khan']

print(names[0])  # Output: => shoaib

names.append("azlaan")  # add value in last
names.pop()             # delete from last
names.remove("Khan")    # written value remove
deleted_val = names.pop() # give deleted value

print(
    deleted_val
)


# <--------------------------------------------------END------------------------------------------------->
# for loop

Users: list = ["shoaib", "Khan", "Awais", "Ali"]

for single_name in Users:
  print(single_name)    # 2 lines ka gap for loop ko chalne ke liye chahiye hoti hai.
  print(" Hello")
print(" Hello")       # playe only one time
  
# Output  => dono print for loop ka part hain. 

# shoaib
#  Hello
# Khan  
#  Hello
# Awais 
#  Hello
# Ali
#  Hello    