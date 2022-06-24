# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:43:47 2019

@author: mario
"""
#!/usr/bin/python3

import sys

if len(sys.argv) != 4:
    print ("Usage: python3 "+ sys.argv[0] + " <input_file> <output_file> <delimiter> <position>")
    print ("Eg: python3 converter.py /mnt/c/Users/mario/Documents/Dissertation/dvir_caf1/GCF_000005245.1_dvir_caf1_geno")   
           sys.exit()
path1 = sys.argv[1]
path2 = sys.argv[2]
delimiter = sys.argv[3]
position = int(sys.argv[4])

with open(path1) as file_object:                #open file with the name 34886_ref_ASM402803v1_chrUn.fa
    with open(path2, "a+") as file:             #create a new file with the name ASM402803v1.fa
        for line in file_object:                #read line by line/separate header with lines
            if line[0]== ">":
                line = line[1:]
                newline = ">" + line.split(delimiter)[position] + "\n"
                file.write(newline)

            else:
                file.write(line)