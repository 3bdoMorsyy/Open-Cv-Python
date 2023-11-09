import cv2 as cv

# Draw Line
# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     width = int(cap.get(3))
#     height = int(cap.get(4))
#     cv.line(frame, (0, 0), (width, height), (255, 255, 255), 3)
#     cv.line(frame, (width, 0), (0, height), (255, 255, 255), 3)
#     cv.imshow("Frame1", frame)
#     if cv.waitKey(1) == ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()
# _________________________________________________________________

# Draw Rectangle

# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     width = int(cap.get(3))
#     height = int(cap.get(4))
#     cv.rectangle(
#         frame,
#         (width // 4, height // 4),
#         ((width * 3) // 4, (height * 3) // 4),
#         (255, 255, 255),
#         3,
#     )
#     cv.imshow("Frame", frame)
#     if cv.waitKey(1) == ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()
# _________________________________________________________________

# Draw Circle

# cap = cv.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
#     width = int(cap.get(3))
#     height = int(cap.get(4))
#     cv.circle(
#         frame,
#         (width // 2, height // 2),
#         height * 2 // 6,
#         (255, 255, 255),
#         3,
#     )
#     cv.imshow("Frame", frame)
#     if cv.waitKey(1) == ord("q"):
#         break
# cap.release()
# cv.destroyAllWindows()
# _________________________________________________________________

# Type Text
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    width = int(cap.get(3))
    height = int(cap.get(4))
    cv.rectangle(
        frame,
        (width // 4, height // 4),
        ((width * 3) // 4, (height * 3) // 4),
        (0, 0, 0),
        3,
    )
    cv.rectangle(
        frame,
        ((width - 10) // 4, height // 5),
        ((width * 4) // 9, height // 4),
        (0, 0, 0),
        -1,
    )
    cv.putText(
        frame,
        "Abdelrahman",
        (width // 4, (height // 4) - 5),
        cv.FONT_HERSHEY_PLAIN,
        1,
        (255, 255, 255),
        1,
        cv.LINE_AA,
    )
    cv.imshow("Frame", frame)
    if cv.waitKey(1) == ord("q"):
        break
cap.release()
cv.destroyAllWindows()
