# -*- coding: utf-8 -*-
"""Fermat's near misses.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CeGbMyoG5H7KL5jNHVvlhpPnAnIThp5d
"""

# program verifying fermat's near misses for a given range and n

def Numbers(limit, n):
	#define the working range
	for a in range(1, limit + 1):
		for b in range(a, limit + 1):
		
			# checking Fermat's theorem, a^n + b^n = c^n
			x = pow(a, n) + pow(b, n)
			c = pow(x, 1.0 / n)
			c_pow = pow(int(c), n)+1
			y=c_pow==x

			if (y):
				print(a,b,c,n)
 #set limit   
Numbers(10, 5)

