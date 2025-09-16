print("DAY 12") # DATE : 13-09-2025
#Dictionary Methods

# 1. myDict.keys()

student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 92 ,
        "math" : 95 ,
        "chem" : 97
    }
}

print(student.keys())  #nested dictionaries
print(tuple(student.keys()))  #the keys will be inside parenthisis ()
print(len(student))  #output=2

info = {
    "key" : "value",
    "name" : "visual studio",
    "subjects" : ["Python", "C" , "C++"], #list
    "topics" : ("dict" , "set"),  #tuple
    "learning": "coding",
    "age" : 23,
    "is_adult" : "True",
    "marks": 93.4
     }

print(info.keys())
print(list(info.keys())) #the keys will be inside [..]
print(len(info))  #output=8          #to find total no.of keys
print(len(list(info.keys())))        #function inside function

# 2. myDict.values()
month = {
    "jan" : 31,
    "feb" : 28,
    "march" : 31
}

print(list(month.values())) 

# 3. myDict.items()  returns key value pairs in tuple

summer = {
    "april" : 30,
    "may" : 31,
    "june" : 30
}

print(tuple(summer.items()))

pairs = list(summer.items()) 
print(pairs[1])  

# 4. myDict.get(key) -> returns value according to key

monsoon ={
    "july" : 31,
    "august" : 31,
    "sept" : 30
}

print("BEFORE")
print(monsoon["octo"]) #error
print("AFTER")         #it will not print this


print(monsoon.get("sept")) 
print(monsoon.get("oct"))  #print none
print("AFTER")             #further code will run



# myDict.update(newDict)  -> insert items to dictionary

#adding a new key value pair
monsoon ={
    "july" : 31,
    "august" : 31,
    "sept" : 30
}
new_Dict = {"oct" : "diwali" , "nov" : "no holiday"}
monsoon.update(new_Dict)

# monsoon.update({"oct" : "diwali"})
print(monsoon)

#updating the old value with new one

monsoon.update({"sept" : "navratri"}) 
print(monsoon) 


#practice this methods 












