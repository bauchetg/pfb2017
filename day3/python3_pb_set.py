#!usr/bin/python3
my_dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

# test seq 
#my_dna_sub = 'GATGCGCTTC'
#print('my seq is ' + my_dna_sub)

## seq lenght 
#len(my_dna)
#len(my_dna_sub) #10

## -1-2- find  AT and GC content of sub seq
##sub
#AT_ct_sub = 100/len(my_dna_sub)*(my_dna_sub.count("A") + my_dna_sub.count("T"))
#GC_ct_sub = 100/len(my_dna_sub)*(my_dna_sub.count("G") + my_dna_sub.count("C")) 

## -1-2- same with full seq
#ATcontent = 100/len(my_dna)*(my_dna.count("A") + my_dna.count("T"))
#GCcontent = 100/len(my_dna)*(my_dna.count("G") + my_dna.count("C"))

## -3- find reverse complement of seq:
## input data
## Ori_seq5-3 = 'ATGCAGGGGAAACATGATTCAGGAC'  
## Com_seq3-5 = 'TACGTCCCCTTTGTACTAAGTCCTG'  
## RevCom_seq5-3 = 'GTCCTGAATCATGTTTCCCCTGCAT'

my_dna_sub = 'GATGCGCTTC'
print("Original Sequence 5' " + my_dna_sub + " 3'")

my_dna_sub_rev = my_dna_sub[::-1]
print("Complement 3'" + my_dna_sub_rev + " 5'")
my_dna_sub_rev_comp1 = my_dna_sub_rev.replace('T','A')
my_dna_sub_rev_comp2 = my_dna_sub_rev_comp1.replace('A','T')
my_dna_sub_rev_comp3 = my_dna_sub_rev_comp2.replace('G','C')
my_dna_sub_rev_comp4 = my_dna_sub_rev_comp3.replace('C','G')
print("Reverse Complement 5'" + my_dna_sub_rev_comp4 + " 3'")
# complete print

#my_dna = 'A'
#my_nuc = ['A','T','G','C']

#if my_dna == my_nuc[0]:
#    message = 'T'
#    print(message)
#elif my_dna == my_nuc[1]:
#    message = 'A'
#    print(message)
#elif my_dna == my_nuc[2]:
#    message = 'C'
#    print(message)
#elif my_dna == my_nuc[3]:
#    message = 'G'
#    print(message)
#else:
#    message = "this is an undefined char. "
#    print(message)


## -5- find position of EcoRI
## DNA seq
len(my_dna) # 842

## EcoRI seq
EcoRI_53_seq = 'GAATTC'
EcoRI_53 = my_dna.find('GAATTC') # 6
EcoRI_35 = my_dna.find('CTTAAG') 
my_DNA_EcoRI_53_frag = my_dna.split('GAATTC')
len(my_DNA_EcoRI_53_frag) # 2

## upstream seq
my_DNA_EcoRI_53up = my_DNA_EcoRI_53_frag[0]
my_DNA_EcoRI_53uplen = len(my_DNA_EcoRI_53up)+1 # 395 + 1

## downstream seq
my_DNA_EcoRI_53do = my_DNA_EcoRI_53_frag[1]
my_DNA_EcoRI_53dolen = len(my_DNA_EcoRI_53do)+1 # 441 + 1
EcoRI_53_stop = my_DNA_EcoRI_53uplen + len(EcoRI_53_seq)

print("EcoRI restriction site starts at " + str(my_DNA_EcoRI_53uplen) + " bp and ends at " + str(EcoRI_53_stop) + " bp")

## -6- get first and last nuc of each restriction fragments
## nucs
my_DNA_EcoRI_53up_ftnuc = my_DNA_EcoRI_53up[0:1] # G
my_DNA_EcoRI_53up_lsnuc = my_DNA_EcoRI_53up[-1] # A  
my_DNA_EcoRI_53do_donuc = my_DNA_EcoRI_53do[0:1] # G
my_DNA_EcoRI_53do_lsnuc = my_DNA_EcoRI_53do[-1] # G

## get a print of all this 
line = "Sequence is {}\tstarts at {} bp\tends at {} bp\tand is {} bp long."
print("{}\t{}\t{}\t".format(my_DNA_EcoRI_53up,my_DNA_EcoRI_53uplen,my_DNA_EcoRI_53do_donuc))

## -8-create a list of frag
frag_list = []
frag_list.append(my_DNA_EcoRI_53do)
frag_list.append(my_DNA_EcoRI_53up)
print(frag_list)

## -9- sort list (2 ways doing it eith the list based (below) or the sorted() method
frag_list.sort()

## -10- sort by fragment lenght
len_sort = sorted(frag_list, key=len) 
