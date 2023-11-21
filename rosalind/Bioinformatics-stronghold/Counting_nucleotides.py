#Counting Nucleotides
#sample dataset

sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#Define a fuction to count all the nucleotides
def count_nucleotides(seq):

#create a new dictionary "dna_counts" to store the results of the nucleotides' counts
    dna_counts = {"A": 0, "C": 0, "G": 0, "T": 0} #set the counter for each nucleotide to zero

#loop over the sequence to find and count the nucleotides
    for nuc in sequence: 
        dna_counts[nuc] += 1 # counts all the nucleotides in the string, and stores values in the dictionary
    return dna_counts

dna_sequence = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result = count_nucleotides(dna_sequence)
print(result)

#to get desired rosalind output format:
#convert value to string str(val) from the dictionary
#use join() method to join the values as a string; with (' ') as a separator and (str(val)) as iterable

print(' '.join(str(val)  for key, val in result.items() ))
 

