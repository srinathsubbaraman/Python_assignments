'''
Name 	:string.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question: Write a function isIn() that accepts two strings as arguments and returns True if either string occurs 
anywhere in the other, and False otherwise. Hint: you might want to use the built-in str operation in.
'''

def string(s1,s2):
    if s1 in s2 or s2 in s1:
        print "Strings matched"
    else :
        print "The strings are not matched"
str1=raw_input("Enter the first string : ")
str2=raw_input("Enter the second string : ")
string(str1,str2)