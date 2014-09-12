#! /usr/local/bin/python
import random

d = raw_input('input number of rand:') 
v = int(d)
def randfunct(d):
	q = 1
	while(q < v):
		l = raw_input('X-VALUE:')
		k = raw_input('Y-VALUE:')
		x = int(l)
		y = int(k)
		a = random.triangular(x, y)
		q = q + 1
		c = [a]
		#return q, c
	print c

randfunct(d)
#c = [a]
#print c
