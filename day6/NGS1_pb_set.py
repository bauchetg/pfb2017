#!/usr/bin/env python3
import numpy as np
## -1- count FASTQ file seq

## cur -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/pfb.fastq

fastq_read = open ("pfb.fastq", "r")

line_num_tot = ''
line_cat = ''
seq_mn = ''

for line_num, line in enumerate(fastq_read):
	lines_all += line
	line_num_tot = line_num % 4
	#print(line_num_tot)
	if line_num_tot == 1:
		# strip \n
		line = line.rstrip()
		line_cat += line
		#seq_lent.append(len(line))
#get lenght of seq
seq_len = len(line_cat)
#print(seq_len)
# use list comprehnsion to turn str into list of ints (or  alt sol.: #seq_ls_nb = map(ord(seq_ls)))
seq_ls_nb = [ord(nuc) for nuc in line_cat]
seq_mn = sum(seq_ls_nb)/seq_len
#print('{:.1f}'.format(seq_mn)) 
# get std dev using numpy
seq_stdev = np.std(seq_ls_nb)

print('sequence lenght is', seq_len, ' bp,  mean quality score is', '{:.1f}'.format(seq_mn), 'standard deviation is ', {:.1f}'.format(seq_stdev))

