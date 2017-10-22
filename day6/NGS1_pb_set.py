#!/usr/bin/env python3
import numpy as np
## -1- count FASTQ file seq

## cur -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/pfb.fastq

fastq_read = open ("pfb.fastq", "r")

line_num_tot = ''
line_cat = ''
seq_mn = ''
line_tot = 0 

for line_num, line in enumerate(fastq_read):
	line_tot += 1
	line_num_tot = line_num % 4
	if line_num_tot == 1:
		line = line.rstrip()
		line_cat += line
#get lenght of seq
seq_len = len(line_cat)
#list comprehension: turn str in list of int (or  alt sol.: #seq_ls_nb = map(ord(seq_ls)))
seq_ls_nb = [ord(nuc) for nuc in line_cat]
seq_mn = sum(seq_ls_nb)/seq_len
# get std dev using numpy
seq_stdev = np.std(seq_ls_nb)

print("total seq length:", seq_len)
print("average read length is", int(line_tot/4))
print("Average quality score is:", '{:.1f}'.format(seq_mn))
print("Standard deviation is:", '{:.1f}'.format(seq_stdev))
