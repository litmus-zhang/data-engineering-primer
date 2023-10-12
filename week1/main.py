# Data type
#Integers ==> Numbers

def simpleCalculator():
    getNumber = int(input("Enter a number: "))
    print(f"Double of the Number: {getNumber * 2}")
    print(f"Half of the Number: {getNumber / 2}")
    print(f"Square of the Number: {getNumber ** 2}")

#Boolean ==> Truth / False
# completed = True
# print(completed)
# print(not completed)

#String  ==> "abcdef%!$#"
def GetUserCredentials():
    getFullName = input("What is your name? ")
    getAddress = input("Where do you live? ")
    getAge = input("What is your age? ")

    print(f"His name is {getFullName}, he/she lives at {getAddress}, he is {getAge} old")

# Loops and conditionals

# For loop :=> 

students = ["Aris",  "James", "John", "Bowen"]
# for student in students:
#     print(student)
# While:=>

wanted = "John"

# Go through the list
# check if the current name is the wanted name
# If yes:  print the current name and the index
# If no: continue scanning/loop

# Basic Data structure and Algorithm (FizzBuzz)

# Given an integer n, for every integer i <= n, the task is to print “FizzBuzz” if i is divisible by 3 and 5, “Fizz” if i is divisible by 3, “Buzz” if i is divisible by 5 or i (as a string) if none of the conditions are true.

# Example:

# Input: n = 3
# Output: [1 2 Fizz]

# Input: n = 5
# Output: [1 2 Fizz 4 Buzz]

# Input: n = 19
# Output: [1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz]


# input = integer n
# Output = list of number

def FizzBuzz(n):
    answer = []
    # loop from 1 ==> n
    for i in range(1,n+1):
    # check if the current number is divisible by 3 or 5
        if (i % 3 == 0) and (i % 5 == 0):
            answer.append("FizzBuzz")
        elif i % 5 == 0:
            answer.append("Buzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        else:
            answer.append(i)

    return answer


answer = FizzBuzz(20)
print(answer)

# value = 10 
# print(value // 3)
# print(value % 3)