import cv2, math
import numpy as np
from cv2 import cv

#Noise Reduction
def find_edge(im):
    im_blurred = cv2.GaussianBlur(im, (5, 5), 0)
    #Edge Detection
    edges = cv2.Canny(im_blurred, 100, 200)
    return edges

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('Window', find_edge(gray))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()



