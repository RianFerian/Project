import cv2
import time
import mediapipe as mp

# cd /d d:\users\rian.ferian\appdata\local\programs\python\python311 python.exe -m pip install mediapipe

cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms)



    cv2.imshow("Img", img)
    cv2.waitKey(1)