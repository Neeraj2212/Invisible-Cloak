import cv2
import numpy as np

cap = cv2.VideoCapture(0)
back = cv2.imread("BackGround.jpg")

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # cv2.imshow("HSV",hsv)
        # Blue _Hsv = 120,255,255
        l_blue = np.array([100, 150, 0])
        h_blue = np.array([140, 255, 255])
        kernel = np.ones((4, 4), np.uint8)

        mask = cv2.inRange(hsv, l_blue, h_blue)
        # cv2.imshow("Mask1",mask)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # cv2.imshow("mask2",mask)
        mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel)
        # cv2.imshow("mask3",mask)
        mask2 = cv2.bitwise_not(mask)

        part1 = cv2.bitwise_and(back, back, mask=mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask2)
        # cv2.imshow("part1",part1)

        cv2.imshow("invisble", part1 + part2)

        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
