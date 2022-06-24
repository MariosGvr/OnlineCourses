# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:24:07 2019

@author: mario
"""

import math

#Longest Increasing Subsequence
list_num= input("place the numbers here: ").split(" ")
lis= list_num[0]
list_lis=[]
seq=""
n=len(list_num)

list_num=[int(x) for x in list_num]



def lgis (X,N):
    P=[0]*N
    M=[0]*(N+1)
    L=0
    for i in range(N):
        lo=1
        hi=L
        while lo<=hi:
            mid=math.ceil((lo+hi)/2)
            if X[M[mid]]<=X[i]:
                lo=mid+1
            else:
                hi=mid-1
        newL=lo
        P[i] = M[newL-1]
        M[newL] = i
        if newL>L:
            L=newL
    S=[0]*L
    k=M[L]
    for i in reversed(range(L)):
        S[i]=X[k]
        k=P[k]
    return S

def lgds (X,N):
    P=[0]*N
    M=[0]*(N+1)
    L=0
    for i in range(N):
        lo=1
        hi=L
        while lo<=hi:
            mid=math.ceil((lo+hi)/2)
            if X[M[mid]]>=X[i]:
                lo=mid+1
            else:
                hi=mid-1
        newL=lo
        P[i] = M[newL-1]
        M[newL] = i
        if newL>L:
            L=newL
    S=[0]*L
    k=M[L]
    for i in reversed(range(L)):
        S[i]=X[k]
        k=P[k]
    return S

#magic stuff man
print(*lgis(list_num,n), sep= " ")
print(*lgds(list_num,n), sep= " ")