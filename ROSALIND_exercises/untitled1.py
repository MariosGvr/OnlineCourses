# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:44:58 2019

@author: mario
"""
try:
    with open('efee100.txt') as file_object:
        print('ASDF')
except OSError as err:
    print(err.message)
