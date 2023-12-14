#sample dataset
n = 5
k = 3

#Use fibonacci series pattern to find the total number of rabbits pairs after n months

def fib(n):
    if n > 1:
    #total no. of rabbits in current month: 
    #no. of adults 2 months before * number of pairs of offsprings produced in each generation
    #plus(+) no of rabbits 1 month before 
           
        return (fib(n-2)*k) + fib(n-1)
    else:
        return 1


n = 5
k = 3

#for rosalind exercise; fib(n) == month n-1; (n5 = fib(5-1))
# month 5 = fib(4)
print(fib(n-1))