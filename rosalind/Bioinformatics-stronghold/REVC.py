#compliment_sequence = {"A": "T", "C": "G", "G": "C", "T": "A"}

# We need get: 1. Compliment sequence of DNA sequence provided; 2. Reverse the compliment sequence

dna_strand = "AAAACCCGGT"
#Create reversed_strand string; Add the reversed nucleotides into the reversed_strand string
reversed_strand = ""

#Loop through the dna_strand, compliment the sequence and reverse it

for i in range(len(dna_strand)):

    nucleotide = dna_strand[len(dna_strand) - 1 - i] # identifies the position of the nucleotide examined in each iteration

    if nucleotide == "A":
        reversed_strand = reversed_strand + "T"
    elif nucleotide == "T":
        reversed_strand = reversed_strand + "A"
    elif nucleotide == "G":
        reversed_strand = reversed_strand + "C"
    elif nucleotide == "C":
        reversed_strand = reversed_strand + "G"
    else:
        reversed_strand = reversed_strand + nucleotide
        
print("The input DNA strand is:", dna_strand)
print("The reverse complement is:", reversed_strand)









   