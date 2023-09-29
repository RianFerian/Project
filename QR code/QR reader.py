import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('QR code\img1.png')

cap = cv2.VideoCapture(0)

while True:

    sucess, img = cap.read()
    for barcode in decode(img):
        print(barcode.data)
        myData = barcode.data.decode('utf-8')
    
    cv2.imshow('Result', img)
    cv2.waitKey(1)


