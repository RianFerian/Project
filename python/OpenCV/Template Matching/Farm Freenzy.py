import cv2
import mss
import pyautogui
import numpy as np
import keyboard
import time
import os
import pydirectinput

dirname = os.path.dirname(__file__)
animal_path = os.path.join(dirname, 'animals')
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

    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

    # pig barn image
    pig_barn_img = cv2.imread('CowBarn.png', cv2.IMREAD_UNCHANGED)
    #sheep_barn_img = cv2.imread('SheepBarn.png', cv2.IMREAD_UNCHANGED)
    #cow_barn_img = cv2.imread('CowBarn.png', cv2.IMREAD_UNCHANGED)

    # match pig barn
    result_pig = cv2.matchTemplate(color, pig_barn_img, cv2.TM_CCOEFF_NORMED)
    #result_sheep = cv2.matchTemplate(color, sheep_barn_img, cv2.TM_CCOEFF_NORMED)
    #result_cow = cv2.matchTemplate(color, cow_barn_img, cv2.TM_CCOEFF_NORMED)

    # min_val, max_val, min_loc, max_loc
    _, max_val_pig, _, max_loc_pig = cv2.minMaxLoc(result_pig)
    #_, max_val_sheep, _, max_loc_sheep = cv2.minMaxLoc(result_pig)
    #_, max_val_cow, _, max_loc_cow = cv2.minMaxLoc(result_pig)

    print(max_val_pig)

    # Threshold
    if max_val_pig > .2:
        #Draw Rectangle
        cv2.rectangle(color, max_loc_pig, (max_loc_pig[0] + 100, max_loc_pig[1] + 100), (0, 0, 255), 2)




    cv2.imshow("input", color)



#pig_barn_img = cv2.imread('PigBarn.png', cv2.IMREAD_UNCHANGED)
#sheep_barn_img = cv2.imread('SheepBarn.png', cv2.IMREAD_UNCHANGED)
#cow_barn_img = cv2.imread('CowBarn.png', cv2.IMREAD_UNCHANGED)

#result_pig = cv2.matchTemplate(color, pig_barn_img, cv2.TM_CCOEFF_NORMED)
#result_sheep = cv2.matchTemplate(color, sheep_barn_img, cv2.TM_CCOEFF_NORMED)
#result_cow = cv2.matchTemplate(color, cow_barn_img, cv2.TM_CCOEFF_NORMED)

