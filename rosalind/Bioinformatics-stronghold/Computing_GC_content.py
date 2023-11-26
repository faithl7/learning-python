
max_gc = 0.0
with open('rosalind_gc.txt') as f:
    file_content = f.readlines()
    for i, line in enumerate(file_content):
        if line.startswith('>'):
            sequence_id = line[1:]
            # reset sequence string
            seq = ""
        else:
            new_seq = line.strip()
            seq = seq + new_seq
            # print if last substring; or if the next substring starts with '>'
            if i==len(file_content)-1 or file_content[i+1].startswith('>'):
                gc = 100 * (seq.count('G') + seq.count('C')) / len(seq)
                if gc > max_gc:
                    max_gc = gc
                    max_id = sequence_id

print(max_id, end='')
print(("{0:.6f}".format(round(max_gc,6))))