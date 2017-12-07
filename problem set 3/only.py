'''
Name 	:only.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Write a function named using_only() that takes a word and a string of letters, and that returns True if the 
word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than "Hoe alfalfa?"
'''

def using_only(str1,fb):
  for i in fb:
    if i in str1:
      return 1
    else:
      return 0


str=raw_input("enter the string:")
fb=raw_input("enter the letters as comma seperated:")
fb=fb.split(',')
re=using_only(str,fb)
if re==1:
  print "true"
else:
  print "false"
