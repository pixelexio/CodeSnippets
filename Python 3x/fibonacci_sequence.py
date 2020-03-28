#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'pixelexio'
__email__ = 'hello@pixelex.io'
__license__ = 'GPLv3'

"""
A gibonacci number/sequence is when each number is the sum of the two preceding ones, 
starting from 0 and 1. Example: 0, 1, 1, 2, 3, 5, 8, 13...
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
