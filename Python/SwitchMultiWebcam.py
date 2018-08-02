'''
v1.2
Switch multi USB webcam
Jay Kim

'''

import cv2
x = 0
cap = cv2.VideoCapture(x)
while True:
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    key = cv2.waitKey(1) & 0xFF == ord('q')
    if key == ord('q'):
        break
    elif key == ord('t'):
        if x == 0:
            x = 1
            cap = cv2.VideoCapture(1)
        elif x== 1:
            x = 0
            cap = cv2.VideoCapture(0)
            
cap.release()
cv2.destroyAllWindows()
