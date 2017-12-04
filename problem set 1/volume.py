'''
Name 	:volume.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Practice using the Python interpreter as a calculator:

a) The volume of a sphere with radius r is 4/3pr3. What is the volume of a sphere with radius 5?
Hint: 392.7 is wrong!?
'''

r = int(raw_input("Enter the radius:"))

v = (4*(3.14)*(r**3))/3

print("The volume of the sphere is :",v)
