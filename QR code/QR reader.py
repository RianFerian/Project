import cv2
# import numpy as np
from pyzbar.pyzbar import decode
import webbrowser
import time

# Take the video
cap = cv2.VideoCapture(0)


while True:

    sucess, img = cap.read()
    for barcode in decode(img):

        # Create Polylines
        # pts = np.array([barcode.polygon], np.int32)
        # pts = pts.reshape((-1,1,2))
        # cv2.polylines(img, [pts], True, (255,0,255), 5)

        # Decode URL
        myData = barcode.data.decode('utf-8')
        
        # Execute the URL
        webbrowser.open_new(myData)

        # # Time for executing
        time.sleep(10)
        
    cv2.imshow('Result', img)
    cv2.waitKey(1)