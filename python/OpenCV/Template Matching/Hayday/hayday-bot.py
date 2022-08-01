import cv2
import mss
import numpy as np
import os
import pyautogui
import pydirectinput
import time
import schedule

SCT = mss.mss()
dirname = os.path.dirname(__file__)
field_path = os.path.join(dirname, 'picture')

# LOAD IMAGE SOURCE
wheat_img = cv2.imread(os.path.join(field_path, 'wheat7.jpg'), cv2.IMREAD_UNCHANGED)
celurit_img = cv2.imread(os.path.join(field_path, 'celurit.jpg'), cv2.IMREAD_UNCHANGED)
empty_field_img = cv2.imread(os.path.join(field_path, 'field.jpg'), cv2.IMREAD_UNCHANGED)
raw_wheat_img = cv2.imread(os.path.join(field_path, 'raw wheat.jpg'), cv2.IMREAD_UNCHANGED)
market_img = cv2.imread(os.path.join(field_path, 'market.jpg'), cv2.IMREAD_UNCHANGED)
store_img = cv2.imread(os.path.join(field_path, 'store.jpg'), cv2.IMREAD_UNCHANGED)
store_wheat_img = cv2.imread(os.path.join(field_path, 'store wheat.jpg'), cv2.IMREAD_UNCHANGED)
max_value_img = cv2.imread(os.path.join(field_path, 'max value.jpg'), cv2.IMREAD_UNCHANGED)
sell_img = cv2.imread(os.path.join(field_path, 'sell.jpg'), cv2.IMREAD_UNCHANGED)
newspaper_img = cv2.imread(os.path.join(field_path, 'newspaper.jpg'), cv2.IMREAD_UNCHANGED)
money_img = cv2.imread(os.path.join(field_path, 'money.jpg'), cv2.IMREAD_UNCHANGED)
sold_img = cv2.imread(os.path.join(field_path, 'sold.jpg'), cv2.IMREAD_UNCHANGED)
close_market_img = cv2.imread(os.path.join(field_path, 'close market.jpg'), cv2.IMREAD_UNCHANGED)

# LOAD SCREEN
def main_screen(height=900):
    scr = SCT.grab({
                'left': 250,
                'top': 100,
                'width': 1400,
                'height': height
            })
    img = np.array(scr)
    return cv2.cvtColor(img, cv2.IMREAD_COLOR)

# MAKE IMAGE DETECTOR, output = location
def image_detector(color, field_image):
    #match the field
    field_result = cv2.matchTemplate(color, field_image, cv2.TM_CCOEFF_NORMED)

    _, max_val, _, max_loc = cv2.minMaxLoc(field_result)

    #print(max_val)

    threshold = 0.75
    if max_val >= threshold:
        return max_loc
    else:
        None





def panen_gandum():
    print("executed panen gandum")

    #  # While loop for 60 second panen gandumw2dddd
    t_end = time.time() + 50
    while time.time() < t_end:
        color = main_screen()
        # take every location for the field detected
        field_loc = image_detector(color, wheat_img)

        # Draw Rectangle
        # Panen
        if field_loc != None:
            pyautogui.moveTo(field_loc[0] + 250 + 20, field_loc[1] + 100 + 10, duration=0.1)
            pydirectinput.click()
            time.sleep(2)
            color = main_screen()
            celurit_loc = image_detector(color, celurit_img)
            if celurit_loc != None:
                pyautogui.moveTo(celurit_loc[0] + 250 + 20, celurit_loc[1] + 100 + 10, duration=0.1)
                pydirectinput.mouseDown()
                pyautogui.moveTo(field_loc[0] + 250 + 20, field_loc[1] + 100 + 10, duration=0.1)
                pydirectinput.mouseUp()

                # for pt in zip(*field_loc[::-1]):
                # cv2.rectangle(color, pt, (pt[0] + 100, pt[1] + 100), (0, 0, 255), 2)
        cv2.imshow("input", color)
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break


    # TANAM GANDUM
    t_end = time.time() + 50
    while time.time() < t_end:
        color = main_screen()

        # take every location for the field detected
        empty_field_loc = image_detector(color, empty_field_img)

        # Tanam
        if empty_field_loc != None:
            pyautogui.moveTo(empty_field_loc[0] + 250 + 30, empty_field_loc[1] + 100 + 30, duration=0.1)
            pydirectinput.click()
            time.sleep(1)
            color = main_screen()
            wheat_loc = image_detector(color, raw_wheat_img)
            if wheat_loc != None:
                pyautogui.moveTo(wheat_loc[0] + 250 + 10, wheat_loc[1] + 100 + 10, duration=0.1)
                pydirectinput.mouseDown()
                pyautogui.moveTo(empty_field_loc[0] + 250 + 30, empty_field_loc[1] + 100 + 25, duration=0.1)
                pydirectinput.mouseUp()

        cv2.imshow("input", color)
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

