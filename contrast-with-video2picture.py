#! /usr/local/bin/python
#this is the contrast script
import cv2, math
import numpy as np
from cv2 import cv


def calcHistograph(q):
        channels = [0,1] #this seciton of commented code did not work so it was isolated from program
        mask = None
        histsize = [30, 32]
        ranges = [0, 256]
        myimage = cv2.calcHist(q, channels, mask, histsize, ranges)
        return myimage

def find_edge(im):
        #Noise Reduction
        im_blurred = cv2.GaussianBlur(im, (5, 5), 0)
        #Edge Detection
        edges = cv2.Canny(im_blurred, 1, 200)
        return edges

def equ(myimage):
        myhist = cv2.equalizeHist(myimage)
        return myhist

def get_lines(img, threshold = 1):
        theta = math.pi / 180
        rho = 1
        return cv2.HoughLinesP(img, rho, theta, threshold)

def add_lines(img, lines):
        color = (0, 0, 255)
        for line in lines:
            for l in line:
                cv2.line(img, (l[0], l[1]), (l[2], l[3]), color)

im = cv2.imread('program_image.jpg')
gray= cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
edges = find_edge(gray)
lines = get_lines(edges, 75)
add_lines(im, lines)
cv2.imshow('Segment', im)
cv2.waitKey(0)

