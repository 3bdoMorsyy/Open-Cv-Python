import cv2 as cv
import numpy as np

img = cv.imread("chessboard.png")
img = cv.resize(img, (0, 0), fx=0.6, fy=0.6)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 100, 0.01, 10)
# goodFeaturesToTrack(image, corners, qualityLevel, minDistance)

corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv.circle(img, (x, y), 5, (255, 0, 0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        cv.line(img, corner1, corner2, (0, 255, 0), 1)


cv.imshow("Image1", img)
cv.imshow("Image2", gray)
cv.waitKey(0)
cv.destroyAllWindows()
