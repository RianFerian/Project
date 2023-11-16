import cv2
import time
import mediapipe as mp
import HandTrackingModule as htm
import math
import pyautogui

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()

# Index finger location
IndexFinger = [0, 0]

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    # Output
    lmList = detector.findPosition(img)
    # ID and tracker
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        # Each finger position 4 thumb 8 index
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        # Index and middle finger
        x3, y3 = lmList[8][1], lmList[12][2]
        
        # Middle position
        cx, cy = (x1+x2)//2, (y1+y2)//2

        # Draw circle and line
        cv2.circle(img, (x1,y1), 10, (255,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (255,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,255), 3)
        cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)
        
        # Length for thumb and index finger
        length_thumb_index = math.hypot(x2 - x1, y2 - y1)
        # print(length)

        # Length for index and middle finger
        length_index_middle = math.hypot(x3-x2, y3-y2)
        print(length_index_middle)

        # Is the fingers was up?
        fingersUp = detector.fingersUp(lmList)

        # Get the position of the mouse
        mouseX, mouseY = pyautogui.position()
        print(mouseX, mouseY)

        # if the fingers was up
        if fingersUp:
            if length_index_middle < 10:
                # Index finger location - new index finger location
                if len(IndexFinger)>0:
                    movementX, movementY = IndexFinger[0] - lmList[4][1], IndexFinger[1] - lmList[4][2]
                    # print(movementX, movementY)

                    try:
                        pyautogui.move((movementX * 2), (movementY * -2))
                    except pyautogui.FailSafeException as e:
                        print(f"Fail-safe triggered: {e}")
            
            # # if the length thumb and index was less than 40 show a green circle
            # if length_thumb_index < 40:
            #     cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)
            
            # Update index finger location            
            IndexFinger[0], IndexFinger[1] = lmList[4][1], lmList[4][2]
                
        

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Flip the frame horizontally
    img = cv2.flip(img, 1)  # 1 denotes horizontal flip
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)