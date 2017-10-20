#! /usr/bin/env/ python3

## curl -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_06_nobody.txt
## load file
#nob_read = open ("Python_06_nobody.txt", "r")
#content = nob_read.read()
#import re

## -1- find "Nobody" occurences
#nob_found = ''
#output = ''
#nob_fd_stt = ''
#nob_fd_sto = ''

#with open("Python_06_nobody.txt", "r") as file_object:
#    for line_num, line in enumerate(file_object):
        ##print(line_num)
        ##print(line)
#        line = line.rstrip()
#        for nob_found in re.finditer(r"Nobody", line):
#            nob_fd_stt = nob_found.start()
            ##print(nob_fd_stt)
#            nob_fd_sto = nob_found.end()
            ##print(nob_fd_sto)
            ##print(line_num)
#            output = [str(line_num), str(nob_fd_stt), str(nob_fd_sto)]
#            print("\t".join(output))


## find all (other mthd)
#nob_all = re.findall(r"Nobody",content)


## -2- find "Nobody" occurences and replace

#nob_rep = re.sub(r"Nobody",r"Somebody", content)
#print(nob_rep)

## -3-4-5 seq pattern
## curl -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_06.fasta
#fas_read = open ("Python_06.fasta", "r")
#import re 
#name_descr = ''

#for line in fas_read:
#    if line.startswith ('>'):    
#        line = line.rstrip()
#        name_descr = re.search(r">(\S+)\s(.*)", line)
#        print("name: ", name_descr.group(1),"descr: ", name_descr.group(2))

## -6- ApolI
## ApolI pattern R^AATTY 
## load file: curl -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_06_ApoI.fasta 
## Y C/T
## R A/G
fas_read = open ("Python_06_ApoI.fasta", "r")
contents = fas_read.read()

for line_num, line in enumerate(file_object):                                                                           
        ##print(line_num)                                                                                                           ##print(line)                                                                                                        
#line = line.rstrip()
out = re.findall(r"(C|T)AATTY(A|G)",contents)













    





