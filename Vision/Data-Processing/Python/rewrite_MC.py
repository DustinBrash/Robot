#! /usr/local/bin/python
# This is the inference algorithm to determine if the attributes at the selected 
# points are up to par with the known target. I will pepper this code with comments
# for ease of understanding. 

import cv, cv2, numpy, math, edge, contrast, convert, random, MonteCarlo, array, video
feed = video.video() #NOTE: feed is in color & is unchanged video frame
lines = edge.main() #REMEMBER THIS VARIABLE!!!!
#print lines

def parallel(lines):
	good_lines = [line for line in lines if (line[2] - line[0]) != 0]	
	sort_slopes = sorted(good_lines, key = slope)
	return sort_slopes 		
		
def slope(line):
	return float(line[3] - line[1]) / float(line [2] - line[0])

#we are going to assume that q is our image

#DO NOT FORGET TO REMOVE ERROR CHECKING PARTS OF CODE!!!
k = []
q = contrast.main()
k = q#q is name of working contrast frame passed from module

slopearray = []
for line in parallel(lines[0]):
	orderedSlope = slope(line)
	slopearray.append(orderedSlope)

#below I find value from orderedSlope
parr = []
pos = set(slopearray)
for j in pos:
	l = slopearray.count(j)
	if l > 1:
		for n in xrange(l):
			parr.append(j)

#v uses format [x0, y0, xF, yF]; v has outer array stripped from lines [[[values][values]]] ---> [[values][values]]
v = lines[0]
#for row in k:
#	for cell in row:
		#compare values at positions
#		pass
def comp(k, v): #find v sub i in k and return element(k)
	i = 1
	pt_val = []
	while i < len(v):
		vi = v[i]
		y = vi[1]
		x = vi[0]
		ki = k[y]
		working_elem = ki[x]
		working_array = [working_elem, x, y]
		pt_val.append(working_array)
		i = i + 1
	#print pt_val
	return pt_val

done = []
wr = comp(k, v)
for element in wr:
	done.append(wr)

####!!FINAL EVALUATIONS OF DATA HERE!!####
def contrastProbgen(done):
	i = 0
	problistA = [] #made of: [[done], P]
	while i < len(done):
		s = done[i]
		v = s[0]
		try:
			if v >= 256:
				#problistA.append(done[3])
				problistA.append(1.0)#fix
	
			elif v >= 200 and done[0] < 256:
				#problistA.append(done[3])
				problistA.append(0.8)#fix
	
			elif v >= 150 and done [0] < 200:
				#problistA.append(done[3])
				problistA.append(0.6)#fix

			elif v >= 100 and done[0] < 150:
				#problistA.append(done[3])
				problistA.append(0.4)#fix

			elif v >= 50 and done[0] < 100:
				#problistA.append(done[3])
				problistA.append(0.2)#fix

			elif v < 50:
				return None
			
		except TypeError:
			print 'ERROR IN TRY BLOCK'
			return None
		i = i + 1
	return problistA
	#print '\n'
	#print '\n'
	#print problistA

problistA = contrastProbgen(done)
###########################################################################################
#gradient analysis here.....gradient analysis is performed by applying a monte carlo method 
#and a modified hamming distance for vision
mc = MonteCarlo.MonteCarlo()



###########################################################################################
def FinalCMP(problistA):
	i = 0
	print problistA
	try:
		while i < len(problistA):       #NEED TO ADD COORDS TO problistA
			try:
									
				if problistA[i] < 0.6:
					return False, None
			except TypeError:
			#if problistA[1] is None:		
			#	print 'ERROR IN TRY BLOCK'
			#	return None
				return None, None
			i = i + 1
	
	except TypeError:
		print 'ERROR IN CMP'
		return None, None
	i = i - 1
	return True, problistA[i]
ol = FinalCMP(problistA)
#Final output must be True or False
####!!FINAL EVALUATIONS OF DATA HERE!!####
print '\n'
print '\n'
print ol
