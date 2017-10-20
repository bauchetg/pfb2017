#!/usr/bin/env python3

fas_read = open ("Python_08_sub.fasta", "r")
fas_write = open ("Python_08_out.fasta", "w")

line_head = ''
line_all = ''
seq = {}
seq_dict = {}
for line in fas_read:
    if line.startswith ('>'):
        if line_all:
            #print(line_head)
            #print(line_all)            
            line_all = ''
            line_head = line.rstrip() # keep the next sequence header
            seq[line_head] = line_all
            #print(seq)
            #break
        else:
            line_head = line.rstrip() # keep the first  header (only once)
    else:
        line_all += line.rstrip() # generate seq content
        seq[line_head] = line_all
#print(seq) # ptintout the 1st disctionary
#print(line_head) # printout last seq head (only once)
#print(line_all) # printout last seq content (only once)

# creating 2nd dictionnary
for seq_id, seq_str in seq.items():
    #print(seq_ID,seq)
    seq_dict[seq_id] = {'A':seq_str.count('A'), 'T':seq_str.count('T'), 'C':seq_str.count('C'), 'G':seq_str.count('G')}
    print(seq_dict)


## -2- multifasta 
## curl -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/Python_08.fasta
## expected output:
## seq1-frame-1-codons
## CAT GCT TGA GTC'



