'''
Name 	:lar_odd_num.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Write a program that asks the user to input 10 integers, and then prints the largest odd number that was entered.
If no odd number was entered, it should print a message to that effect?
'''

m = 0


for i in range(1, 11):
    
num = int(raw_input('Enter integer %d: ' % i))
    
    if num % 2 != 0 and (num > m):
        
        m = num


if m is 0:
    
    print "The numbers are even"

else:
    
    print "Your largest of odd number is:", m