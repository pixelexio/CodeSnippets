"""
Rogerio Snarli - 2019
For learning purposes
"""

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 0 #change to level.

if nterms <= 0:
   nterms = int(input("Plese enter a positive integer" + "\n"))
   print("Fibonacci lets'a goo:")
   for i in range(nterms):
       print(recur_fibo(i))
else:
   print("Fibonacci lets'a goo:")
   for i in range(nterms):
       print(recur_fibo(i))
