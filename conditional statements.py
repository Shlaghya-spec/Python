print("DAY 7") # DATE : 30-07-2025
#Conditional statements

age = int(input("enter ur age : ")) 

if(age >= 18):
    print("can vote")
    print("apply for license")

else:
    print("not applicable for license") 
    print("not applicable for vote too.")

#type_2
# if , elif , elif

light = input("enter the colour of light : ")

if(light == "red"):     #condition needed    #if():
    print("stop the vehicle")
elif(light == "green"):   #condition needed  #elif():
    print("can go")
elif(light == "yellow"):  #condition needed  #elif():
    print("look")
else:           #no condition for this 'else:'
    print("light is broken.\n sorry for inconvenience.")

print("End of Code..") 

#Prac_1

stud = (input("enter your name : "))
marks = int(input("enter your marks : "))

if(marks >= 90):
    print("Student name : " , stud )
    print("Your grade is 'A' !!")
elif(marks >= 80 and marks < 90):
    print("Student name : " , stud )
    print("Your grade is 'B' !")
elif(marks >= 70 and marks < 80):
    print("Student name : " , stud )
    print ("Your grade is 'C' ")
else:
    print("Grade is 'D' ")

#Nesting statements

age1 = 92

if(age1 >= 18):
    if(age1 >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#WAP to check whether the no. is odd or even
num = int(input("enter the number : "))
# rem = num % 2 

if(num % 2 == 0): #rem == 0
    print("EVEN")
else:
    print("ODD")

#WAP to find the greatest no. by user

a = int(input("enter the first no.: "))
b = int(input("enter the second  no.: "))
c = int(input("enter the third no.: "))

if(a > b and a > c):
    print("the first number is greater : " , a)
elif(b > c and b > a ):
    print("the second number is greater : " , b)
else:
    print("the third number is greater : " , c)
 

if(a >= b and a >= c):
    print("first no. is larger " , a)
elif(b >= c):
    print("second no. is larger :" , b)
elif():
    print("third no. is larger" , c)

#four numbers problem
a = int(input("enter the first number: "))
b = int(input("enter the second  number: "))
c = int(input("enter the third number: "))
d = int(input("enter the fourth number: "))

if(a > b and a > c):
    print("the first no. is greater : " , a)
elif(b > c and b > a ):
    print("the second no is greater : " , b)
elif(c > a and c > b):
    print("the third no is greater : " , c)
else:
    print("the fourth number is greater: " , d )


#check number is multiple of 7 and 5 or not
x = int(input("enter number:"))

if(x % 7 == 0 ):
    print("multiple of 7")
else:
    print("not a multiple") 





    
