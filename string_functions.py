print("DAY 6") #DATE : 26-07-2025
#STRING FUNCTIONS

#1.str.endswith("---")

str1 = "I am studying python everday"
print(str1.endswith("day")) 
print(str1.endswith("stud")) 

#2.str.capitalize()

str2 = "i am studying consistent everday"
yut = str2.capitalize()
print(yut)

#3.str.replace(old,new)

str6 = "I am pursuing bachelor's degree for NMIET college"
print(str6.replace("u" , "o")) 
print(str6.replace("bachelor's" , "master's"))

#4.str.find("--")

jkl = "Reading is a theraphy and a self-healing technique."
print(jkl.find("n")) #returns the index where it is 1st occured.
print(jkl.find("o")) #-1 it says that char in not valid
print(jkl.find(" ")) #space between words
print(jkl.find("a"))

#5.str.count("--")

win = "Work today better than yesterday's Work."
print(win.count("Work"))

#Practice: WAP to input user's first name and print its length

name = str(input("Enter your name: "))
print("len is : " , len(name)) 

#prac: occurence of $ in a string

dfg = input("Enter the string: ")
cnt = dfg.count("$")
print("the string is : " , dfg)
print("count of '$' is : " , cnt) 

#prac : replace 'bb' from the string with 'sd'

mdh = input("enter the string")
hjk = mdh.replace("bb" , "sd")
print("the original string is : " , mdh)
print("the new string is : " , hjk) 

#HackerRank practiced

#answer link: https://chatgpt.com/share/6884fb5e-757c-8007-bf49-9b358a978235
