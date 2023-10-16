import cv2
import numpy as np

cap = cv2.VideoCapture(0)
imgTarget = cv2.imread('D:\\Users\\rian.ferian\\Desktop\\Project\\Augmented Reality\\1. Code detection\\Kiwi Bird.jpg')
myVid = cv2.VideoCapture('D:\\Users\\rian.ferian\\Desktop\\Project\\Augmented Reality\\1. Code detection\\Kiwi!.mp4')

detection = False
frameCounter = 0

# Read the video
success, imgVideo = myVid.read()
# Take height, width of the target image and resize the video
_, frame = cap.read()
hT,wT,_ = frame.shape
imgVideo = cv2.resize(imgVideo, (wT, hT))
imgTarget = cv2.resize(imgTarget, (wT, hT))

# Make a key point using orb
orb = cv2.ORB_create(nfeatures=1000)
# Generate image orb
kp1, des1 = orb.detectAndCompute(imgTarget, None)
# # Draw the key points in the image
# imgTarget = cv2.drawKeypoints(imgTarget, kp1, None)

while True:
    # Take the video from webcam
    sucess, imgWebcam = cap.read()
    imgAug = imgWebcam.copy()
    imgWarp = imgWebcam.copy()

    # Generate webcam orb
    kp2, des2 = orb.detectAndCompute(imgWebcam, None)

    if detection == False:
        myVid.set(cv2.CAP_PROP_POS_FRAMES,0)
        frameCounter = 0
    else:
        if frameCounter == myVid.get(cv2.CAP_PROP_FRAME_COUNT):
            myVid.set(cv2.CAP_PROP_POS_FRAMES,0)
            frameCounter = 0
        success, imgVideo = myVid.read()
        imgVideo = cv2.resize(imgVideo, (wT, hT))

    # Matcher
    bf = cv2.BFMatcher()
    # Using brute force matches for des1 and des2
    matches = bf.knnMatch(des1, des2, k=2)
    good = []
    for m,n in matches:
        if m.distance < 0.75 * n.distance:
            good.append(m)
    # print(len(good))
    imgFeatures = cv2.drawMatches(imgTarget, kp1, imgWebcam, kp2, good, None, flags=2)

    # Homograph calculation
    if len(good) > 20:
        detection = True
        # Source
        srcPts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
        # Destination
        dstPts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)
        
        # Create the shape over the image
        matrix, mask = cv2.findHomography(srcPts, dstPts, cv2.RANSAC, 5)
        pts = np.float32([[0,0], [0,hT], [wT,hT], [wT,0]]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,matrix)
        img2 = cv2.polylines(imgWebcam, [np.int32(dst)], True, (255,0,255), 3)

        # Take the shape and replace the image with video
        imgWarp = cv2.warpPerspective(imgVideo, matrix, (imgWebcam.shape[1], imgWebcam.shape[0]))
        # Take the shape and fill with white
        maskNew = np.zeros((imgWebcam.shape[0], imgWebcam.shape[1]), np.uint8)
        cv2.fillPoly(maskNew, [np.int32(dst)], (255,255,255))
        # Invert the shape
        maskInv = cv2.bitwise_not(maskNew)
        # Mask the inverted shape with the webcam image
        imgAug = cv2.bitwise_and(imgAug, imgAug ,mask = maskInv)
        # Insert the video into masked area
        imgAug = cv2.bitwise_or(imgWarp, imgAug)
        
    cv2.imshow('masked', imgAug)
    cv2.imshow('imgWarp', imgWarp)
    # cv2.imshow('img2', img2)
    # # Show image features
    cv2.imshow('Img Features', imgFeatures)
    # # Show Image Target
    # cv2.imshow('Img Target', imgTarget)
    # # Show the first frame of video
    # cv2.imshow('myVid', imgVideo)
    # # Show webcam video
    cv2.imshow('Webcam', imgWebcam)
    cv2.waitKey(1)
    frameCounter += 1