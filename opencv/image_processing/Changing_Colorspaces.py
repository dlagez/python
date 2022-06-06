import cv2 as cv

'''
@Time    :   2022/06/06 19:18:28
@Author  :   RocZhang 
@Contact :   mr.roczhang@outlook.com
'''
# flags = [i for i in dir(cv) if i.startswith('COLOR_')]
# print( flags )

# Take each frame of the video
# Convert from BGR to HSV color-space
# We threshold the HSV image for a range of blue color
# Now extract the blue object alone, we can do whatever we want on that image.

# 由于没有摄像头，所以这个跳过，以前这个代码跑过两三次。
import cv2 as cv
import numpy as np
cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow('frame',frame)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()