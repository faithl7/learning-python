
s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

#for word in s.split(" "): # Split the input string 's' into a list of words using spaces as separators
    #print(word)


words = s.split(" ") #store the list of words in the 'words' list.

new_collection = {}
#Create an empty dictionary named 'new_collection' to store word count.



for word in words:# Iterate through each word in the 'words' list.

    if word in new_collection:  #Check if the word is already in the 'new_collection' dictionary.

        new_collection[word] += 1 #If the word is already in the dictionary, increase count by 1.

    else:
        new_collection[word] = 1 #If the word is not in the dictionary, add it to the dictionary, the value of the new word is 1.

#print(new_collection)


for key, value in new_collection.items(): #print the contents of the new dictionary in keys and values
    print(key, value)




    
