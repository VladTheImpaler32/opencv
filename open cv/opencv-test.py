import cv2
import numpy as np

cv2.namedWindow('image')
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    cv2.imshow('image', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release
cv2.destroyAllWindows