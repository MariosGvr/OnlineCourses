# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:22:46 2019

@author: mario
"""
import math
na=0
nt=0
nc=0
ng=0
x=0
poss=[]
seq=input("place the sequence :")
for base in seq:
    if base == "A":
        na +=1
    if base == "T":
        nt +=1
    if base == "G":
        ng +=1
    if base == "C":
        nc +=1

pos=input("place the numbers :").split(" ")
for i in pos:
    poss.append(float(i))


for x in poss:
    number=(na+nt)*(math.log10((1-x)/2))+(nc+ng)*(math.log10(x/2))
    print (round(number,3), end= " ")