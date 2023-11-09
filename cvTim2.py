import cv2 as cv
import numpy as np
import random

img = cv.imread("Batman.jpg")
print(img.shape)  # ( Width , Height , Depth )
batman = img[150:250, 180:400]  # Height , Width
img[0:100, 0:220] = batman
cv.imshow("Batman", img)
cv.imshow("BatmanLogo", batman)
cv.waitKey(0)
cv.destroyAllWindows()

img2 = cv.imread("cat.png")
for i in range(50):
    for j in range(img2.shape[1]):
        img2[i][j] = [
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        ]
cv.imshow("cat", img2)
cv.waitKey(0)
