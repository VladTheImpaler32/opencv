import serial
import cv2

serialPort = serial.Serial(port = "COM7", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

face_cascade = cv2.CascadeClassifier('C:/Users/esorb/Desktop/turret/python version/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:/Users/esorb/Desktop/turret/python version/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    img = cv2.resize(img,(800,600))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 20)
    # eyes = eye_cascade.detectMultiScale(gray, 1.1, 15)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), 2, (0,0,255), 2)

        TurretX = str(int(x+(w/2)) / (800 / 180))
        TurretY = str(int(y+(h/2)) / (600 / 180))

        serialPort.write(str(('X' + TurretX) + ('Y' + TurretY)).encode())

    # for(x, y, w, h) in eyes:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    #     cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), 2, (0,0,255), 2)

    #     TurretX = str(int(x+(w/2)) / (800 / 180))
    #     TurretY = str(int(y+(h/2)) / (600 / 180))

    #     serialPort.write(str(('X' + TurretX) + ('Y' + TurretY)).encode())



    cv2.imshow('img', img)
    k = cv2.waitKey(10) & 0xff

    if k==27:
        break

cap.release()
