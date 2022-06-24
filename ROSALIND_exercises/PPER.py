# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:57:14 2019

@author: mario
"""

        
def pper (n,k,y):
    if k == y:
        return 1
    else:
        y += 1
        return n*pper(n-1,k,y)


n= int(input("n : "))
k= int(input('k :'))
y=0
result=str( pper(n,k,y))
print(result[-6:])
