'''
Name 	:GCD.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question::The greatest common divisor (GCD) of a and b is the largestnumber that divides both of them with no remainder. 
One way to find the GCD of two numbers is based on the observation that if r is the remainder when a is divided by b, 
then gcd(a, b) = gcd(b, r). As a base case, we can use gcd(a, 0) = a. Write a function called gcd that 
takes parameters a and b and returns their greatest common divisor.?
'''
def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

a=int(raw_input("Enter the first number : "))
b=int(raw_input("Enter the second number : "))
if (a>b):
    n=gcd(a,b)
else:
    n=gcd(b,a)
print ("the gcd of the given two numbers is:",n)
