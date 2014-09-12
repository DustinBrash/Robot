#! /usr/local/bin/python
# This is the inference algorithm to determine if the attributes at the selected 
# points are up to par with the known target. I will pepper this code with comments
# for ease of understanding. 

import cv2, numpy, edge, contrast, convert, random, MonteCarlo, array
#feed = video.video() #NOTE: feed is in color & is unchanged video frame
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
	problistA = []
	while i < len(done):#check loop...may need change
		s = done[i]
		#v = s[0]
		try:
			#NEED TO CHANGE TO SET LOGIC IF USING "s"
			if any(s) >= 256:#changed from v
				problistA.append(1.0)
				problistA.append(s)
	
			elif any(s) >= 200 and done[0] < 256:#changed from v
				problistA.append(0.8)
				problistA.append(s)				
	
			elif any(s) >= 150 and done [0] < 200:#changed from v
				problistA.append(0.6)
				problistA.append(s)

			elif any(s) >= 100 and done[0] < 150:#changed from v
				problistA.append(0.4)
				problistA.append(s)

			elif any(s) >= 50 and done[0] < 100:#changed from v
				problistA.append(0.2)
				problistA.append(s)

			elif any(s) < 50:#changed from v
				return None
			
		except TypeError:
			print 'ERROR IN TRY BLOCK'
			return None
		i = i + 1
	return problistA#change v as v is static #changed to include s

problistA = contrastProbgen(done)

def FinalCMP(problistA):
	i = 0
	try:
		while i < len(problistA):
	
			try:
									
				if problistA[i] < 0.8:#changed from 0.6
					return False, None
			except TypeError:
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
print ol
#gradient/texture analysis here...(a final eval)
#NOTE "ol" IS A TUPLE THAT NEEDS UNPACKING BEFORE PROCESSING!!!
#NOTE inconsistancy in capturing 2 separate frames and processing as same, may want to adjust later on
#need to factor in shape of detected objects as well as texture/gradient
