#!usr/bin/python3

#my_dna = 'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCG'

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


## -4- find position of EcoRI


