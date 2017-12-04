'''
Name 	:comma_sep.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question: Let s be a string that contains a sequence of decimal numbers separated by commas, e.g., s = '1.23,2.4,3.123'.
 Write a program that prints the sum of the numbers in s.
'''

s=raw_input("Enter the decimal numbers : ")
list = s.split(",")
n=0.0
for i in list:
    n=n+float(i)
print "The sum of decimal values is :",n