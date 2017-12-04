'''
Name 	:digit.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question::Implement a function that meets the specification below. Use a try-except block.

def sumDigits(s):
	"""Assumes s is a string
	Returns the sum of the decimal digits in s
	For example, if s is 'a2b3c' it returns 5"""?
'''
def digit(s):
 
  t = 0

  for i in s:

    try:

      t = t+int(i)

    except ValueError:

      pass
  
  print t

s=raw_input('Enter the String : ')

digit(s)