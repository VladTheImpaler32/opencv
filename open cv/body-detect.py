import cv2

body_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_fullbody.xml')
upper_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')


cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect body
    body = body_cascade.detectMultiScale(gray, 1.1, 1)
    upper = upper_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in body:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), int(w/2), (0,0,255), 2)

    for (x, y, w, h) in upper:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), int(w/2), (0,0,255), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(5) & 0xff

    if k==27:
        break

cap.release()