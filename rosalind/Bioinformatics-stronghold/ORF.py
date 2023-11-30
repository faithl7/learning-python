#sample dataset
dna = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"


#trancribe DNA sequence from the sample dataset
for i in dna:
    rna = dna.replace("T", "U")
print("RNA seq:", rna)


#reverse complement the DNA sequence provided
#create empty string to store DNA reverse complement sequence

reverse_complement= ""

for i in range(0, len(dna)):

    nucleotide = dna[len(dna) - 1 - i] # identify the position of the nucleotide examined in each iteration

    if nucleotide == "A":
        reverse_complement += "T"

    elif nucleotide == "T":
        reverse_complement += "A"

    elif nucleotide == "G":
        reverse_complement += "C"

    elif nucleotide == "C":
        reverse_complement += "G"
    else:
        reverse_complement += nucleotide

print("DNA reverse complement:", reverse_complement)



#trancribe DNA reverse_complement sequence

for i in reverse_complement:
    rna_reverse = reverse_complement.replace("T", "U")
print("RNA reverse compliment:", rna_reverse)    


#create dictionary to contain codons

codon_table = {"UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V", "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V", "UUA": "L",
            "CUA": "L", "AUA": "I", "GUA": "V", "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V", "UCU": "S", "CCU": "P",
            "ACU": "T", "GCU": "A", "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A", "UCA": "S", "CCA": "P", "ACA": "T",
            "GCA": "A", "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A", "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
            "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D", "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
            "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E", "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
            "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G", "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
            "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}



#create empty list to store open reading frames

ORFs=[]

#Using nested loops, loop through RNA sequence to find ORFs
#codons are read in triplets
#loop through RNA sequence to read nucleotides only in triplets  (-2 ==>start of the last codon triplet read)

for i in range(len(rna)-2):
    #codon == rna[i:i+3]
    if rna[i:i+3] == "AUG":
        start_codon = "AUG"

        j=i 
    #j is used to locate the remaining reding frames in the sequence after the first is located
    
    #create empty string to store frames from the nested loop    
        frame = ""

        start_codon = "AUG"
    
    # nested loop 
    
    #Start reading the frame at the start codon

        while codon_table[start_codon] != "Stop": #the loop is executed as long as the condition is true

            frame += codon_table[start_codon]

            j = j + 3 #codon triplets

    #break the loop if the remaining nucleotides are less than 3 and therefore can't form a codon

            if j>len(rna)-3:

                break

            start_codon = rna[j:j+3]

# Stop reading the current frame when a stop codon is reached
#Add the frame located to the ORFs list

        if codon_table[start_codon] == "Stop" and frame not in ORFs:

            ORFs.append(frame)



#Repeat the loop through the reversed RNA sequence

for i in range(len(rna_reverse)-2):
    #coddon == rna_reverse[i:i+3]

    if rna_reverse[i:i+3] == "AUG":
        start_codon = "AUG"
    
        j=i

        frame = ""

        start_codon = "AUG"

        while codon_table[start_codon] != "Stop":

            frame += codon_table[start_codon]

            j = j + 3 #triplets codon

            if j>len(rna_reverse)-3:

                break

            start_codon = rna_reverse[j:j+3]

        if codon_table[start_codon] == "Stop" and frame not in ORFs:

            ORFs.append(frame)


#ORFs now contains all the possible protein sequences from the Open Reading Frames
#Loop through ORFs list to print all protein strings

for i in ORFs:
    print(i)
                