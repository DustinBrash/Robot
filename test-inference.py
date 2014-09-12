#! /usr/local/bin/python
# This is the inference algorithm to determine if the attributes at the selected 
# points are up to par with the known target. I will pepper this code with comments
# for ease of understanding. 

import cv, cv2, numpy, math, edge, contrast, convert, random, MonteCarlo, array

lines = edge.main() #REMEMBER THIS VARIABLE!!!!
#print lines

def parallel(lines):
	good_lines = [line for line in lines if (line[2] - line[0]) != 0]	
	sort_slopes = sorted(good_lines, key = slope)
	return sort_slopes 		
		
def slope(line):
	return float(line[3] - line[1]) / float(line [2] - line[0])
#change references and rewrite random to work with edges
def randfunct(lines):
	a = 0
	c = [] # declare c up here as list
	while a <= d: # change v to d, < change to <=
		l = raw_input('X-VALUE: ')
		k = raw_input('Y-VALUE: ')
		x = int(l)
		y = int(k)
		a = random.triangular(x, y)
		q = q + 1
		c.append(a) # append a values to list c
		#return q, c #return statement here breaks while loop
	print c

#we are going to assume that q is our image

#DO NOT FORGET TO REMOVE ERROR CHECKING PARTS OF CODE!!!
x = cv2.VideoCapture()
k = []
q = contrast.main()
k = q#q is name of working contrast frame passed from module

slopearray = []
for line in parallel(lines[0]):
	orderedSlope = slope(line)
	slopearray.append(orderedSlope)
	#print orderedSlope#slope(line)

#below I find value from orderedSlope
parr = []
pos = set(slopearray)
for j in pos:
	l = slopearray.count(j)
	if l > 1:
		for n in xrange(l):
			parr.append(j)

#use parr as edges to compare
#start contrast search here, k is contrast frame, parr is parallel lines 

##
##
##Iterative Deepening A* (IDA-STAR) algorithm for vision by Vincent Pugliese and Dustin Brashear, (2014)
##This is a memory sensitive version of A* in which nodes which have reached a certain 
##cost are immediately terminated (much like alpha-beta pruning) #revise?
##The search space is the areas of the plane of vision in which high intensity light has been detected
##The heuristic will start at one of 2 parallel lines and spread out to find the other matching line
##this serves 2 purposes, bouding the local region of intensity for later analysis, and pairing 
##lines when more that 2 lines fo the same slope exist
##
##

#might want to sort parr here...
#k is nodes to be searched, parr is bounds/start


##############!!!!!BROKEN, IGNORE!!!!!###############
def IDASTAR(k, parr):
	navMap = k #this is the map of nodes in which we are navigating
	while len(navMap) != 0:
		#how to find location of parr in k (x, y, e form where x is row, 
		#y is column, e is element at point) (use point as start)		
		x = 0
		y = 0	
		start = [x, y]
		#we might use a Monte Carlo method instead of iterating through all points on graph
		#evaluate "current" (node) to see if it has reached the goal or if it has reached the cost
		#do that with if, elif, else statement
##############!!!!!BROKEN, IGNORE!!!!!###############

##############!!!!!NEEDS REPAIR!!!!!###############
def MonteCarloVision(k, parr):#this program does the actual comparisions on random points
#and determines jointness of k and parr
	MC = MonteCarlo.MonteCarlo() #change MC to operate between parr bounds
	a = MC[0]#MC generates random coords, we only need 1st element here (element 0)	
	for x in MC:
		elem = k[a]
		boundA = #position of element in parr, reference lines for exact location of parallel lines
		boundB = #position of element in parr, reference lines for exact location of parallel lines
		rangeA = range(boundA, boundB)
		if elem in rangeA:#if the position of the element is between bound A and bound B...
			#out = [k[a], True]
			return k[a]#must be broken down more, see what k[a] is in print statement
		else:
			#out = [k[a], False]
			return None
##############!!!!!NEEDS REPAIR!!!!!###############

done = []
mv = MonteCarloVision(k, parr)
done.append(mv) #set function equal to array and append outside of function
print done

########################!!!!!SPECIAL REMINDER!!!!!##########################
#Dont forget to make the edge detection and the contrast processing take exactly one frame per loop of program
#Dont forget to make a final program that imports this one and the communications architecture and loops it
############################################################################

####!!FINAL EVALUATIONS OF DATA HERE!!####
#def probability(done):#generates probability based on brightness
	#for element in done:
		#if element == 

#Final output must be True or False
####!!FINAL EVALUATIONS OF DATA HERE!!####

