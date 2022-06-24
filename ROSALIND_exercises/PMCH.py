# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:41:10 2019

@author: mario
"""

file_name = input("give the file name: ")
list_seq=[]
sequence=''
path = 'C:\\Users\\mario\\Downloads\\' + file_name


with open(path) as file_object:
    for line in file_object:
        if line[0]== ">":
            list_seq.append(sequence)
            sequence=''
            continue
        else:
            sequence += line[:-1]

A=0
G=0
for base in sequence:
    if base == "A":
        A +=1
    if base == "G":
        G += 1


def pper (n):
    if n == 1:
        return 1
    else:
        
        return n*pper(n-1)

AU= pper(A)
GC= pper(G)
print(AU*GC)


