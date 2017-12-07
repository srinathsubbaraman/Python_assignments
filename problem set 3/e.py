'''
Name 	:no_e1.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:Modify the above program to print only the words that have no “e” and compute the percentage of the words in
the list have no “e.”?
'''
def str1(n):

  for i in n:

    if i=='e' or i== 'E':

      return False

  return True

count = 0

c = 0

str2 = raw_input("Enter the words : ")

str2 = str2.split(" ")

for n in str2:

  c = c+1

  if str1(n):

    count = count + 1

    print "The words with no 'e' or 'E' are :",n


percentage = (float(count)/float(c))*100

print "The percentage of words with no 'e' or 'E' is :",str(percentage)