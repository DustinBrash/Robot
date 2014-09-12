#! /usr/local/bin/python
# This is the frame conversion module

import cv, cv2, numpy, math
import array as a
import edge
import contrast
#change references

#we are going to assume that q is out image, for the start, I will use a raw captured image to test
#after the test, the code will be modified to work as intended

#DO NOT FORGET TO REMOVE ERROR CHECKING PARTS OF CODE!!!
x = cv2.VideoCapture()
#q = contrast.main()
k = []
#k = q #q is name of working frame passed from module, need to change name
#this section converts frame to usable list
def afunction(k):
	p = []
	for array in k:
		#p.append(array)
		p = array
		#print p	#this is for error checking
	return p

#run convert.afunction(k)

