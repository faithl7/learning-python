dna_sequence = "GATATATGCATATACTT" #sample dataset
sub_string = "ATAT"

#create a new list to store counts for locations of sub_string
sub_string_locations = [] 

#loop over the DNA sequence to find all sub_string locations
for i in range (0, len(dna_sequence)):
#starting from the start of the sequence, and compare [start:end] of the examined part to the sub_string
    if dna_sequence[i:i+len(sub_string)] == sub_string:
    #if the sequence is similar, append start position to the new list(sub_string_locations)
        sub_string_locations.append(i+1)


#we get all numbers in a list and transform them into strings with map() and join()
print(' '.join(map(str, sub_string_locations)))