import cv2
import time
import mediapipe as mp
import HandTrackingModule as htm
import math
import pyautogui

pTime = 0
cTime = 0

# Take the video
cap = cv2.VideoCapture(0)
# Load hand tracking Module
detector = htm.handDetector()

# Index finger location
IndexFinger = [0, 0]

# Mouse Status
Mouse_Clicked = False

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=True)
    # Output
    lmList = detector.findPosition(img)
    # ID and tracker
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])

        # Position for thumb finger 
        x1, y1 = lmList[4][1], lmList[4][2]
        # Index finger position
        x2, y2 = lmList[8][1], lmList[8][2]
        # middle finger postition
        x3, y3 = lmList[12][1], lmList[12][2]
        # Pinky MCP finger position
        x4, y4 = lmList[17][1], lmList[17][2]


        # # Middle position thumb and pinky MCP
        cx, cy = (x1+x4)//2, (y1+y4)//2

        # # Draw circle and line
        # cv2.circle(img, (x1,y1), 10, (255,0,255), cv2.FILLED)
        # cv2.circle(img, (x2,y2), 10, (255,0,255), cv2.FILLED)
        # cv2.line(img, (x1,y1), (x4,y4), (255,0,255), 3)
        # cv2.circle(img, (cx,cy), 10, (255,0,255), cv2.FILLED)
        
        # Length for thumb and Pinky MCP 
        length_thumb_pinky = math.hypot(x4 - x1, y4 - y1)
        # print(length)

        # Length for index and middle finger
        length_index_middle = math.hypot(x3-x2, y3-y2)
        # print(length_index_middle)

        # Is the fingers was up?
        fingersUp = detector.fingersUp(lmList)

        # Get the position of the mouse
        mouseX, mouseY = pyautogui.position()
        # print(mouseX, mouseY)

        # if the fingers was up
        if fingersUp:
            if length_index_middle < 10:
                # Index finger location - new index finger location
                if len(IndexFinger)>0:
                    movementX, movementY = IndexFinger[0] - x2, IndexFinger[1] - y2
                    # print(movementX, movementY)

                    try:
                        pyautogui.move((movementX * 3), (movementY * -3))
                    except pyautogui.FailSafeException as e:
                        print(f"Fail-safe triggered: {e}")
            
            # # if the length thumb and index was less than 40 show a green circle
            # if length_thumb_index < 40:
            #     cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)
                        
            
            # Update index finger location            
            IndexFinger[0], IndexFinger[1] = x2, y2
            
            if length_thumb_pinky<40 and Mouse_Clicked == False:
                try: 
                    pyautogui.mouseDown()
                    print("Mouse Down")
                    Mouse_Clicked = True
                    print(Mouse_Clicked)
                except pyautogui.FailSafeException as e:
                    print(f"Fail-safe triggered: {e}")
            if length_thumb_pinky>40 and Mouse_Clicked == True:
                try:
                    pyautogui.mouseUp()
                    print("Mouse Up")
                    Mouse_Clicked = False
                    print(Mouse_Clicked)
                except pyautogui.FailSafeException as e:
                        print(f"Fail-safe triggered: {e}")


    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # Flip the frame horizontally
    img = cv2.flip(img, 1)  # 1 denotes horizontal flip
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)