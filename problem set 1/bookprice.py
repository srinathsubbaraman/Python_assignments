'''
Name 	:bookprice.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Suppose the cover price of a book is Rs.24.95, but bookstores get a 40% discount. Shipping costs
Rs.3 for the first copy and 0.75p for each additional copy. What is the total wholesale cost for
60 copies?
'''

r = 24.95

n = 24.95*0.4

m = 3

o = 0.75

k = 3+(59*0.75)

t = (n*60)+k

print("The total wholesale cost is :",t)