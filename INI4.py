#Dataset:
a = 4612
b = 8942

# Return: The sum of all odd integers from a though b, inclusively
result = 0

for n in range(a, b+1): #this produces a range of values between a and b 
    if n %2 == 1:
      result = result + n
print (result)


#n %2 == 1: Used to determine if the integer in odd

#Output = 14672205