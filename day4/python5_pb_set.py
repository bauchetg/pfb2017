#!/usr/bin/env python3

## install module:import os
## get path: use os.getcwd()
## change path: os.chdir("/Users/admin/Desktop/pfb2017/day4")
## import file: curl -O https://github.com/srobb1/pfb2017/blob/master/files/Python_05.txt

## -1-2- script to read/store python05.txt
## open files
#text_write = open ("Pyton_05_uc.txt", "w")
#total_line_up = 0

#with open("python05.txt", "r") as file_object:
#    for line in file_object:
#        line = line.rstrip()
## set upper case
#        line_up = line.upper()
## print 
#        print(line_up)
## send to STDOUT
#        text_write.write(str(line_up) + "\n")
#text_write.close()

## -3- open and print reverse complement of python_05.fasta
## get file
#curl -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_05.fasta

## open files
#fas_read = open ("Python_05.fasta", "r")
#fas_write = open ("Python_05_out.fasta", "w")
##contents = fas_read.read() (doesnt work)

#line_all = ''
#for line in fas_read:
#    if line.startswith ('>'):
#        line_head = line.rstrip()
#        if line_all:
#            ## rev
#            line_rev = line_all[::-1]
#            print(line_rev)
#            line_all = ''
#        print(line_head)
#    else:
#        line = line.rstrip()
#        ## complement
#        line_comp1 = line.replace('T','a')
#        line_comp2 = line_comp1.replace('G','c')
#        line_comp3 = line_comp2.replace('C', 'g')
#        line_comp4 = line_comp3.replace('A','t')
#        line_comp_fi = line_comp4.upper()
#        line_all += line_comp_fi
##output for the last seq (seq 4) after the loop
line_rev = line_all[::-1]
print(line_rev)

## -4- FASTQ

















