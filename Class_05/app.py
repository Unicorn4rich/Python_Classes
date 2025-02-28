numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in numbers:         # loop get one by one value
  print(item)                # print values with indentation method => 2 spaces
  print("next number ....")   # run run multiple times with loop values
print("next number ....")     # Only Once time print


#----------------------------------------------------------------------------------------------
# condition range loop

num = 0

for i in range(10):
  num += i
  print(num)


# OutPut:
  
# 0
# 1
# 3
# 6
# 10
# 15
# 21
# 28
# 36
# 45

#----------------------------------------------------------------------------------------------
# for loop apni di hui condition ke hisab se kese chlaty hain


for i in range(10): 
  print(i)          # => 0 to 9


#          start, end, inc
for i in range(0,    10,  2):
  print(i)
  
# Output  
# 0
# 2
# 4
# 6
# 8



for i in range(1, 10, 1):
  print(i)
  
  if i == 5:   # ye condition values ko 5 pe hi rok degi aage nahi barhny degi.
    break
  
# Output

# 1
# 2
# 3
# 4
# 5

#----------------------------------------------------------------------------------------------
# for loop with index number

names: list = ["Shoaib", "Azlaan", "Bilal", "Ali", "Hassan"]

for index, item in enumerate(names): # ye function lgane se list ki values ke sath index number bhi milenge.
  print("index", index)
  print("item", item)
  
# Output
# index 0
# item Shoaib
# index 1    
# item Azlaan
# index 2    
# item Bilal 
# index 3    
# item Ali   
# index 4    
# item Hassan  


#----------------------------------------------------------------------------------------------
# while loop


num: int = 0

while num <= 5:
  print("Hello")
  num = num + 1
  
# Output
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello  

#----------------------------------------------------------------------------------------------
# Do-While loop not avelible in python

#----------------------------------------------------------------------------------------------
# map function


numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# pass 2 values
# map(function, iterible)

def my_func(num):  # 2. or yahn parameter mein un values ko pass karega.
  return num * 2   # 3. phir jo bhi values aegi usy multiply by 2 kar ke return kar dega is variable mein (my_var)

my_var = list(map(my_func, numbers))  # 1. map 2argument leta hai (function or list) function list mein se aik aik values lega 

print(my_var) # 4 phir ham us values ko print krwa denge.

