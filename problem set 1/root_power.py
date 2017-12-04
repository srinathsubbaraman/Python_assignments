'''
Name 	:root_power.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question: Write a program that asks the user to enter an integer and prints two integers, root and pwr, such that 
0 < pwr< 6 and root**pwr is equal to the integer entered by the user. If no such pair of integers exists, it should print 
a message to that effect.?
'''

num = int(input('Please enter integer: '))
list= []
for root in range (0,num):
    for pwr in range (1,6):
        if root**pwr == num:
            list.append([root,pwr])
if list ==[]:
    print ('No root exist')
else:
    print (list)