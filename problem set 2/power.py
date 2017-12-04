'''
Name 	:power.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question::A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.?
'''

def is_power(a,b):

  if a==b:

    return True

  elif a%b==0:

    return is_power(a/b,b)

  else:

    print 'not divisible'

    return False

a=int(raw_input('enter the first number'))

b=int(raw_input('enter the second number'))

print is_power(a,b)
