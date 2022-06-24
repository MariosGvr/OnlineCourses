# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:20:50 2019

@author: mario
"""

import re
p=re.compile('OS')

with open('P08100.txt') as file_object:
    for line in file_object:
        t=p.match(line)
        if t is not None:
            print(t)
            r=re.compile('\(.*\)')
            #print(re.split('\(|\)',line))
            s=r.search(line).span(0)
            print(line[s[0]+1:s[1]-1])
            