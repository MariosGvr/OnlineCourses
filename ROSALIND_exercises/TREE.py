# -*- coding: utf-8 -*-
"""
Created on Sat Apr 13 11:54:53 2019

@author: mario
"""

n= int(input ("How many nodes? "))

edge_list=[]

edges= input("give the edges: ").split("\n")
for edge in edges:
    ed=edge.split(" ") #ed einai string
    ed=list(map(int, ed))
    edge_list.append(tuple(ed))    

  
  
cclist=[]

for i in range(n):
    cclist.append([i+1])

for edge in edge_list:
    tempcc=[]
    temp=[]
    for cc in cclist:
        if edge[0] in cc:
            if edge[1] in cc:
                tempcc.append(cc)
            else:
                if len(temp)==0:
                    temp=cc
                else:
                    temp+=cc
                    tempcc.append(temp)
        else:
            if edge[1] in cc:
                if len(temp)==0:
                    temp=cc
                else:
                    temp+=cc
                    tempcc.append(temp)
            else:
                tempcc.append(cc)
    cclist=tempcc           
print(len(cclist)-1)