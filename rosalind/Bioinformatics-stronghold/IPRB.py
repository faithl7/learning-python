#sample data set
k = 2
m = 2
n = 2

def probability(k, m, n):
#Total population number:
   t = k+m+n  # t represents total number

#probabilities of getting offspring with dominant phenotype from each random parents selection
   t1 = t - 1
   p1 = k/t*(k-1)/t1*1
   p2 = k/t*m/t1*1
   p3 = k/t*n/t1*1              #p1 to p9 are the probabilities of random parent selection;and offspring with dominant phenotype
   p4 = m/t*k/t1*1
   p5 = m/t*(m-1)/t1*0.75
   p6 = m/t*n/t1*0.5
   p7 = n/t*k/t1*1
   p8 = n/t*m/t1*0.5
   p9 = n/t*(n-1)/t1*0
   total_probability = p1+p2+p3+p4+p5+p6+p7+p8+p9
   return total_probability
print(probability(k,m,n))