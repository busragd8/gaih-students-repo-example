# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f36SrGck1NEWZLZNtymThfOP6WBM3wce
"""

#busragdascioglu@gmail.com Büşra Gülnihan Daşcıoğlu

list1 = list(range(2,10,2))
list2 = list(range(1,9,2))

print(list1)
print(list2)

list1.extend(list2) 
list3 = list(list1)
print(list3)

list3.sort()
list3

list3 = [i*2 for i in list3]
print(list3)

for i in list3:
  print("{} verinin tipi: {}".format(i,type(i)))