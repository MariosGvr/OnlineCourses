# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 11:37:52 2019

@author: mario
"""
dna_dict={}

#import re
#fastaname = re.compile("^>\w+")
#sequence = re.compile("^(?!>).+")
sequence=""
header=""
with open('rosalind_grph.txt') as file_object:
    for line in file_object:
        if line[0]== ">":
            dna_dict.update({header:sequence})
            header = line[1:-1]
            sequence=""

        else:
            if line[-1]!= "\n":
                sequence += line
            else:
                sequence += line[:-1]
    dna_dict.update({header:sequence})




list_str=""
for codename,seq in dna_dict.items():
    for codename2,seq2 in dna_dict.items():
        if seq[-3:]==seq2[:3] and seq!=seq2:
            #print (seq, codename, " ", seq2, codename2)
            list_str+=codename+" "+codename2+"\n"
            
print(list_str)