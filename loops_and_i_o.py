# -*- coding: utf-8 -*-
"""Loops and I/O

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rU_-QfLyz724D7zR_ZIpJPF1LLndNoCn
"""

#Input and output in python
#input("Prompt") is used to input 
#print(value, sep, end, file)
#value- to be printed
#sep- seperator, by default is a space
#end- String to be appended at the end of the statement. Default is a newline(\n).
#file- File where value to be written. Default is sys.stdout
print("Hello", "World", sep='#', end='@@')
print("This is next print statement")

#Input is taken by input() method
input_var = input("What is your name?")
print("Hello", input_var)
#By default, it accepts string but we can typecast it as follows:
any_int= int(input("enter any no"))#If any literal except integer is given, it will raise an error
decimal = float(input("Enter a decimal number"))
any_list = list(int(input("enter an integer")))#Takes integer input and returns a list
print(any_list)
#You can do the same with other data types as well. Ty it!

#Python range
#Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
#Syntax- range(start, stop, step)
#start- starting number, by default 0
#stop - Ending number. Stops at stop-1
#Step - Increment, by default 1
x = range(2,7)
for i in x :print(i) #prints numbers from 2 to 5

#Now that we are familiar with python data types and i/o. We are ready to start with python loops
#Python has 2 loops :
'''1.for in loop
  2. while loop
For loop- Runs for a paticular condition.'''
#for i in range(0,10):
 #    print(i)
#While loop- Executes as long as a condition is satisfied.
#Be precautious while using while loop. If the condition never fails, for example while(True), it results in an infinite loop and might lead to system crash.
#i=1 #initialisation vaiable
#while(i =1):
 # print(Hii)
#!!Don't execute the above 3 lines of code, it is an infinite loop!!

#Python offers an additional functionality of else statement after loops
#ex-
for i in range(2,7):
  print("Round",i)
else: 
  print("in else")

#While-else:

i = 1
while(i<3):
  print('Round',i)
  i= i+1 #Update expression
else:
  print("in else")

#Today's Tasks:
'''
1. Print table upto 10 of 1 to 10 in a single loop. Use both for and while loops.
2. Take integer inputs from user:
    a. An integer z
    b. An integer y
  Print table of z upto y
  Ex- z=6, y=14. You should print table of 6 upto 14
  Use both loops.
'''