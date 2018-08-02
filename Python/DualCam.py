'''
v1.3
Display dual USB webcam
Jay Kim

'''

import cv2
import numpy as np
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', 640, 300)

    frame3 = np.hstack((frame1, frame2))
    cv2.imshow('image', frame3)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
