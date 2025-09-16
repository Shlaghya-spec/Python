print("DAY 13") # DATE : 15-09-2025  
#Set in python

collection = {1, 2, 3.14, True, "uniso" , 4, "atlas" , "uniso" } 

print(collection)
print(type(collection)) 
print(len(collection))

collection = {} #empty dict
print(type(collection)) 

collection = set() #empty set syntax
print(type(collection)) 


#Set METHODS
#1. set.add(ele)  

collection = set()
collection.add(1)
collection.add(2)
collection.add(2) #duplicate ele ignored
collection.add(6)
collection.add("monday") #str
collection.add((1,2,3))  #tuple
collection.add(96.6)     #float

print("1.ADD")
print(collection)
print(len(collection))

# #2. set.remove(ele)
collection.remove(2)

print("2.REMOVE")
print(collection)
print(len(collection)) 

# #3. set.clear()
collection.clear()
print("3.CLEAR")
print(len(collection)) #0

#4. set.pop()  pops out random value

eric = {"python" , "deepseek" , "gemini"}

print("4.POP")
print(eric)
print(eric.pop())
print(eric.pop())

#5. set.union(set2) combines both set elements ignoring the repeatition of element

set1 = {1, 2, 3}
set2 ={3, 4, 5}

print("5.UNION")
print(set1)
print(set2)
print(set1.union(set2)) #combining 2 sets here


#6. set.intersection(set1) prints only common elements

set3 = {6, 7, 8}
set4 = {8, 9, 23}

print("6.INTERSECTION")
print(set3)
print(set4)
print(set3.intersection(set4)) #output is 8 


