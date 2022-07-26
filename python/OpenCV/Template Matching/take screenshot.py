import cv2
import mss
import numpy as np

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
