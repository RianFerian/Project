import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser
import time
# from selenium import webdriver
# import asyncio

# img = cv2.imread('QR code\img1.png')

cap = cv2.VideoCapture(0)


while True:

    sucess, img = cap.read()
    for barcode in decode(img):

        # # Create Polylines
        # pts = np.array([barcode.polygon], np.int32)
        # pts = pts.reshape((-1,1,2))
        # cv2.polylines(img, [pts], True, (255,0,255), 5)

        # Decode URL
        myData = barcode.data.decode('utf-8')
        
        # driver.get(myData)
        webbrowser.open_new(myData)

        # # Create Polylines
        # pts = np.array([barcode.polygon], np.int32)
        # pts = pts.reshape((-1,1,2))
        # cv2.polylines(img, [pts], True, (255,0,255), 5)

        time.sleep(10)
        
    cv2.imshow('Result', img)
    cv2.waitKey(1)

# # Asynchronous function to open URL in the background
# async def open_url_in_background(myData):
#     webbrowser.open_new(myData)
#     await asyncio.sleep(15)  # Simulate a non-blocking delay


# # Asynchronous function to process frames
# async def process_frames():
#     while True:
#         success, img = cap.read()
#         # Process barcodes asynchronously
#         barcodes = decode(img)
#         tasks = [open_url_in_background(barcode.data.decode('utf-8')) for barcode in barcodes]
#         await asyncio.gather(*tasks)
#         # Draw polylines and display the frame
#         for barcode in barcodes:
#             pts = np.array([barcode.polygon], np.int32)
#             pts = pts.reshape((-1, 1, 2))
#             cv2.polylines(img, [pts], True, (255, 0, 255), 5)
#         cv2.imshow('Result', img)
#         cv2.waitKey(1)


# # Run the asynchronous event loop
# async def main():
#     # Start processing frames asynchronously
#     await process_frames()

# # Run the event loop with the main() function
# asyncio.run(main())