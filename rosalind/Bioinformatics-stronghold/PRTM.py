protein_string = "SKADYEK"

#Create dictionary containing monoisotopic mass of 20 amino acids
mass_table = {"A": "71.03711",  "C":  "103.00919", 
"D":  "115.02694",    "E":  "129.04259",  "F":  "147.06841", 
"G":  "57.02146",     "H":  "137.05891",  "I":  "113.08406",    
"K":  "128.09496",    "L":  "113.08406",  "M":  "131.04049",    
"N":  "114.04293",    "P":  "97.05276",   "Q":  "128.05858",     
"R":  "156.10111",    "S":  "87.03203",   "T":  "101.04768",  
"V":  "99.06841",     "W":  "186.07931",  "Y":  "163.06333"}



#create an empty list to store the monoisotopic mass values

weighted_string = []
for i in protein_string:
    print(i)

for key,value in mass_table.items():
    print(key, value)

#for i in enumerate(protein_string):
    #print(i)   

#loop through monoisotopic mass table and protein string, if Letter is present in protein string, get it's value from the dictionary
for key in mass_table:
    if key in protein_string[0:]:

#Append the values to weighted_string list

        weighted_string = (mass_table[key]) #***How to include duplicate values in output????****
        if key in weighted_string:
            weighted_string.append(key)
        print(weighted_string)


    #Weight += sum(int(weighted_string))
    #print(Weight)

        #print(mass_table[key])




