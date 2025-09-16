print("DAY 14") # DATE : 16-09-2025  
#Set in python
#practice questions

#1. store the key value in dictionary

dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture" , "list of facts & figures"]

}
print(dict) 

#2. list of subjects for students . find how many classrooms needed. 
#so we use set for this we it will store the unique subjects and by counting the length of set , no.of classrooms can be found

subjects = {
    "python" , "java" , "C++" , "python" , "javascript" , "java" ,
    "python" , "java" , "C++" , "c"
}
print(subjects)
print("No.of classrooms: " , len(subjects)) 

#3. enter marks from user store it in dict.

#start with empty dict 
# marks ={}

# n = input("enter your name:")
# marks.update({"name" : n })

# x = int(input("enter the phy: "))
# marks.update({"phy" : x}) 

# y = int(input("enter the chem: "))
# marks.update({"chem" : y}) 

# z = int(input("enter the maths: "))
# marks.update({"maths" : z}) 

# print(marks) 

#3. find out a way to store 9 and 9.0 as seaprate values . Use diff data types

values = {9, "9.0"} #one is int , other is typecasted into str
print(values)

val = {
    ("float" , 9.0),
    ("int" , 9)
}
print(val)
