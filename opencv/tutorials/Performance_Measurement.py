import cv2 as cv

img1 = cv.imread(r'C:\Users\roc\OneDrive\data\opencv-img\messi5.jpg')
e1 = cv.getTickCount()
for i in range(5,49,2):
    img1 = cv.medianBlur(img1,i)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
