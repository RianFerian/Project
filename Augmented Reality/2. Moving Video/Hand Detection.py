import cv2
import time
import numpy as np

wCam, hCam = 648, 480


cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 8

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS:{int(fps)}', (40, 58), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    
    cv2.imshow("Img", img)
    cv2.waitKey(1)