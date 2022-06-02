import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
# x = np.uint8([250])
# y = np.uint8([10])

# print( cv.add(x,y) )
# print( x+y )


# img1 = cv.imread('/Volumes/roczhang/data/opencv-img/ml.png')
# img2 = cv.imread('/Volumes/roczhang/data/opencv-img/opencv-logo.png')
# dst = cv.addWeighted(img1,0.7,img2,0.3,0)
# cv.imshow('dst',dst)
# cv.waitKey(0)
# cv.destroyAllWindows()


# Load two images
img1 = cv.imread('/Volumes/roczhang/data/opencv-img/messi5.jpg')
img2 = cv.imread('/Volumes/roczhang/data/opencv-img/opencv-logo-white.png')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
# 在图像的左上角选择一块区域，大小和logo大小一样。
roi = img1[0:rows, 0:cols]
# Now create a mask of logo and create its inverse mask also
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)  # 将RGB图像转化为单通道灰色图像
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)  # 二值化图像 所有像素不是0就是255 
mask_inv = cv.bitwise_not(mask)
# Now black-out the area of logo in ROI
img1_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
# Take only region of logo from logo image.
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
# Put logo in ROI and modify the main image
dst = cv.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv.imshow('res',img1)
cv.waitKey(0)
cv.destroyAllWindows()

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('image')
plt.subplot(232),plt.imshow(img2,'gray'),plt.title('logo')
plt.subplot(233),plt.imshow(img2gray,'gray'),plt.title('img2gray')
plt.subplot(234),plt.imshow(img1_bg,'gray'),plt.title('img1_bg')
plt.subplot(235),plt.imshow(img2_fg,'gray'),plt.title('img2_fg')
plt.subplot(236),plt.imshow(dst,'gray'),plt.title('dst')
plt.show()