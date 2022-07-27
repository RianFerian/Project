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

pig_barn = None
sheep_barn = None
cow_barn = None

pig = [cv2.imread(os.path.join(animal_path, 'Pig.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'PigRev.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'PigSkin.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'PigSpecial.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'PigSpecialRev.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'PigSkinSpecial.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'PigSkinSpecialRev.jpg'), cv2.IMREAD_UNCHANGED)
       ]

sheep = [cv2.imread(os.path.join(animal_path, 'Sheep.jpg'), cv2.IMREAD_UNCHANGED),
         cv2.imread(os.path.join(animal_path, 'SheepRev.jpg'), cv2.IMREAD_UNCHANGED),
         cv2.imread(os.path.join(animal_path, 'SheepSkin.jpg'), cv2.IMREAD_UNCHANGED),
         cv2.imread(os.path.join(animal_path, 'SheepSkinRev.jpg'), cv2.IMREAD_UNCHANGED)
         ]

cow = [cv2.imread(os.path.join(animal_path, 'Cow.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'CowRev.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'CowSkin.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'CowSkinRev.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'CowSpecialRev.jpg'), cv2.IMREAD_UNCHANGED),
       cv2.imread(os.path.join(animal_path, 'CowSpecial.jpg'), cv2.IMREAD_UNCHANGED),
       ]


def detect_animal(animal):
    result_animal = cv2.matchTemplate(color, animal, cv2.TM_CCOEFF_NORMED)
    _, max_val_animal, _, max_loc_animal = cv2.minMaxLoc(result_animal)
    if max_val_animal > .8:
        # Return animal location
        return max_loc_animal
    else:
        return None

def main_screen(height=500):
    scr = SCT.grab({
                'left': 250,
                'top': 180,
                'width': 600,
                'height': height
            })
    img = np.array(scr)
    return cv2.cvtColor(img, cv2.IMREAD_COLOR)


def detect_barn(pig_barn, sheep_barn, cow_barn):
    # pig barn image
    pig_barn_img = cv2.imread('PigBarn.jpg', cv2.IMREAD_UNCHANGED)
    sheep_barn_img = cv2.imread('SheepBarn2.jpg', cv2.IMREAD_UNCHANGED)
    cow_barn_img = cv2.imread('CowBarn.jpg', cv2.IMREAD_UNCHANGED)

    # match pig barn
    result_pig = cv2.matchTemplate(color, pig_barn_img, cv2.TM_CCOEFF_NORMED)
    result_sheep = cv2.matchTemplate(color, sheep_barn_img, cv2.TM_CCOEFF_NORMED)
    result_cow = cv2.matchTemplate(color, cow_barn_img, cv2.TM_CCOEFF_NORMED)

    # min_val, max_val, min_loc, max_loc
    _, max_val_pig, _, max_loc_pig = cv2.minMaxLoc(result_pig)
    _, max_val_sheep, _, max_loc_sheep = cv2.minMaxLoc(result_sheep)
    _, max_val_cow, _, max_loc_cow = cv2.minMaxLoc(result_cow)

    # Treshold 95%
    if max_val_pig > .95:
        pig_barn = max_loc_pig
    if max_val_sheep > .95:
        sheep_barn = max_loc_sheep
    if max_val_cow > .95:
        cow_barn = max_loc_cow

    # Output barn location
    return pig_barn, sheep_barn, cow_barn

def Put_Away(animal_name, animals, location):
    print(f"Checking for {animal_name}....")
    keep_testing = True
    while keep_testing:
        for animal in animals:
            animal_loc = detect_animal(animal)
            if animal_loc is not None:
                pyautogui.moveTo(animal_loc[0] + 250 + 20, animal_loc[1] + 180 + 10)
                pydirectinput.mouseDown()
                pydirectinput.moveTo(location[0] + 250, location[1] + 180 + 10, duration=.1)
                pydirectinput.mouseUp()
                return True
            else:
                keep_testing = False
    return False



while True:
    color = main_screen()

    # Press "q" to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

    if pig_barn == None and sheep_barn == None and cow_barn == None:
        pig_barn, sheep_barn, cow_barn = detect_barn(pig_barn, sheep_barn, cow_barn)

    cv2.imshow("input", color)

    if keyboard.is_pressed('3'):
        found = Put_Away("Pig", pig, pig_barn)
    if keyboard.is_pressed('2'):
        found = Put_Away("Sheep", sheep, sheep_barn)
    if keyboard.is_pressed('1'):
        found = Put_Away("Cow", cow, cow_barn)


    #print(max_val_pig)

    # Threshold
    #if max_val_pig > .95:
        #Draw Rectangle
        #cv2.rectangle(color, max_loc_pig, (max_loc_pig[0] + 100, max_loc_pig[1] + 100), (0, 0, 255), 2)





#pig_barn_img = cv2.imread('PigBarn.png', cv2.IMREAD_UNCHANGED)
#sheep_barn_img = cv2.imread('SheepBarn.png', cv2.IMREAD_UNCHANGED)
#cow_barn_img = cv2.imread('CowBarn.png', cv2.IMREAD_UNCHANGED)

#result_pig = cv2.matchTemplate(color, pig_barn_img, cv2.TM_CCOEFF_NORMED)
#result_sheep = cv2.matchTemplate(color, sheep_barn_img, cv2.TM_CCOEFF_NORMED)
#result_cow = cv2.matchTemplate(color, cow_barn_img, cv2.TM_CCOEFF_NORMED)

