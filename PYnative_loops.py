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


***##Exercise 8***
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1): #reversed() fuction to reverse list
    print(i)


***##Exercise 9***
for i in range(-10, 0): #range end is exclusive
    print(i)


***##Exercise 10***
for i in range(5):
    print(i)
else:
    print("Done!")


***##Exercise 10***
# range
start = 25
end = 50
print("Prime numbers between 25 and 50 are:")
for num in range(25, 51):
    if num > 1:  #prime numbers are greater than 1
        for i in range(2, num):
            if num % i== 0: #this is not a prime number
                break #break, go to the next number in the loop
        else:
            print(num) 


***##Exercise 11***

#fibonacci series up to 10 terms
print("Fibonacci sequence:")
num1 = 0
num2 = 1
#first two numbers of the sequence
for i in range(10):
    print(num1, end=" ")
    res = num1+num2 #add last 2 numbers to get the next number
    num1=num2 #update values of num1 and num2
    num2=res


#Fibonacci sequence = 0,    1,    1,    2,    3,   5,   8
#                   num1 + num2 = res
#                          num1 + num2


***##Exercise***
