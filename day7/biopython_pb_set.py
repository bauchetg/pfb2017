#!/usr/bin/env python3
import Bio
import re 
from Bio import SeqIO
all_ID = 0

## -1- number of ID

#for record in SeqIO.parse("uniprot_sprot.fasta","fasta"):
    ##print('ID', record.id)
#    all_ID += 1
    ##print('Sequence length', str(record.seq))
    ##print('Sequence alphabet', len(record))
#print("number of sequences", all_ID) # 555594 

## -2 list of description + Salmonella match an count

ID_dict = SeqIO.to_dict(SeqIO.parse("uniprot_sprot.fasta","fasta"))
#print(ID_dict['sp|Q6GZX3|002L_FRG3G'])
list_desc = []
seq_desc_salpar_all = 0
result_file = open("list_salmo.txt","w")

for prot,seq in ID_dict.items():
#seq_desc = re.search(r"OS=..+\bGN=",seq.description)
#print(seq.description)
    list_desc.append(seq.description)
    seq_desc_salpar = re.search(r".*OS=Salmonella paratyphi.*",seq.description) 
    if seq_desc_salpar:
        seq_desc_salpar_all += 1
        print(seq_desc_salpar)
#print(seq_desc_salpar_all)
        #result_file.write(seq_desc_salpar)
#result_file.close()


#print(list_desc)

## -3- generate a fasta file with salmonella subset
## s_paratyphi.prot.fa

#list_salmo_file = "list_salmo.txt" # Input interesting sequence IDs, one per line
#out_file = "s_paratyphi.prot.fa" # Output fasta file

#list_salmo = set()
#with open(list_salmo_file) as file:
#    for line in file:
#        line = line.strip()
#        if line != "":
#            list_salmo.add(line)

#fasta_sequences = SeqIO.parse(open(uniprot_sprot.fasta),'fasta')
#with open(out_file, "w") as file:
#    for seq in fasta_sequences:
#        if seq.id in list_salmo:
#            SeqIO.write([seq], file, "fasta")






















