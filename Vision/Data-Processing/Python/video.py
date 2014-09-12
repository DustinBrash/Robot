import cv2
x = cv2.VideoCapture()
def video():
    x.open(0)
    while(True):
        ret, frame = x.read()
        cv2.imshow('frame', frame)
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    x.release()
    return frame

