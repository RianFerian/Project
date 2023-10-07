import cv2
from pyzbar.pyzbar import decode
import webbrowser
import time

# Take the video
cap = cv2.VideoCapture(0)

while True:

    sucess, img = cap.read()
    for barcode in decode(img):

        # Decode URL
        myData = barcode.data.decode('utf-8')
        
        # Execute the URL
        webbrowser.open_new(myData)

        # # Time for executing
        time.sleep(3)
        
    cv2.imshow('Result', img)
    cv2.waitKey(1)