def jual_barang():
    print("executed jual barang")
    t_end = time.time() + 20
    while time.time() < t_end:
        color = main_screen()

        # take every location for the field detected
        market_loc = image_detector(color, market_img)

        # Jual
        if market_loc != None:
            pyautogui.moveTo(market_loc[0] + 250 + 20, market_loc[1] + 100 + 10, duration=0.1)
            pydirectinput.click()
            time.sleep(1)

            t_end = time.time() + 10
            while time.time() < t_end:
                color = main_screen()
                store_loc = image_detector(color, store_img)
                if store_loc != None:
                    pyautogui.moveTo(store_loc[0] + 250 + 10, store_loc[1] + 100 + 10, duration=0.1)
                    pydirectinput.click()
                    time.sleep(.5)

                    color = main_screen()
                    store_wheat_loc = image_detector(color, store_wheat_img)
                    if store_wheat_loc != None:
                        pyautogui.moveTo(store_wheat_loc[0] + 250 + 10, store_wheat_loc[1] + 100 + 10, duration=0.1)
                        pydirectinput.click()

                        color = main_screen()
                        max_value_loc = image_detector(color, max_value_img)
                        if max_value_loc != None:
                            pyautogui.moveTo(max_value_loc[0] + 250 + 10, max_value_loc[1] + 100 + 10, duration=0.1)
                            pydirectinput.click()

                            # Newspaper
                            newspaper_loc = image_detector(color, newspaper_img)
                            if newspaper_loc != None:
                                pyautogui.moveTo(newspaper_loc[0] + 250 + 20, newspaper_loc[1] + 100 + 25, duration=0.1)
                                pydirectinput.click()

                            sell_loc = image_detector(color, sell_img)
                            if sell_loc != None:
                                pyautogui.moveTo(sell_loc[0] + 250 + 10, sell_loc[1] + 100 + 10, duration=0.1)
                                pydirectinput.click()

            close_market_loc = image_detector(color, close_market_img)
            if close_market_loc != None:
                pyautogui.moveTo(close_market_loc[0] + 250 + 10, close_market_loc[1] + 100 + 10, duration=0.1)
                pydirectinput.click()

        cv2.imshow("input", color)
        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

def take_money():
    print("executed take money")
    t_end = time.time() + 15
    while time.time() < t_end:
        color = main_screen()

        # OPEN MARKET WHILE SOMETHING SOLDED
        market_sold_loc = image_detector(color, money_img)
        if market_sold_loc != None:
            pyautogui.moveTo(market_sold_loc[0] + 250 + 10, market_sold_loc[1] + 100 + 10, duration=0.1)
            pydirectinput.click()

            # TAKE MONEY FROM SOLDED WHEAT
            t_end = time.time()+10
            while time.time() < t_end:
                color = main_screen()
                solded_loc = image_detector(color, sold_img)
                if solded_loc != None:
                    pyautogui.moveTo(solded_loc[0] + 250 + 10, solded_loc[1] + 100 + 10, duration=0.1)
                    pydirectinput.click()



            # CLOSING THE MARKET STORE
            close_market_loc = image_detector(color, close_market_img)
            if close_market_loc != None:
                pyautogui.moveTo(close_market_loc[0] + 250 + 10, close_market_loc[1] + 100 + 10, duration=0.1)
                pydirectinput.click()



schedule.every(2.2).minutes.do(panen_gandum)
schedule.every(5).minutes.do(jual_barang)
schedule.every(2).minutes.do(take_money)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(1)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break

# panen_gandum()
# jual_barang()
# take_money()
#
# while True:
#     color = main_screen()
#     image_detector(color, close_market_img)
#
#     cv2.imshow("input", color)
#     # Press "q" to quit
#     if cv2.waitKey(25) & 0xFF == ord("q"):
#         cv2.destroyAllWindows()
#         break



