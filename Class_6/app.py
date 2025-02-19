# defination function work

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]     => Target is tarhn ki list hamen bnani hai.

num_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # 1. is list ki har aik value function mein jaegi aik aik kar ke.

def My_function(num: int):      # 3. function yahn parameter mein har aik value ko recive karega.
    return num * 2              # 4. phir usy 2 se multyply kar ke return kar dega or return wali value map ko di jaegi.

R_New_num_list = list(map(My_function, num_list))  # 2. ye list har aik value ko aik aik kar ke apne braber rakhy function ko wo value deti jaegi.
# 5. function se value map() mein return hogi phir mao wo value list() ko dega phir list wo value is (R_New_num_list) empty rakhy gaye return waly variable mein save krwa dega. 

print(R_New_num_list) # Output => [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# map(function, list) => map 2 cheezen leta hai or ye return nahi karwa pata
# agr map ke andar ki values ko return krwana hai to usy aik list() function mein rakhenge.

# <------------------------------------------------------------------------------------------------>
# Same work with Arrow lambda function 

# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]     => Target is tarhn ki list hamen bnani hai.

num_list: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

# (item: number) => item * 2  => we are usding this structure in typescript
 
R_New_num_list = list(map(lambda item: item * 2, num_list)) # list mein aik value lamda function ke parameter (item) mein aegi
# # phir wo item us value ko 2 se multiply kar ke value ko return krwa dega (R_New_num_list) mein.

# print(R_New_num_list)

# <------------------------------------------------------------------------------------------------>
# lambda function

add = lambda item1, item2: item1 + item2  # lambda function ke pass 2 paramater hain or wo un dono ki values ko plus krwa ke return krwa rha hai (add) mein.

add(2, 6) # yahn se ham argument bhej rhy hain lambda function ke parameters ko.

print(add(2, 6)) # Output => 8 


# <------------------------------------------------------------------------------------------------>
# defination function

def add(item1, item2):
    return item1 + item2

print(add(5, 6)) #Output 11

