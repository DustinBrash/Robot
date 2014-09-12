#! /usr/local/bin/python
#this is the contrast script
import cv, cv2, math

def demo():
	x = raw_input('file_location:')
	myimage = cv2.imread(x, cv2.CV_LOAD_IMAGE_GRAYSCALE)
	return myimage

myimage = demo()
def equ(myimage):
	myhist = cv2.equalizeHist(myimage)
	return myhist

myhist = equ(myimage)
y = raw_input('new_file_name:')
cv2.imwrite(y, myhist)

