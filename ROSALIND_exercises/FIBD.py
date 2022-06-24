# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:48:29 2019

@author: mario
"""

#FIBD Mortal Fibonacci Rabbits

rabbit_nums= [0,1]
months= int(input("for how many months? :"))
death_month = int(input("for how many months do they survive? "))
a= death_month 



Fn1=1
Fn2=0
for generation in range(0,death_month-1):
    temp=Fn1
    Fn1+= Fn2
    Fn2= temp
    rabbit_nums.append(Fn1)
    
#print (rabbit_nums)

for month in range(0,months-death_month):
    num_of_rabbits= sum(rabbit_nums[-a:-1])
    #print (rabbit_nums[-a:-1])
    rabbit_nums.append(num_of_rabbits)
    
    
print (rabbit_nums[-1])
    
