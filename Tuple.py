print("DAY 10") # DATE : 08-08-2025
#TUPLE 

tup = (6, 8, 4, 9)
#buil-in datatype
print(type(tup))
print(tup)
#index
print(tup[0])
print(tup[2])
print(tup[-1])

#type of tuple

tup = ()
print(type(tup))
print(tup)

tup = (1,)
print(type(tup))
print(tup) 

tup = (1)
print(type(tup))
print(tup)   #int

tup = (4.0)
print(type(tup))
print(tup)   #float

tup = ("street")
print(type(tup))
print(tup)    #str

#slicing
tup = (7, 4, 3, 5, )
print("complete tuple:" , tup)
print("sliced tuple:" , tup[1:3]) 

#tuple methods

#tup.index(el)
tup = (2, 3, 1, 4)
print(tup.index(1))  #returns the index of element

#tup.count()
tup = (2, 4, 6, 4, 6, 9, 7, 4)
print(tup.count(6))  #count of occurences
print(tup.count(4))

#Practice question 
movies = []

mov1 = input("enter the first movie:")
mov2 = input("enter the second movie:")
mov3 = input("enter the third movie:") 

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print("Your fav movies are: " , movies)

#TYPE2  #appending in same variable
movies = []

mov = input("enter the first movie:")
movies.append(mov)

mov = input("enter the second movie:")
movies.append(mov)

mov = input("enter the third movie:")
movies.append(mov)

print("Your list is : " , movies)

#ADVANCED

movies =[]
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))

print("Your three best movies are: " , movies)

#Practice_2 : check if the list contains palindrome of elements
list1 = [4, 5, 9,]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("NOT palindrome")
      
#char
word = ["m" , "a" , "a" , "m"]

copy_word = word.copy()
copy_word.reverse()

if(copy_word == word):
    print("YES palindrome")
else:
    print("NOT palindrome")

print("END OF CODE")

#count the number of students with the A grade in the tuple
grade = ("A" , "D" , "C" , "A" , "B" , "B" , "A")
print(grade.count("A"))
print(grade.count("B"))
print(grade.count("C"))
print(grade.count("D"))


print("END OF THE DAY!!!")
