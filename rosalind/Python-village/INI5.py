#create input file (.txt)
#open input file in read mode

f = open('input.txt', 'r')

#create output file as a list
output_file = []


with open("input.txt", "r") as f:
    #print(f.read())
    output_file = [line for pos, line in  enumerate(f.readlines()) if pos % 2 != 0]
#print(output_file)

with open("output_file", "w") as f:
    f.write(''. join([line for line in output_file]))