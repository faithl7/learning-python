**#PYnative_Loops Exercises***


***#Exercise 1***
x = 1 #start of the loop
while x<=10: #stops the loop at 10
    print(x)
    x = x + 1 # gets the  a range of numbers from 1 - 10




***##Exercise 2***
row = 5 #row count 
for i in range(1, 5 + 1,):  #outer loop *(for i in range (row))
    for j in range(1, i + 1): #inner loop *(for j in range (i)) ##nested loop ; ##increments of 1(+1) with each row
        print(j, end=" ") #new line after each row
    print(" ")




***##Exercise 3***
num = 10 #input number
sum = 0
for i in range(1, num + 1):#gets all numbers from 1 to 10, including 10
    sum = sum + i #add current variable to sum
print("sum is:", sum)




***##Exercise 4***
num = 2
for i in range(1, 11): #iterates numbers 1 to 10; stop is exclusive
    result= i*num #multiplies value by 2(input number)
    print(result)




***##Exercise 5***
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 500:
        break # loop stops if current number is greater than 500
    elif i > 150:
        continue  #skips if current number is greater than 150 and continues to the next number in the loop
    elif i % 5 == 0: #checks if number is divisible by 5
        print(i)




***##Exercise 6***
number = 75869

counter = 0
while number !=0: #number is not equal to 0
    number = number//10 #floor division ; truncates decimals from the number
    counter = counter + 1 #counter increment by 1 ; gets the value of all digits in the number
print(counter)




***##Exercise 7***
row = 5 #row count

#reverse loop
for i in range(0, 5 + 1): #outer loop *(for i in range (row))
    for j in range(5 - i, 0, -1):#inner loop *(for j in range (i)) ##nested loop ; ##decrement on 1(-1) with each inner loop
        print(j,end=' ') #new line after each row
    print(" ")



