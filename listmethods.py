print("DAY 9") # DATE : 06-08-2025
# List Methods

# 1) list.append() -> adds the element at last

list = [3, 4, 5]
list.append(8)
print(list)

# 2) list.sort() -> sorts by ascending order
#    list1.sort(reverse=True) -> descending order

print("list.sort() method")
list1 = [8, 5, 2]
list1.sort()
print("ascending : " , list1)

list2 = [8, 5, 2]
list2.sort(reverse=True)
print("descending : " , list2)

fruits = ["banana" , "litchi" , "apple"]
fruits.sort()
print(fruits)

fruits1 = ["banana" , "litchi" , "apple"]
fruits1.sort(reverse=True)
print(fruits1)

#list.reverse()

list = ['a' , 'g' , 'o']
list.reverse()
print(list)

#list.insert(idx,ele) -> insert element at index

list = ["panipuri" , "shevpuri" , "bhel"]
print(list)
list.insert(1,"vadapav")
print(list)

#list.remove() -> removes first occurences

list8 = [8, 9, 7, 9]
print(list8)
# list8 = [8, 9, 7, 9]
list8.remove(9)
print(list8)

#list.pop(idx) -> removes ele at idx

tall = [4, 5, 7, 9]
print(tall)
tall.pop(2)
print(tall)

#list.copy()
pam = ["pop", "push" ,"stack",]
pam.sort(reverse=True)
pam2 = pam.copy()
print(pam2) 

 
