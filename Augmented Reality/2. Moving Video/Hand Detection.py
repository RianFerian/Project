import cv2
import time
import mediapipe as mp

# Repository
# https://github.com/google/mediapipe/blob/master/docs/solutions/hands.md

# Install package
# cd /d d:\users\rian.ferian\appdata\local\programs\python\python311 python.exe -m pip install mediapipe

# Take video from camera
cap = cv2.VideoCapture(0)

# import mediapipe library function
# Package detect hand palm
mpHands = mp.solutions.hands
hands = mpHands.Hands()
# Visualize the result
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    # Convert color from BGR to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(result.multi_hand_landmarks)

    # Detect if there is any hand landmarks
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            # Visualize every hand landmarks
            for id, lm in enumerate(handLms.landmark):
                # Heigh and Width
                h, w, c = img.shape
                # Create the coordinate
                cx, cy = int(lm.x*w), int(lm.y*h)
                if id == 8:
                    cv2.circle(img, (cx,cy), 15, (255, 0, 255), cv2.FILLED)

            # # Draw landmarks
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Img", img)
    cv2.waitKey(1)