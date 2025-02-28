my_dict: dict[str, any] = {
    "name": "shoaib",
   
}

print(my_dict["name"])  # name acces
print(type(my_dict))    # <class 'dict'>
my_dict["isAlive"] = True
print(my_dict)   # {'name': 'shoaib', 'age': 23, 'isAlive': True} => add anthing in dict value pairs.

del my_dict["age"]  # delete key value pair => agr value nahi hogi hogi to ye error genrate karega.
print(my_dict)   # remaing => {'name': 'shoaib'} kiyun ke age key value pairs delete ho chuka hai.

my_dict.pop("name", None) # Now name key value pair delete => agr value nahi hongi to error nahi dega dict mein bachi baqi value dikha dega.
print(my_dict) # {'age': 23} => remaning

# safe Access
print(my_dict["Crime"])  # genrate error because property does not exsist.
print(my_dict.get("Crime", "not found")) # not found => isme agr non-existing value acces karne ki koshish karenge to ye default 2nd wali value show krwa dega


#<---------------------------------------------------------------------------------------->
# for loop in dictionery

my_dict: dict[str, any] = {
    "name": "shoaib",
    "age": 23,
    "isRaining": True,
}

# for "variable" in "jispe Loop chlana hai"
for key in my_dict:
    print(key)            # show only keys
    print(my_dict[key])   # show only values
    print( f"{key}: {my_dict[key]}")   # show both keys and values
    
    
    
#<---------------------------------------------------------------------------------------->
# for loop using value() method 

my_dict: dict[str, any] = {
    "name": "shoaib",
    "age": 23, 
    "city": "karachi"
    }

# example 1
for key in my_dict.values():   # is method ki wajah se hamen sirf value milegi.
    print(key)  # sirf values print hongi.
    
# example 2    
for key, value in my_dict.items():
    print(f"{key} : {value}")    
    
    
#<---------------------------------------------------------------------------------------->
# Comprehensions    
# Definition: A concise way to create lists, sets, or dictionaries.


# Old Names
old_names_list: list[str] = ["shoaib", "ahmed", "azlaan", "shahzaib", "mithoo"]

# new_list                  modify          single_Name   external_list
names_list: list[str] = [old_name+" khan" for old_name in old_names_list] # is list mein for loop chalega jis se dosri list ke names aenge or modify ho kar isi new list mein save ho jaenge.

print(names_list) # ['shoaib khan', 'ahmed khan', 'azlaan khan', 'shahzaib khan', 'mithoo khan']



# example 2
old_names_list: list[str] = ["shoaib", "ahmed", "azlaan", "shahzaib", "mithoo"]

new_names_list = []

for old_name in old_names_list:
    new_names_list.append(old_name+ " khan")
    
print(new_names_list)  # same work in 2 ways => ['shoaib khan', 'ahmed khan', 'azlaan khan', 'shahzaib khan', 'mithoo khan']


# example 3
old_names_list: list[str] = ["Shoaib", "Ahmed", "AzlAan", "ShahZaib", "MithOo"]

names_list: list[str] = [name.lower()   for name in old_names_list   if name != "shoaib"] # 

print(names_list)  # => ['shoaib', 'ahmed', 'azlaan', 'shahzaib', 'mithoo']



#<---------------------------------------------------------------------------------------->
# Set & Dictionary Comprehension 

names_list: list[str] = ["shoaib", "ahmed", "azlaan", "shahzaib", "mithoo"]

# my_dict = ["code"                     "loop"                 "if condition"]
my_dict = {name: name.upper()    for name in names_list    if name != "shoaib"}

print(my_dict) # {'ahmed': 'AHMED', 'azlaan': 'AZLAAN', 'shahzaib': 'SHAHZAIB', 'mithoo': 'MITHOO'}
print(type(my_dict)) # <class 'dict'>