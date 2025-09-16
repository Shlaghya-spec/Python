print("DAY 11") # DATE : 04-09-2025
#Dictionary

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

print(type(info)) 
print(info)

#accessing values through keys
print(info["subjects"])
print(info["topics"])  
print(info["age"])
print(info["marks"])

#assigning new key value pairs in dict

info["name"] = "agatha"
info["surname"] = "cristie"
print(info) #new dict created

#nested dict
student = {
    "name" : "rahul kaumar",
    "subjects" : {
        "phy" : 95,
        "chem" : 98,
        "math" : 96
    }
}

print(student)
print(student["subjects"]) 
print(student ["subjects"] ["chem"])  



