print("DAY 15") # DATE : 20-09-2025  
#LOOPS

count = 1
while count <= 5 :
    print("consistent")
    count += 1
print("the count is : " , count) 

i = 1
while i <= 38: 
    print("kashmir" , i)
    i += 1
print("the count is : " , i) 

# print 1 to 10

i = 1
while i <= 10:
    print(i)
    i += 1

print("Loop Ended")

i = 5
while i >= 1:
    print(i)
    i -= 1

print("reverse loop end")

j = 5
while j >= 1:
    print("japan" , j)
    j -= 1

print("reverse string loop end")

#practice time
#print even nos

i = 2 #initialization
while i <= 30: #condition
    print(i)
    i += 2     #updation
print("loop end") 

#sum of 5 natural no

j = 1
total = 0  
while j <= 5:
    total += j 
    j += 1
print("sum is :" , total) #15         

#qs print the multiplication table of any no. n

n = int(input("enter number: "))
i = 0
print("the multiplication table is:" )
while i <= 9:
    i += 1
    print(n * i)

print("end") 

#qs print the numbers in the list 

nums = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

print(nums[4]) #print the value which is on 4th index

authors = [ "Sudha Murty", "Arundhati Roy", "Agatha Cristie", "Chitra Banerjee", "Shrishti Chaudhary"]

a = 0
while a < len(authors):
    print(authors[a])
    a += 1

print("dive into reading :)") 

#qs5 search for a number x in tuple using loop

numb = (1, 5, 8, 12, 25, 28, 35, 39, 44, 52, 59, 35)

x = int(input("enter number:"))

i = 0
while i < len(numb):
    if(numb[i] == x):
        print("FOUND at index", i)
        print("number is: ", x , "at index: ", i) 
        break      #it will terminate the loop as soons as search element is found
    else:
        print("searching...")
        
    i += 1

print("Number not found")
    

    
    




