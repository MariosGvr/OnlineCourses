# -*- coding: utf-8 -*-
"""
Created on Mon May 13 11:23:34 2019

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
            
dict_tetr= {}

def perms_repeat(alphabet,n,word):
    if n==0:
        dict_tetr[word]= 0

    else:
        for let in alphabet:
            word+=let
            perms_repeat(alphabet,n-1,word)
            word=word[:-1]
            
alphabet=['A','C','G','T']

k=4
perms_repeat(alphabet,k,"")

for i in range(len(sequence)-3):
    tetr=sequence[i:i+4]
    dict_tetr[tetr] +=1


for val in dict_tetr.values():
    print (val, end=" ")

