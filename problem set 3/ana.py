'''
Name 	:ana.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called
is_anagram that takes two strings and returns True if they are anagrams.?
'''

def anagram(str1,str2):
  a=sorted(str1)
  b=sorted(str2)
  if a==b:
    print "true"
  else:
    print "false"
str1=raw_input("enter the string:")
str2=raw_input("enter the string:")
anagram(str1,str2)
