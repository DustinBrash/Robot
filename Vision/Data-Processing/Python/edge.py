import cv2, math
import numpy as np
from cv2 import cv

def find_edge(im):
	#Noise Reduction
	im_blurred = cv2.GaussianBlur(im, (5, 5), 0)
	#Edge Detection
	edges = cv2.Canny(im_blurred, 1, 200)
	return edges

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
	edges = find_edge(gray)
	edges = blur_edges(edges)
	lines = get_lines(edges, 80)
	return (lines)

def main():
	cap = cv2.VideoCapture(0)
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		# Our operations on the frame come here
		lines = get_frames(frame)
		# Display the resulting frame
        
		try:
			add_lines(frame, lines)
		except TypeError:
			print 'No straight lines detected'
			pass
		cv2.imshow('lol', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		#print lines
	cap.release()
	cv2.destroyAllWindows()
	return lines

main()

#change get_frames to not make frames in program
