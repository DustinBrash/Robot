#! /usr/local/bin/python
import cv, cv2
import numpy as np

x = cv2.VideoCapture()
device = 0 #this is the default device, assumes there are no other camera devices conected to computer

def myfunction():
	x.open(device)
	#a = x.isOpened
	#if(a(device) == False):		
	#	x.open(device)
	#elif(a(device) == True):
	#	q = x.read(device)
	#	q
	q = x.read(device)
	q	
	print q
	return q

myfunction()
#ALWAYS REMEMBER TO HAVE X.RELEASE() AFTER CALLING A SINGLE VIDEO CAPTURE INSTANCE!!!!
x.release()

