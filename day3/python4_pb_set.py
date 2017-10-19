#! /usr/bin/python3

## -1- while loop 1 to 100
#count = 0 
#while count <= 100:
#    print("count:", count)
#    count+=1
#print("Done")

## -2- while loop 1 to 1000
#n = 1
#fact = 1
#while  n < 10:
#    print("count:",n)
#    fact= fact*n
#    n+=1
#    print("fact", fact)
#print("Done")

## -3- for loop 
#my_seq =  [101,2,15,22,95,33,2,27,72,15,52]
#num =1 

#for num in my_seq:
#    if num%2 == 0: 
#        print(num)
#print("Done")

## -4- print each element of the list, calculate 2 cumulative sum (even and odd), print
#my_seq =  [101,2,15,22,95,33,2,27,72,15,52]
#even_num = 0
#odd_num = 0

#for num in my_seq:
#    print(num)
#    if num%2 == 0:
#        even_num += num
#    elif num%2 == 1:
#        odd_num += num
#print("even num :", even_num)
#print("odd_num :", odd_num)
#print("Done")
    
## -5- Use pop() and remove() with int. list
## pop
#my_seq =  [101,2,15,22,95,33,2,27,72,15,52]
#print(my_seq)
#pop_val = my_seq.pop(0) # 101
#print("list ", my_seq, "pop val",  pop_val)
## list  [2, 15, 22, 95, 33, 2, 27, 72, 15, 52] pop val 101

## remove
#my_seq =  [101,2,15,22,95,33,2,27,72,15,52]
#print(my_seq)
#rem_val = my_seq.remove(101)
#print("list ", my_seq, "rem val",  rem_val)
##list  [2, 15, 22, 95, 33, 2, 27, 72, 15, 52] rem val None

## -6- use range in a for loop, print 0 to 99
#num=0
#for num in range(100):
#    print(num)

## -7- same from 1 to 100
#for num in range(100):
#    print(num+1)

## -8- same script but with start stop from command line
## -9- same odd
## see count.py

## -10- list of seq

#my_seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#for seq in my_seq:
#    print(seq,"lenght =",len(seq),"bp")

## -11- use tuples 

#my_seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
#lengths = tuple([(seq, len(seq)) for seq in my_seq])
#print(lengths)
## (('ATGCCCGGCCCGGC', 14), ('GCGTGCTAGCAATACGATAAACCGG', 25), ('ATATATATCGAT', 12), ('ATGGGCCC', 8))

## -12- same but  1\t4\tACGT\n"

my_seq = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
lengths = tuple([(seq, len(seq)) for seq in my_seq])
for index, seqlength in  enumerate(lengths):
    print(index, seqlength)

## -13- create shuffled seq
