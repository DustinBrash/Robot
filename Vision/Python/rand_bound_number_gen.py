#! /usr/local/bin/python
import random
#moved function up here for conventions
def randfunct(d):
	q = 0
	c = [] # declare c up here as list
	while q <= d: # change v to d, < change to <=
		l = raw_input('X-VALUE: ')
		k = raw_input('Y-VALUE: ')
		x = int(l)
		y = int(k)
		a = random.triangular(x, y)
		q = q + 1
		c.append(a) # append a values to list c
		#return q, c #return statement here breaks while loop
	print c
#picture size is 640 x 480

d = raw_input('input number of rand: ') 
v = int(d)


randfunct(v) # changed d to v, as d is a string

