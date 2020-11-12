# -*- coding: utf-8 -*-
"""Data Science - Batch 1 - Assignment 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YWg-8_biJICsPdRvaHDT8kydutUQX3Gz
"""

# Questions 1:
# Create an empty list. Accept 10 numbers from the user and append to it the list if it is an even number.

def even_number(A): 
   evenlist = []  
   for i in A: 
      if (i % 2 == 0): 
         evenlist.append(i) 
   print("Even lists:", evenlist) 
       
A=list()
n=int(input("Enter the size of the First List ::"))
print("Enter the Element of First  List ::")
for i in range(int(n)):
   k=int(input(""))
   A.append(k)
even_number(A)

# Questions 2:
# Create a notebook on LIST COMPREHENSION. This exercise is to put you in a Self learning mode

square = [i**2 for i in range(1,101)]
print(square)

# Questions 3:
# You have seen in the videos how powerful dictionary data structure is.
# In this assignment, given a number n, you have to write a program that generates a dictionary d which
# contains (i, i*i), where i is from 1 to n (both included).
# Then you have to just print this dictionary d.

def dictionary_function(D):
  num = {}
  for i in range(1, D+1):
    num[i]= i**2
  return num
d1 = int(input("Enter the number : "))
print(dictionary_function(d1))

# Questions 4:
# There is a robot which wants to go the charging point to charge itself. The robot moves in a 2-D plane from the original point (0,0). The robot can
# move toward UP, DOWN, LEFT and RIGHT with given steps.

# Write a program to compute the distance between the current position after a sequence of movement and original point. If the distance is a float, then
# just print the nearest integer (use round() function for that and then convert it into an integer).

import math
print("First point axis x1, y1 ")
print("="*25)
x1 = float(input("Input the value of x1 : "))
y1 = float(input("Input the value of y1 : "))
print("Second point axis x2, y2 ")
print("="*25)
x2 = float(input("Input the value of x2 : "))
y2 = float(input("Input the value of y2 : "))
p1=[x1,y1]
p2=[x2,y2]
dist=math.sqrt (((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print("The distance is : ", round(dist))