import cv2
import numpy as np

lowerBound=np.array([0,50,20])
upperBound=np.array([8,255,255])

cam = cv2.VideoCapture(0)
kernelOpen=np.ones((10,10))
kernelClose=np.ones((20,20))


while True:
    ret, img = cam.read()
    img = cv2.resize(img,(800,600))

    #convert BGR to HSV
    imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    maskFinal=maskClose
    
    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    # cv2.drawContours(img,conts,-1,(255,0,0),3)
    for i in range(len(conts)):
        x,y,w,h = cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
        # cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), int(((h/2)+(w/2))/2), (0,255,0), 2)
    
    cv2.imshow("maskClose",maskClose)
    # cv2.imshow("maskOpen",maskOpen)
    # cv2.imshow("mask",mask)
    cv2.imshow("img",img)
    cv2.waitKey(5)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release
cv2.destroyAllWindows