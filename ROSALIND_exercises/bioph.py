# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 20:31:56 2019

@author: mario
"""

#Askisi biophysics

seq=        "MIQQESRLKVADNSGAREVLVIKVLGGSGRRYANIGDVVVATVKDATPGGVVKKGQVVKAVVVRTKRGVRRPDGSYIRFDENACVIIRDDKSPRGTRIFGPVARELRDKDFMKIISLAPEVI"
prognosi= input("place YOUR HBT sequence: ")
paratirisi= "xBxxxxBBBBxBxxxBBBBBBBBBxxxxxxxxBxxxxBBBBBBBBBxxxxxxxxxxBBBBBBBBxxxxBBxxxxxBBxxxxxBBBBBxxxxxBxxxxBxxxBxxxxxxxxxxxxxxxxxxBx"
w=0
z=0
y=0
x=0



seq_len=len(seq)

for i in range(seq_len):
    #print (i)
    if prognosi[i] == "B" and paratirisi[i] == "B":
        w +=1
    elif prognosi[i] == "B" and paratirisi[i] != "B":
        z +=1
    elif prognosi[i] != "B" and paratirisi[i] == "B":
        y +=1
    elif prognosi[i] != "B" and paratirisi[i] != "B":
        x +=1
        
b= 100*(w/(w+y))
nb= 100*(x/(x+z))

Qb= (b+nb)/2

print (Qb)
print ('x= '+str(x)+'\ny= '+str(y)+"\nz= "+str(z)+"\nw= "+str(w))
