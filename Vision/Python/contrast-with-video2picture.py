#! /usr/local/bin/python
#this is the contrast script
import cv2, math
import numpy as np
from cv2 import cv

x = cv2.VideoCapture()
device = 0 #this is the default device, assumes there are no other camera devices conected to computer
x.open(device)

def myfunction(x):
        ret, q = x.read()       
        return cv2.cvtColor(q, cv2.COLOR_BGR2GRAY), q

q = myfunction(x)
#ALWAYS REMEMBER TO HAVE X.RELEASE() AFTER CALLING A SINGLE VIDEO CAPTURE INSTANCE!!!!
x.release()

#now we will be working with histographic equalization


def calcHistograph(q):
        channels = [0,1] #this seciton of commented code did not work so it was isolated from program
        mask = None
        histsize = [30, 32]
        ranges = [0, 256]
        myimage = cv2.calcHist(q, channels, mask, histsize, ranges)
        return myimage


def equ(myimage):
        myhist = cv2.equalizeHist(myimage)
        return myhist


myhist = equ(myimage)
cv2.imshow(cv2.cvtColor(myimage, 0))
cv2.waitKey(0)

