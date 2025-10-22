print("DAY 16") # DATE : 29-09-2025  
#LOOPS
#BREAK and CONTINUE

#BREAK

numb = (1, 5, 8, 12, 25, 28, 35, 39, 44, 52, 59, 35)

x = int(input("enter number:"))

i = 0
while i < len(numb):
    if(numb[i] == x):
        print("FOUND at index", i)
        print("number is: ", x , "at index: ", i) 
        break      #it will terminate the loop as soons as search element is found
    else:
        print("searching....")
        
    i += 1

print("Number not found")


#CONTINUE
#skip 

i = 0
while i <= 5:
    if (i == 3):
        i += 1
        continue #it will skip the element 3 from 1 to 5
    print(i)
    i += 1

#print odd numbers from 1 to 20
print("odd numbers are 1 to 20:")
i = 0
while i <= 20:
    if(i%2 == 0): 
        i += 1
        continue 
    print(i)
    i += 1

#print even numbers from 1 to 15

print("even numbers are from 1 to 15:")
i = 1
while i <= 15:
    if(i%2 != 0):
        i += 1
        continue
    print(i)
    i += 1



