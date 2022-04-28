import cv2
import numpy as np

def empty(i):
    pass

path = "resources/27.jpg"
cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')



def on_trackbar(val):
    face = cv2.getTrackbarPos("Face", "TrackedBars")
    eyes = cv2.getTrackbarPos("Eyes", "TrackedBars")
    smile = cv2.getTrackbarPos("Smile", "TrackedBars")
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, face)
    # eyes = eye_cascade.detectMultiScale(gray, 1.1, eyes)
    # smiles = smile_cascade.detectMultiScale(gray, 1.1, smile)

    cv2.imshow("Output1", img)
    # cv2.imshow("Output2", imgHSV)
    # cv2.imshow("Mask", imgMASK)
    # cv2.imshow("maskfinal", maskFinal)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

    


cv2.createTrackbar("Face", "TrackedBars", 5, 255, on_trackbar)
cv2.createTrackbar("Eyes", "TrackedBars", 15, 255, on_trackbar)
cv2.createTrackbar("Smile", "TrackedBars", 150, 255, on_trackbar)



cam = cv2.VideoCapture(0)

while True:

    ret, img = cam.read()
    img = cv2.resize(img,(800,600))
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        

    # Show some stuff
    on_trackbar(0)

    # Wait until user press some key
    cv2.waitKey(10)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release
cv2.destroyAllWindows