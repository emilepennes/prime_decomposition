# coding:utf-8
"""The objective is to define all the prime numbers of the prime factorization
 of a strictly positive integer named N. """

N = 0
Y = []
CPT = 0
print("The objective is to define all the prime numbers of the prime factorization",
      " of a strictly positive integer named N.")
while N <= 0:
    try:
        N = int(input("Let's have a strictly positive integer N = "))
    except ValueError:
        print("N must be a strictly positive integer ;) Try again...")

i = 2
X = N
for i in range(2, N+1):
    while X % i == 0:
        Y.append(i)
        CPT += 1
        X /= i


if CPT > 1:
    print("The decomposers of the prime factorization of N are ", Y,
          ". That is why N can be decomposed with", CPT, "integers.")
else:
    print("N is a prime integer.")
    
