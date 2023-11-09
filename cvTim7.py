import cv2 as cv
import numpy as np

img = cv.imread("soccer_practice.jpg", 1)
template = cv.imread("template2.jpg", 0)
h, w = template.shape


methods = [
    cv.TM_CCOEFF,
    cv.TM_CCOEFF_NORMED,
    cv.TM_CCORR,
    cv.TM_CCORR_NORMED,
    cv.TM_SQDIFF,
    cv.TM_SQDIFF_NORMED,
]

for method in methods:
    img2 = img.copy()
    result = cv.matchTemplate(cv.cvtColor(img2, cv.COLOR_BGR2GRAY), template, method)
    _, _, min_loc, max_loc = cv.minMaxLoc(result)
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    cv.rectangle(img2, location, (location[0] + w, location[1] + h), (0, 255, 0), 5)
    cv.imshow("Image", img2)
    cv.waitKey(0)
