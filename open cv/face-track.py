import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    # eyes = eye_cascade.detectMultiScale(gray, 1.1, 15)
    # smiles = smile_cascade.detectMultiScale(gray, 1.1, 150)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), int(w/2), (0,0,255), 2)

    # for(x, y, w, h) in eyes:
    #     # cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0, 0), 2)
    #     cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), 10, (255,0,0), 2)

    # for(x, y, w, h) in smiles:
    #     cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(10) & 0xff

    if k==27:
        break

cap.release()