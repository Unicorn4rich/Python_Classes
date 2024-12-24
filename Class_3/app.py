# String 3 types ki hti hain

#  single quote string => ''
#  double quote string => "" 
#  Trpple quote string use for muilti lines => """ """ + ''' ''', 
#  F string dyna,icly value likh sakty hain => f""

#<---------------------------------------------------------------->
names: list = ["Shoaib"] * 4

print(names)  # shoaib print 4 times

#<---------------------------------------------------------------->

name: str = "Khan"

full_Name: str = f"Shoaib {name}"

print(full_Name) # Shoaib Khan

#<---------------------------------------------------------------->
# methods

names2: list = ["shoaib", "ahmed", "Khan"]

# names2.append("azlaan")        # last mein add karega.
# names2.pop()                   # last mein se dlete karega.
# names2.pop(1)                  # index number se delete karega.
return_value = names2.pop()      # last value delete kar ke variable mein return karega.


print(names2)          => ['shoaib', 'ahmed']
print(return_value)    => Khan


#<---------------------------------------------------------------->
# list methods

names: list = ["shoaib", "ahmed", [1,2,3], "khan", "yamm"]

# names.remove("shoaib")                 # value ke naam se value ko delete karega.
# names.insert(1, "azlaan")              # value ko apne diyye huy index number ke opar store karta hai.
# return_value = names.count("shoaib")   # jitni same values list mein hongi unko count kar ke return karega.
# names.sort()                           # alphbetical order mein kar ke dega (A => Z)
# names.reverse()                        # ulta alphabetical order chalega (Z => A)
# names.clear()                          # pori list ko clear kar ke empty kar dega.
second_copy: list =  names.copy()      # hmari list ki dublicate copy bana kar dega.
names[2][1] = 7000                     # list ki second index ki second value ko change kiyya => [1, 7000, 3]

print(second_copy)  #    


#<---------------------------------------------------------------->

names: list = ["dainda"] * 8    # repeat value 8 times.

print(names)


names: list = ["dainda", "ahmed", "ali", "wakeel", "shoaib"] 

return_value = names[0:2]   # 0 index se second index tak se pehly ki value ko nikal kar return karega => ['dainda', 'ahmed']

print(return_value)