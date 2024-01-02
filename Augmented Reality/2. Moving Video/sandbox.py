import numpy as np
import pyautogui

# Smoothening
wCam, hCam = 640, 480
frameR = 100
smoothening = 7
plocX, plocY = 0, 0
clocX, clocY = 0, 0
wScr, hScr = pyautogui.size()

x1 = 300
x2 = 330
x5 = np.interp(x1, (100, 640 - 100), (0,1366))
x6 = np.interp(x2, (100, 640 - 100), (0,1366))

clocX = (x5 - x6) / smoothening

print(x5, x6, clocX)


# Lokasi sebelumnya + (lokasi sekarang - lokasi sebelum)/smoothening
# 