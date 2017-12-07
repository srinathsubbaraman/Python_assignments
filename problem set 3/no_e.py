'''
Name 	:no_e.py
Date	:04/12/2017
Author 	:srinath.subbaraman
Question:3.In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does not contain the letter 
"e." Since "e" is the most common letter in English, that’s not easy to do. In fact, it is difficult to construct a 
solitary thought without using that most common symbol. It is slow going at first, but with caution and hours of training
you can gradually gain facility. All right, I’ll stop now. Write a function called has_no_e that returns True if the 
given word doesn’t have the letter "e" in it.
'''
def str1(n):

  for i in n:

    if i=='e' or i== 'E':

      return 0

    else:

      return 1

n = raw_input("Enter the string : ")

str2 = str1(n)

if str2 ==0:

  print("The word contains 'e' or 'E'")

if str2 == 1:
 
  print("The word doesnot contain 'e' or 'E'")