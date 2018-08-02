'''
v1.1
Display single USB webcam
Jay Kim

'''
import cv2
import numpy as np
cap1 = cv2.VideoCapture(0)
while True:
    ret1, frame1 = cap1.read()
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image', frame1)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap1.release()
cv2.destroyAllWindows()
