'''
Name 	:oddnum.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Write a program that examines three variables—x, y, and z— and prints the largest odd number among them. 
If none of them are odd, it should print a message to that effect?
'''

num1 = raw_input("Enter the Number 1 : ")

num2 = raw_input("Enter the Number 2 : ")

num3 = raw_input("Enter the Number 3 : ")

n = int(num1)

m = int(num2)

o = int(num3)

if n%2!=0 and n > m and n > o:
  
    print ('The largest number is :',n)

elif m%2!= 0 and m > n and m > o:
  
    print ('The largest number is :',m)

elif o%2!= 0 and o > n and o > m:
  
    print ('The largest number is :',o)

elif n%2 == 0 or m%2 == 0 or o%2 == 0:
  
    print ('The number is even')

else:
  
    print("it is not a number")