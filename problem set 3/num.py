'''
Name 	:num.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in 
ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with
the relational operators <, >, etc. For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should 
return False.?
'''

def is_abecedarian(str1):
    str2=sorted(str1)
    if "".join(str1)=="".join(str2):
      print "true"
    else:
      print"false"
  
str=list(raw_input("enter the comma seperated string:"))
is_abecedarian(str)