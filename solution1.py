'''Exercise 1 
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they 
will turn 100 years old. Note: for this exercise, the expectation is 
that you explicitly write out the year (and therefore be out of date the next year). 

Extras:

1. Add on to the previous program by asking the user for another number and 
printing out that many copies of the previous message. 

2. Print out that many copies of the previous message on separate lines. '''

name = input('Enter your name: ')
age = int(input('Enter your age: '))
num = int(input("No of messages: "))
print(num * f"After {100 - age} you will turn 100 years old.")
print(num * f"After {100 - age} you will turn 100 years old.\n")




#   e x e r c i s e s  
 