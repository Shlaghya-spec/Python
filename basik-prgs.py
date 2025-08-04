print("DAY 3")

#Check if the no. is even or odd

num = int(input("Enter a number: "))  # Takes input from the user and converts it to an integer

if num % 2 == 0:                      # Checks if the number is divisible by 2 (i.e., remainder is 0)
    print("Even number")             # If divisible, it's even
else:
    print("Odd number")              # Otherwise, it's odd


#find the largest of two numbers

a = int(input("Enter first number: "))  # Takes first number
b = int(input("Enter second number: ")) # Takes second number

if a > b:                                # Compares a and b
    print("Largest is:", a)              # Prints a if it is greater
else:
    print("Largest is:", b)              # Else prints b



#Fcatorial of a number

num = int(input("Enter a number: "))  # Takes a number as input
factorial = 1                         # Initializes factorial result to 1

for i in range(1, num + 1):           # Loops from 1 to the given number (inclusive)
    factorial *= i                    # Multiplies the current factorial with i in each step

print("Factorial is:", factorial)     # Prints the result

#Multiplication of table

num = int(input("Enter a number: "))     # Takes number input

for i in range(1, 11):                   # Loops from 1 to 10
    print(f"{num} x {i} = {num * i}")    # f-string prints table format (e.g., 5 x 2 = 10)

#Plaindrome check

text = input("Enter a string: ")    # Takes string input

if text == text[::-1]:              # text[::-1] reverses the string; checks if reversed = original
    print("Palindrome")             # If same, it's a palindrome
else:
    print("Not a palindrome")       # Else not

#Sum of first n natural nos 

n = int(input("Enter a number: "))  # Takes number input
total = 0                           # Initializes total sum to 0

for i in range(1, n + 1):           # Loops from 1 to n
    total += i                      # Adds i to total in every step

print("Sum is:", total)             # Prints the result

#Simple calculator

def calculator(a, b, op):                # Defines a function with 2 numbers and operator
    if op == '+':
        return a + b                     # Returns sum
    elif op == '-':
        return a - b                     # Returns difference
    elif op == '*':
        return a * b                     # Returns product
    elif op == '/':
        return a / b                     # Returns division
    else:
        return "Invalid operator"        # If operator doesn't match

num1 = float(input("Enter first number: "))      # Takes float input
num2 = float(input("Enter second number: "))     # Takes second input
operator = input("Enter operator (+, -, *, /): ")# Takes operator

print("Result:", calculator(num1, num2, operator))# Calls function and prints result

#Count vowels

text = input("Enter a string: ")        # Takes input string
vowels = "aeiouAEIOU"                   # Vowel list (both cases)
count = 0                               # Counter starts at 0

for char in text:                       # Goes through each character
    if char in vowels:                  # Checks if char is a vowel
        count += 1                      # Increments counter

print("Number of vowels:", count)       # Prints vowel count


#Check prime no.

num = int(input("Enter a number: "))    # Takes input number
is_prime = True                         # Assume it's prime

if num <= 1:                            # 0 and 1 are not prime
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):  # Loop from 2 to √num
        if num % i == 0:                    # If divisible, it's not prime
            is_prime = False
            break

if is_prime:
    print("Prime number")               # Print if prime
else:
    print("Not a prime number")         # Otherwise not


#Reverse a number

num = int(input("Enter a number: "))   # Takes input number
rev = 0                                # Initializes reversed number to 0

while num > 0:                         # Loop until all digits are processed
    digit = num % 10                   # Extracts last digit
    rev = rev * 10 + digit             # Adds digit to reverse
    num //= 10                         # Removes last digit from num

print("Reversed number is:", rev)      # Print result

              