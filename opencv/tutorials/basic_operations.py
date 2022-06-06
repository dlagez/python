import numpy as np
import cv2 as cv

img = cv.imread('/Volumes/roczhang/data/opencv-img/messi5.jpg')
px = img[100, 100]
blue = img[100, 100]
img[100,100] = [255,255,255]
# cv.imshow("messi", img)
# cv.waitKey()
# cv.destroyAllWindows()
cv.imwrite('messi6.jpg', img)

print( img.shape )
print( img.size )
print( img.dtype )

# 将球复制一份
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball


import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
BLUE = [255,0,0]
img1 = cv.imread('/Volumes/roczhang/data/opencv-img/opencv-logo.png')
replicate = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_WRAP)
constant= cv.copyMakeBorder(img1,10,10,10,10,cv.BORDER_CONSTANT,value=BLUE)
plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')
plt.show()