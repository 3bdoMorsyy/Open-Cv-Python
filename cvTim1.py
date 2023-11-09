import cv2 as cv

img1 = cv.imread("cat.png")  # GrayScale = 0 , B G R = 1 , Neglected(Default) = -1
print(img1.shape)
img2 = cv.resize(img1, (0, 0), fx=0.5, fy=0.5)
img3 = cv.rotate(img1, cv.ROTATE_180)
cv.imwrite("New_Cat.jpg", img3)
cv.imshow("Cat1", img1)
cv.imshow("Cat2", img2)
cv.imshow("Cat3", img3)
cv.waitKey(0)
cv.destroyAllWindows()
