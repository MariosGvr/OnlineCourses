# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:26:42 2019

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
#print (list_seq)
#print(len(list_seq))


list_seq=list_seq[1:]
#list_seq=["ATTAGACCTG","CCTGCCGGAA","AGACCTGCCG","GCCGGAATAC"]

score=0
score1=0
sequences = []
def thaklapsw(list_seq):
    if len(list_seq)==1:
        print(list_seq[0])
        print('hi')
    else:
        score=0
        score1=0
        max_seq1=''
        max_seq2=''
        merged_seq=''
        for seq1 in list_seq:
            for seq2 in list_seq:
                if seq1 == seq2:
                    continue
                for i  in range(len(seq1)):
                    if seq1[i] == seq2[0]:
                        if seq1[i:] == seq2[:len(seq1[i:])]:
                            score1 = len (seq1[i:])
                            if score1 >= score:
                                score=score1
                                max_seq1=seq1
                                max_seq2=seq2
                                merged_seq=seq1[:i]+seq2
        list_seq.remove(max_seq1)
        list_seq.remove(max_seq2)
        list_seq.append(merged_seq)
        thaklapsw(list_seq)
                            

thaklapsw(list_seq)
