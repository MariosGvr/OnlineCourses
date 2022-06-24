# -*- coding: utf-8 -*-
"""
Created on Mon May 13 12:02:38 2019

@author: mario
"""

#open file and read the sequence in a line
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