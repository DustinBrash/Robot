#! /usr/local/bin/python
# This is the inference algorithm to determine if the attributes at the selected 
# points are up to par with the known target. I will pepper this code with comments
# for ease of understanding. 

import cv, cv2, numpy, math, edge, contrast, convert, random, MonteCarlo, array

lines = edge.main() #REMEMBER THIS VARIABLE!!!!
#print lines

def parallel(lines):#BROKEN#
	good_lines = [line for line in lines if (line[2] - line[0]) != 0]	
	sort_slopes = sorted(good_lines, key = slope)
	return sort_slopes 		
		
def slope(line): #BROKEN#
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

##############!!!!!NEEDS REPAIR!!!!!###############
def MonteCarloVision(k, parr):#this program does the actual comparisions on random points
#and determines jointness of k and parr
	MC = MonteCarlo.MonteCarlo() #change MC to operate between parr bounds
	a = MC[0]#MC generates random coords, we only need 1st element here (element 0)	
	for x in MC:
		elem = k[a]
		boundA = #position of element in parr, reference "lines" for exact location of parallel lines
		boundB = #position of element in parr, reference "lines" for exact location of parallel lines
		rangeA = range(boundA, boundB)
		try:#we are having the issues with the if statement below		
			if elem in rangeA:#if the position of the element is between bound A and bound B...
				#out = [k[a], True]
				return k[a]#must be broken down more, see what k[a] is in print statement
		except:
			#out = [k[a], False]
			return None
##############!!!!!NEEDS REPAIR!!!!!###############

done = []#should be [contrast point, slope of line, coord of point]
mv = MonteCarloVision(k, parr)
done.append(mv) #set function equal to array and append outside of function
print done

########################!!!!!SPECIAL REMINDER!!!!!##########################
#Dont forget to make the edge detection and the contrast processing take exactly one frame per loop of program
#Dont forget to make a final program that imports this one and the communications architecture and loops it
############################################################################

####!!FINAL EVALUATIONS OF DATA HERE!!####
def contrastProbgen(done):
	problistA = [] #made of: [[done], P]
	try:
		if done[0] >= 256:
			problistA.append(done[3])
			problistA.append('P = 1.0')
	
		if done[0] >= 200 and done[0] < 256:
			problistA.append(done[3])
			problistA.append('P = 0.8')
	
		if done[0] >= 150 and done [0] < 200:
			problistA.append(done[3])
			problistA.append('P = 0.6')

		if done[0] >= 100 and done[0] < 150:
			problistA.append(done[3])
			problistA.append('P = 0.4')

		if done[0] >= 50 and done[0] < 100:
			problistA.append(done[3])
			problistA.append('P = 0.2')

		if done[0] < 50:
			return none
	except:
		print 'ERROR IN TRY BLOCK'
		return None
	print problistA

contrastProbgen()

def MonteCarloCMP():
	pass #this function is going to verify that each randomly tested point in an area is similar
	#this is a basic form of gradient analysis
def FinalCMP(problistA):
	try:
		if problistA[1] >= 0.6:
			return True, problistA[0]
	finally:
		if problistA[1] < 0.6:
			return False
	except:
		if problistA[1] == None:		
			print 'ERROR IN TRY BLOCK'
			return None
#Final output must be True or False
####!!FINAL EVALUATIONS OF DATA HERE!!####

