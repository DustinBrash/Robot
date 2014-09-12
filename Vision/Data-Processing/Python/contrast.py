import cv2, math
import numpy as np
from cv2 import cv


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
            cv2.line(img, (l[0], l[1]), (l[2], l[3]), color, 3)   

def blur_edges(edges):
    edges_blurred = cv2.GaussianBlur(edges, (3, 3), 0)
    return edges_blurred

def get_frames(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hist = equ(gray)
    edges = find_edge(gray)
    edges = blur_edges(edges)
    lines = get_lines(edges, 80)
    return (lines, hist)

def main():
    cap = cv2.VideoCapture(0)
    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()
        # Our operations on the frame come here
        lines, contrast = get_frames(frame)
        # Display the resulting frame
        
#        try:
#            image = equ(frame)
#        except TypeError:
#            print 'No straight lines detected'
        cv2.imshow('lol', contrast)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
#    print lines
    cap.release()
    cv2.destroyAllWindows()
    return contrast
#change get_frames to not make frames in program
