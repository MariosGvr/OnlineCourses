# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:52:21 2019

@author: mario
"""
#Finding a Protein Motif

#IDs to a list
IDs= input("give the IDs: ")
list_ID= IDs.split("\n")

#create the links
list_links=[]
for ID in list_ID:
    list_links.append("https://www.uniprot.org/uniprot/" + ID + ".fasta")
#print (list_links)

#creates a list od the sequences in one line
list_fasta=[]
for link in list_links:
    import urllib.request
    contents = urllib.request.urlopen(link).read()
    fasta=contents.decode("utf-8").split("\n")
    fasta=fasta [1:-1]
    list_fasta.append("".join(fasta))

count=0
for num in range(len(list_ID)):
    seq= list_fasta[num]
    name= list_ID[num]
    for i in range(len(seq)):
        try:
            if seq[i]=='N' and seq[i+1]!='P' and (seq[i+2]=='S' or seq[i+2]=='T') and seq[i+3]!='P':
        
                count += 1
                if count == 1:
                    print (name)
                print (i+1, end=" ")
        except IndexError as err:
                break
    count = 0
    print ()
        
        
        
'''#finds the positions
import re
pat=re.compile('(N[^P](S|T)[^P])')
from re import finditer

#with open('P08100.txt') as file_object:
for num in range(len(list_ID)):
    seq= list_fasta[num]
    t=pat.search(seq) 
    if t is not None:
        print (list_ID[num])
        
        for match in finditer('(N[^P](S|T)[^P])',seq):
            print(match.start()+1,end=" ")
        print ()
 
    
#print(seq)
    t=pat.finditer(seq)
    if t is not None:
        #print(t)
        #r=re.compile('\(.*\)')
        #print(re.split('\(|\)',line))
        #s=r.search(line).span(0)
        #print(line[s[0]+1:s[1]-1]) 
        print(list_ID[num], "\n", t.start())'''
    
''' if t is not None:
        print(t)
        r=re.compile('\(.*\)')
        #print(re.split('\(|\)',line))
        s=r.search(line).span(0)
        print(line[s[0]+1:s[1]-1])'''
            