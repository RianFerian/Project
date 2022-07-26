import cv2
import mss
import pyautogui
import numpy as np
import keyboard
import time
import os
import pydirectinput

SCT = mss.mss()
def main_screen(height=800):
    scr = SCT.grab({
                'left': 250,
                'top': 180,
                'width': 800,
                'height': height
            })
    img = np.array(scr)
    return cv2.cvtColor(img, cv2.IMREAD_COLOR)

while True:
    color = main_screen()
    cv2.imshow("input", color)

    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

#pig_barn_img = cv2.imread('PigBarn.png', cv2.IMREAD_UNCHANGED)
#sheep_barn_img = cv2.imread('SheepBarn.png', cv2.IMREAD_UNCHANGED)
#cow_barn_img = cv2.imread('CowBarn.png', cv2.IMREAD_UNCHANGED)

#result_pig = cv2.matchTemplate(color, pig_barn_img, cv2.TM_CCOEFF_NORMED)
#result_sheep = cv2.matchTemplate(color, sheep_barn_img, cv2.TM_CCOEFF_NORMED)
#result_cow = cv2.matchTemplate(color, cow_barn_img, cv2.TM_CCOEFF_NORMED)

