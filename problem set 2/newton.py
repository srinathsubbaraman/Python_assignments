'''
Name 	:newton.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:One way of computing square roots is Newton’s method. Suppose that you want to know the square root of a. If you start with almost any estimate, x, you can compute a better estimate with the following formula: y = (x + a/x)/2 For example, if a is 4 and x is 3:

>>> a = 4.0
>>> x = 3.0
>>> y = (x + a/x) / 2
>>> print y
2.16666666667

a) Write a function NewtonSqrt() to abstract the Newton's Method of calculation Square roots.

b) Write a function named test_square_root that prints a table like this:
    Number |  NewtonSqrt  |    math.sqr  | Difference 
    -------|--------------|--------------|------------------
	1.0|           1.0|           1.0|               0.0 
	2.0| 1.41421356237|1.41421356237 | 2.22044604925e-16
	3.0| 1.73205080757|1.73205080757 |               0.0
	4.0|           2.0|           2.0|               0.0
	5.0| 2.2360679775 |  2.2360679775|               0.0
	6.0| 2.44948974278| 2.44948974278|               0.0
	7.0| 2.64575131106| 2.64575131106|               0.0
	8.0| 2.82842712475| 2.82842712475|  4.4408920985e-16
	9.0|           3.0|           3.0|               0.0


The first column is a number, a; the second column is the square root of a computed with the function NewtonSqrt(); 
the third column is the square root computed by math.sqrt; the fourth column is the absolute value of the difference 
between the two estimates

'''

import math


def newton_sqrt(a,x):
  
    cal=(x+a/x)/2
  
    return cal
  


def test_square_root(a,x):
  
    os=math.sqrt(a)
  
    diff=x-os
  
    print("%.1f \t|\t %.5f \t|\t %.5f \t|\t %.5f" % (a,x,os,diff))
 


b=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]

es=1.0

l1=[]

for i in b:
  
    re=newton_sqrt(i,es)
  
    if re==es:
    
        es=es+1
  
    l1.append(re)

print "Number \t|\t Newtonsqrt \t|\t math.sqr \t|\t Difference"

print "--------|-----------------------|-----------------------|---------------------" 

for i in range(len(b)):
  
    for j in range(len(l1)):
    
        if i==j:
      
            test_square_root(b[i],l1[j])