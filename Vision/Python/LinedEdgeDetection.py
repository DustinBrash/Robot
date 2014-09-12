import cv2, math
import numpy as np
from cv2 import cv


def find_edge(im):
    #Noise Reduction
    im_blurred = cv2.GaussianBlur(im, (5, 5), 0)
    #Edge Detection
    edges = cv2.Canny(im_blurred, 1, 200)
    return edges

    
    
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

def get_lines(img, threshold = 1, polar = False): 
    theta = math.pi / 180
    rho = 1
    return cv2.HoughLinesP(img, rho, theta, threshold, minLineLength = 20, maxLineGap = 5)
    

def add_lines(img, lines):
    color = (0, 0, 255)
    for line in lines:
        for l in line:
            cv2.line(img, (l[0], l[1]), (l[2], l[3]), color, 1)   


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist = equ(gray)
    edges = find_edge(gray)
    lines = get_lines(edges, 80)
    add_lines(frame, lines)
    # Display the resulting frame
    cv2.imshow('Contrast', lines)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



