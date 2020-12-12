'''
DSC 530 T303 (2213-1)
Purpose of Program:  Getting prepared for the exploratory data analysis
2.1 Exercise: Preparing for Exploratory Data Analysis
Author: Rajasekharreddy Karna
Date: 12/12/2020
'''

#Display the text “Hello World! I wonder why that is always the default coding text to start with”
print ("Hello World!")

#Add two numbers together
# taking and storing first number in num1 variable
num1 = int(input("Enter first number = "))
# taking and storing second number in num2 variable
num2 = int(input("Enter second number = "))
# adding the two numbers and storing it in sum variable
sum = num1 + num2
# printing the sum
print("Sum of first and second numbers =",sum)

#Subtract a number from another number
# subtracting the two numbers and storing it in sub variable
sub = num1 - num2
# printing the sub
print("Subtracting second num from first number =",sub)

#Multiply two numbers
# multiplying the two numbers and storing it in mul variable
mul = num1 * num2
# printing the mul
print("Multiplication of first and second numbers =",mul)

#Divide between two numbers
# Division the two numbers and storing it in div variable
div = num1 / num2
# printing the div
print("Dividing first number with second numbers =",div)

#Concatenate two strings together (any words)
# taking and storing first string in str1 variable
str1 = str(input("Enter first string = "))
# taking and storing second string in str2 variable
str2 = str(input("Enter second string = "))
con = str1 +' '+ str2
print (con)

#Create a list of 4 items (can be strings, numbers, both)
thislist = list((str1, str2, "string", 1, "string123"))
print(thislist)

#Append an item to your list (again, can be a string, number)
entstr = input("Enter item to append to the list = ")
thislist.append(entstr)
print(thislist)

#Create a tuple with 4 items (can be strings, numbers, both)
thistuple = "string", 123, "string123", thislist
print(thistuple)