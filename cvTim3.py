import cv2 as cv
import numpy as np

# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     frame = cv.circle(frame, (325, 250), 150, (255, 255, 0), 1)
#     cv.imshow("Video", frame)
#     if cv.waitKey(7) == ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()
# _____________________________________________________________________

cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    image = np.zeros(frame.shape, np.uint8)

    width = int(cap.get(3))
    height = int(cap.get(4))

    frame = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
    image[: height // 2, : width // 2] = frame
    image[height // 2 :, : width // 2] = cv.rotate(frame, cv.ROTATE_180)
    image[: height // 2, width // 2 :] = frame
    image[height // 2 :, width // 2 :] = cv.rotate(frame, cv.ROTATE_180)

    cv.imshow("Video", image)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
