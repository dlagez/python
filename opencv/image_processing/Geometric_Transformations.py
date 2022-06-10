import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
'''
@Time    :   2022/06/06 19:18:16
@Author  :   RocZhang 
@Contact :   mr.roczhang@outlook.com
'''
# 图像的几何变换

# 缩放，只是改变图像的大小
img = cv.imread('/Volumes/roczhang/data/opencv-img/messi5.jpg')
# 2倍长宽
res = cv.resize(img,None,fx=2, fy=2, interpolation = cv.INTER_CUBIC)

height, width = img.shape[:2]
res = cv.resize(img,(2*width, 2*height), interpolation = cv.INTER_CUBIC)

# 翻译是物体位置的移动
# cv.imread() 第二个参数是控制图像的模式，值为0的话读取的是灰度图像
img = cv.imread('/Volumes/roczhang/data/opencv-img/messi5.jpg', 0)
rows,cols = img.shape
M = np.float32([[1,0,100],[0,1,50]])
# 向右移动100个像素点，向下移动50个像素点
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 旋转
img = cv.imread('/Volumes/roczhang/data/opencv-img/messi5.jpg', 0)
rows,cols = img.shape
# cols-1 and rows-1 are the coordinate limits.
M = cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),90,1)
dst = cv.warpAffine(img,M,(cols,rows))
cv.imshow('img',dst)
cv.waitKey(0)
cv.destroyAllWindows()

# 仿射变换
# 没有图片，
img = cv.imread('drawing.png')
rows,cols,ch = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv.getAffineTransform(pts1,pts2)
dst = cv.warpAffine(img,M,(cols,rows))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

img = cv.imread('/Volumes/roczhang/data/opencv-img/sudoku.png')
rows,cols,ch = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
