# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:05:25 2019

@author: mario
"""

def perms_repeat(alphabet,n,word):
    if n==0:
        print(word)
    else:
        for let in alphabet:
            word+=let
            perms_repeat(alphabet,n-1,word)
            word=word[:-1]
            
#alphabet=['A','C','G','T']



word=input("place your input here: ")

alphabet = word.split()



k=int(input("how long do you want the strings? "))
perms_repeat(alphabet,k,"")