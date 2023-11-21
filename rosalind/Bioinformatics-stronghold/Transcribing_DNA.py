dna_sequence = "GATGGAACTTGACTACGTAAATT" #sample dataset


#RNA sequence contains Uracil (U) in place of Thiamine (T) as is in DNA

#loop over the DNA sequence to capture all "T" and replace with "U"

for nuc in dna_sequence:
    rna_sequence = dna_sequence.replace("T", "U")  #use .replace() method
print(rna_sequence)