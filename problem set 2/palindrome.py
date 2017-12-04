'''
Name 	:palindrome.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question::A palindrome is a word that is spelled the same backward and forward, like "Malayalam" and "Noon" . Recursively, a word is a palindrome if the first and last letters are the same and the middle is a palindrome. Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.
Use the function definition
def isPalindrome(s):
	"""Assumes s is a str
	Returns True if s is a palindrome; False otherwise.
	Punctuation marks, blanks, and capitalization are
	ignored."""
Ensure you build a test function testIsPalindrome() that tests your palindrome function.
'''
n=raw_input('enter the string')

l=[]

for i in n:

  if i.isalpha():

    j=i.lower()

    l.append(j)

str1="".join(l)

str2=str1[::-1]

if str1==str2:

  print 'palindrome'

else:

  print 'not a palindrome'