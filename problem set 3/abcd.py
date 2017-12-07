'''
Name 	:abcd.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order
(double letters are ok). How many abecedarian words are there? (i.e) "Abhor" or "Aux" or "Aadil" should return "True" 
Banana should return "False"?
'''


def is_abecedarian(str1):
    str2=sorted(str1)
    if "".join(str1)=="".join(str2):
      print "true"
    else:
      print"false"
  
str=list(raw_input("enter the comma seperated string:"))
is_abecedarian(str)