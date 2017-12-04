'''
Name 	:Factorial.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question::Observe the following function definitions. They Calculate the Factorial as per the Mathematical definition 1! = 1 (n + 1)! = (n + 1) * n! Implement factI(n) as an Iterative Implementation & factR(n) as a Recursive Implementation

def factI(n):
	"""Assumes that n is an int > 0
	Returns n!
	Uses Iterative Implementation"""
	
def factR(n):
	"""Assumes that n is an int > 0
	Returns n!
	Uses Recursive Implementation"""
'''
#using itteration
def factorial(n):

  f =1

  for i in range(1,n+1):

    f = f * i

  return f

print factorial(5)



#using recursion


def factorial(n):

  if n==1:

    return 1

  else:

    return n*factorial(n-1)

print factorial(6)