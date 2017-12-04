'''
Name 	:even.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question::Implement a function that satisfies the specification. Use a try-except block.
def findAnEven(l):
	"""Assumes l is a list of integers
	Returns the first even number in l
	Raises ValueError if l does not contain an even number"""?
'''
def f_even(l):

  for i in l:

    if i%2 == 0:

      return i

s=raw_input('Enter the list of numbers : ')

l=[]

for i in s:

  try:

    l.append(int(i))

  except ValueError:

    pass

if f_even(l):

  print 'the first even is',f_even(l)

else:

  raise ValueError('No even numbers found')