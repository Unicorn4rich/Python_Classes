# Definition: A tuple is an ordered, immutable sequence of values.

names: tuple[str, str, str] = ("Shoaib", "Ahmed", "Azlaan")

# print(names[0]) # Shoaib
# # Tuples support slicing like lists.
# print(names[0:2]) # ('Shoaib', 'Ahmed'


#<---------------------------------------------------------------------------------------->
# Accessing Tuple Values
# Since tuples are ordered, you can access values using indexing or slicing

#Creating a tuple
my_tuple = (10, 20, 30, 40, 30)

# Accessing values using indexing
# print(my_tuple[2]) # 30

# Using the index() method to find the first occurrence => (konse index pe aa rhi hai) value
first_index = my_tuple.index(30)
# print(first_index) # 2

# Counting the occurrence of a value
count_30 = my_tuple.count(30)
# print(count_30) # 2

# Slicing a tuple
# print(my_tuple[1:4]) # (20, 30, 40)


#<---------------------------------------------------------------------------------------->
# Set => (Unique Unordered Collection)
# Definition: A set is an unordered collection of unique items

# my_set: set[str] = {"a", "b", "c", "a"} # iski single signle value ke liye ham loop chala sakty hain.
# print(my_set) # dublicate hata diyye => {'c', 'a', 'b'}

# Common methods:
# my_set.add("d")
# print(my_set) # {'a', 'b', 'd', 'c'} index ke hisab se nahi chalti ye list
# my_set.remove("b") 
# print(my_set) # {'d', 'a', 'c'} <= b list se hatt gaya agr ye list meinhota nahi to ye error deta

# my_set.discard("c")
# print(my_set) # {'a', 'd'} => ye bhi value remove karta hai but agr value moujod nahi to error nahi deta

# my_set.pop()
# print(my_set) # last value delete

# my_set.clear()
# print(my_set) # pori set list ko remove kar dega.

# anoter_set = ("g", "d", "o", "s")
# my_set.update(anoter_set)
# print(my_set) # {'b', 'a', 'd', 's', 'o', 'c', 'g'} => 2 set of lists ko jorta hai.

# my_set.union()



#<---------------------------------------------------------------------------------------->
# Accessing Set Values
# Since sets do not support indexing, you typically iterate over them:

# Creating a set
# my_set = {1, 2, 3, 4, 5, 6}

# Iterating over a set to access its values
# for num in my_set:
#     print(num) # 123456

# Adding an element
# my_set.add(7)
# print(my_set) # Output will include 7 (order is not guaranteed)

# Removing an element using remove() and discard()
# my_set.remove(4)
# print(my_set) # {1, 2, 3, 5, 6} => 4 deleted agr ye na hota to error ata.

# my_set.discard(9)
# print(my_set) # agr ye hota to delete ho jata warna error nahi aega.

# Popping an element (removes and returns an arbitrary element)
# popped_value = my_set.pop()
# print(f"popped {popped_value} is here") # 1 
# print(my_set) # {2, 3, 4, 5, 6}



#<---------------------------------------------------------------------------------------->
# Why Use Sets in Python?
# Uniqueness Guarantee (No Duplicates)
# If you need to store unique values and automatically remove duplicates, sets are perfect.

# my_set = {1, 2, 3, 3, 4}
# print(my_set)  # Output: {1, 2, 3, 4} (Duplicates are removed)

# Fast Membership Checking (O(1) Complexity)
# Checking if an element exists in a set is much faster than lists because sets use hashing.

# my_set = {"aplle", "Banana", "Cherry", "Water mellon"}
# print("Banana" in my_set) # True => ye value moujod hai set mein.

#<---------------------------------------------------------------------------------------->
# Set Operations (Union, Intersection, Difference)
# Sets allow powerful mathematical operations:

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# print(set1 | set2) # Union => {1, 2, 3, 4, 5} => mixed
# print(set1 & set2) # Intersection => {3} => dono list mein common value
# print(set1 - set2) # Difrence => {1, 2} => left side waly set1 mein jo value alag hain set2 se unko nikal kar dega.


#<---------------------------------------------------------------------------------------->
# Eliminating Duplicates from a List
# If you have a list with duplicates, you can convert it into a set to remove them:

# dublicate_set = [1,2,3,4,4,5,2,7,6]
# remove_dublicates = set(dublicate_set)
# again_list = list(remove_dublicates)
# print(again_list) # [1, 2, 3, 4, 5, 6, 7] => unique values here


#<---------------------------------------------------------------------------------------->
# Dictionary (Key-Value Pairs)
# Definition: A dictionary stores data in key-value pairs

