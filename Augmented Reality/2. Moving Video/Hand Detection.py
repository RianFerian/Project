import cv2
import time
import mediapipe as mp

# cd /d d:\users\rian.ferian\appdata\local\programs\python\python311 python.exe -m pip install mediapipe

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()

while True:
    success, img = cap.read()

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f'FPS:{int(fps)}', (40, 58), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)
    
    cv2.imshow("Img", img)
    cv2.waitKey(1)