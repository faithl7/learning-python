dna_seq = "AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"

#transcribe DNA

for i in dna_seq:
    rna_seq = dna_seq.replace("T", "U")
#print(rna_seq)

#get reverse complement of RNA sequence
#create an empty list to store reverse complement RNA string
rna_reversed = []

#reverse compliment DNA sequence and transcribe into RNA
for i in range(len(dna_seq)):

    #complement = {"A":"U", "G":"C", "U":"A", "C":"G"}
    nucleotide = dna_seq[len(dna_seq) -1 -i]
    if nucleotide == "A":
        dna_seq = "T"
        rna_reversed.append("U")
    elif nucleotide == "U":
        rna_reversed.append("A")
    elif nucleotide == "G":
        rna_reversed.append("C")
    elif nucleotide == "C":
        rna_reversed.append("G")
#print(rna_reversed)  

#join rna_reversed list newly created

rna_reversed = "".join(rna_reversed)
#print(rna_reversed)

#Locate open reading frames in the RNA sequences
#translate ORFs to proteins

codon_table = {"UUU": "F",   "CUU": "L",    "AUU": "I",    "GUU": "V",
"UUC": "F",      "CUC": "L",     "AUC": "I",    "GUC": "V",
"UUA": "L",      "CUA": "L",     "AUA": "I",     "GUA": "V",
"UUG": "L",      "CUG": "L",     "AUG": "M",     "GUG": "V",
"UCU": "S",      "CCU": "P",     "ACU": "T",     "GCU": "A",
"UCC": "S",      "CCC": "P",     "ACC": "T",     "GCC": "A",
"UCA": "S",      "CCA": "P",     "ACA": "T",     "GCA": "A",
"UCG": "S",      "CCG": "P",     "ACG": "T",     "GCG": "A",
"UAU": "Y",      "CAU": "H",     "AAU": "N",     "GAU": "D",
"UAC": "Y",      "CAC": "H",     "AAC": "N",     "GAC": "D",
"UAA": "Stop",    "CAA": "Q",     "AAA": "K",     "GAA": "E",
"UAG": "Stop",   "CAG": "Q",     "AAG": "K",     "GAG": "E",
"UGU": "C",     "CGU": "R",    "AGU": "S",     "GGU": "G",
"UGC": "C",      "CGC": "R",    "AGC": "S",     "GGC": "G",
"UGA": "Stop",   "CGA": "R",     "AGA": "R",     "GGA": "G",
"UGG": "W",     "CGG": "R",     "AGG": "R",     "GGG": "G"} 


#codon = amino_acid
#Create an empty string to store ORFs    
#ORF = ""

#for i in range(0, len(rna_seq), 3):
    #codon = rna_seq[i:i+3]
    #start = "AUG"

    #identify start codon in all ORFs
    
    
    #while codon[start] != "stop":
    #ORF += codon_table[codon]

   
    #protein = protein+

    #if codon == "stop":
            #break
    #else:
       # if codon == "stop" and protein not in ORF:
            #ORF.append[protein]
    #protein = protein+
#print(ORF)
                