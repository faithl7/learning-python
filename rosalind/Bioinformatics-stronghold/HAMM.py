sequence_1 = "GAGCCTACTAACGGGAT"
sequence_2 = "CATCGTAATGACGGCCT"

#the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t.
#i.e., the number of positions at which the corresponding symbols are different in strings of equal lengths.

def hamming_distance(s, t):
    if len(sequence_1) != len(sequence_2):
        print("Strings are not equal size!")
    else:
        hamming_dist = 0
        for position in range(len(s)): # len(s) == len(t) in this case
            if sequence_1[position] != sequence_2[position]:
                hamming_dist = hamming_dist + 1 #gets all the positions that are different in the dna_sequences
        return hamming_dist

print(hamming_distance(sequence_1,sequence_2))