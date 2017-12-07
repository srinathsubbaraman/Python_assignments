'''
Name 	:Palindrome.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question::A string slice can take a third index that specifies the "step size;" that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'?
'''
def is_pal(str): 
    if str == str[::-1]:
        print("It is a palindrome")
    else:
        print("It is not a palindrome") 
str=raw_input("Enter the string") 
is_pal(str) 
