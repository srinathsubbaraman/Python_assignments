'''
Name 	:rotate.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Write a function called rotate_word() that takes a string and an integer as parameters, and that returns a new 
string that contains the letters from the original string "rotated" by the given amount. For example, "cheer" rotated by 
7 is "jolly" and "melon" rotated by -10 is "cubed". You might want to use the built-in functions ord, which converts a 
character to a numeric code, and chr, which converts numeric codes to characters.
'''
def str1(str,n):
 
     j=''
 
     for i in str:
 
         j=j+chr(ord(i) + n)
 
     print j

str=raw_input("Enter the string : ")

n=int(raw_input("Enter the no.of characters to be rotated : "))
str1(str,n) 