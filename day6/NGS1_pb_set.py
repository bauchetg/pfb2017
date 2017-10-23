#!/usr/bin/env python3
import numpy as np
## -1- count FASTQ file seq

## cur -O https://raw.githubusercontent.com/srobb1/pfb2017/master/files/pfb.fastq

#fastq_read = open ("pfb.fastq", "r")

#line_num_tot = ''
#line_cat = ''
#line_cat_phred = ''
#seq_mn = ''
#line_tot = 0 

#for line_num, line in enumerate(fastq_read):
#	line_tot += 1
#	#line_num_tot = line_num % 4
#        line_num_tot = line_num % 4
#	if line_num_tot == 1:
#		line = line.rstrip()
#		line_cat += line
#	if line_num_tot == 3:
#		line = line.rstrip()
#		line_cat_phred += line	
##get lenght of seq
#seq_len = len(line_cat)
#seq_len_phred = len(line_cat_phred)
##list comprehension: turn str in list of int (or  alt sol.: #seq_ls_nb = map(ord(seq_ls)))
#seq_ls_nb = [ord(nuc) for nuc in line_cat]
#seq_ls_nb_phred = [ord(nuc) for nuc in line_cat_phred]
#print(seq_ls_nb_phred)
#seq_mn = sum(seq_ls_nb)/seq_len
#seq_mn_phred = sum(seq_ls_nb_phred)/seq_len_phred
## get std dev (numpy)
#seq_stdev = np.std(seq_ls_nb)
#seq_stdev_phred = np.std(seq_ls_nb_phred)

#print("total seq length:", seq_len)
#print("average read length is", int(seq_len/(line_tot/4)))
#print("Average quality score is:", '{:.1f}'.format(seq_mn))
#print("Standard deviation seq lenght is:", '{:.1f}'.format(seq_stdev))
#print("Standard deviation Phred score is:", '{:.1f}'.format(seq_stdev_phred))

## -2- trim fastQ seq qith phred score < 20
import re
fastq_read = open ("pfb.fastq", "r")

line_num_tot = ''
line_cat = ''
line_cat_phred = ''
seq_mn = ''
line_tot = 0

for line_num, line in enumerate(fastq_read):
	line_num_tot = line_num % 4
	if line_num_tot == 1:                                                                                                   
		header_line = line.rstrip()
		print("l1", header_line)
	if line_num_tot == 2:
		line2 = line.rstrip()
		#print("l2", line2)
	if line_num_tot == 3:
		for line_num, line in enumerate(line_num_tot):
			line = line.rstrip()
			print(line)
			if ord(line)- 33 < 20
			line_len = line[0:line]
			print(line_len)
			line_phred_str = str(line_phred)
                        #print("l3",line_phred_str)
	if line_num_tot == 0:
		line = line.rstrip()
		#print("l0",line)








