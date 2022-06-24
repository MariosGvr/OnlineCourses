# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:01:20 2019

@author: mario
"""

def subsequences(str1,str2,cur_sub,subsequences_list):
    if str1!='' and str2!='':
        for i in range(len(str1)):
            if str1[i]==str2[0]:
                cur_sub+=str2[0]
                subsequences(str1[i+1:],str2[1:],cur_sub,subsequences_list)
                cur_sub=cur_sub[:-1]
        subsequences(str1,str2[1:],cur_sub,subsequences_list)
    else:
        if cur_sub!='':
            subsequences_list.append(cur_sub)
        
        
subs=[]
subsequences('AACCTTGG','ACACTGTGA','',subs)
print(subs)