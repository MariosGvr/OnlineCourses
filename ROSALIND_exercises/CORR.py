# -*- coding: utf-8 -*-
"""
Created on Fri May 24 20:03:34 2019

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
    list_seq.append(sequence)
list_seq=list_seq[1:]
 

rev_cop_list=[]
for seq in list_seq:
    b=seq[::-1]
    b=b.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()
    rev_cop_list.append(b)
    
#print(rev_cop_list)
#print(list_seq)

count=0
correct_seqs=[]
wrong_seqs=[]
for seq in list_seq:
    a=list_seq.count(seq)
    b=rev_cop_list.count(seq)
    if a+b > 1:
        if seq not in correct_seqs:
            correct_seqs.append(seq)
    if a+b==1:
        if seq not in wrong_seqs:
            wrong_seqs.append(seq)

#print(correct_seqs)
#print(wrong_seqs)

rev_cop_list=[]
for seq in correct_seqs:
    b=seq[::-1]
    b=b.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()
    rev_cop_list.append(b)

all_correct_seqs= correct_seqs + rev_cop_list

#print(all_correct_seqs)
#print(wrong_seqs)

dh=0
results_list=[]
for wrong_seq in wrong_seqs:
    for correct_seq in all_correct_seqs:
        for i in range(0,len(wrong_seq)):
            if wrong_seq[i] != correct_seq[i]:
                dh+= 1
        if dh==1:
            results= (wrong_seq + "->" + correct_seq)
            if results not in results_list:
                results_list.append(results)
        dh=0
for i in results_list:       
    print(i)