print("DAY 8") # DATE : 04-08-2025
#LIST #Build-in DataType

#strings are inmutable (unchangeable) -> ONLY ACCESS AND NO CHNG
#list are mutable (changeable) -> CAN ACCESS & CHNG THE VALUE

marks = [78.8 , 89 , 23 , 93.4 ]
print(marks)
print(type(marks))
print(len(marks))
print(marks[1])

student = [ "Karan" , 89 , "Delhi" ]
print(student[0])
student[0] = "Arjun"
print(student)

#List slicing
# we get substring from main string
# ending idx not included

marks = [89 , 56, 67, 34 , 45 , 99]
print(marks) 
print("substring is : " , marks[0:3]) 
print("second substring is : " , marks[1:]) 
print(len(marks)) 
print(marks[-3:-1]) 


