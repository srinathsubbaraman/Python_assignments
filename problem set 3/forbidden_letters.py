'''
Name 	:forbidden_letters.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if 
the word doesn’t use any of the forbidden letters.?
'''
def avoids(str1,n):
  for i in n:
    if i in str1:
      return 0
    else:
      return 1
str=raw_input("Enter the string : ")
n=raw_input("Enter the Forbidden letters : ")
n=n.split(',')
a=avoids(str,n)
if a==1:
  print "true"
else:
  print "false"