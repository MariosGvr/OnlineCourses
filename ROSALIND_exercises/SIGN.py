# -*- coding: utf-8 -*-
"""
Created on Fri May 10 19:44:05 2019

@author: mario
"""


def print_perms(lista,cur_perm,perm_list):
    if len(lista)>1:
        for i in lista:
            cur_perm.append(i)
            listcopy=lista[:]
            listcopy.remove(i)
            print_perms(listcopy,cur_perm,perm_list)
            cur_perm.pop()
    elif len(lista)==1:
        perm=[]
        for i in cur_perm+lista:
            perm.append(str(i))
        perm_list.append(perm)

def print_perms_repetition(lista,cur_perm,perm_list,depth,n):
    if depth<n:
        for i in lista:
            cur_perm.append(i)
            print_perms_repetition(lista,cur_perm,perm_list,depth+1,n)
            cur_perm.pop()
    elif depth==n:
        perm_list.append(cur_perm[:])


n=int(input("how many? "))


lista=[]
for i in range(1,n+1):
    lista.append(i)


num_perms=[]
sign_perms=[]
print_perms(lista,[],num_perms)
#print (num_perms)
print_perms_repetition(['','-'],[],sign_perms,0,n)
#print (sign_perms)

fact=1
power=1
for i in range(n):
    fact*=(i+1)


print(fact*(2**n))

for num_perm in num_perms:
    for sign_perm in sign_perms:
        string_perm=""
        for i in range(n):
            string_perm+=sign_perm[i]+num_perm[i]+' '
        string_perm=string_perm[:-1]
        print(string_perm)
