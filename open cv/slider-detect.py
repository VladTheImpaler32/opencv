import cv2
import numpy as np

def empty(i):
    pass

path = "resources/27.jpg"
cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)

kernelOpen=np.ones((10,10))
kernelClose=np.ones((20,20))

def on_trackbar(val):
    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    imgMASK = cv2.inRange(imgHSV, lower, upper)

    maskOpen=cv2.morphologyEx(imgMASK,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
    maskFinal=maskClose

    conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for i in range(len(conts)):
        x,y,w,h = cv2.boundingRect(conts[i])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)

    cv2.imshow("Output1", img)
    # cv2.imshow("Output2", imgHSV)
    cv2.imshow("Mask", imgMASK)
    cv2.imshow("maskfinal", maskFinal)


cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, on_trackbar)
cv2.createTrackbar("Hue Max", "TrackedBars", 8, 179, on_trackbar)
cv2.createTrackbar("Sat Min", "TrackedBars", 50, 255, on_trackbar)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, on_trackbar)
cv2.createTrackbar("Val Min", "TrackedBars", 20, 255, on_trackbar)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, on_trackbar)


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

# while True:
#     ret, img = cam.read()
#     img = cv2.resize(img,(800,600))

#     #convert BGR to HSV
#     imgHSV= cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#     # create the Mask
#     mask=cv2.inRange(imgHSV,lowerBound,upperBound)
#     #morphology
#     maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
#     maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)
#     maskFinal=maskClose
    
#     conts,h=cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

#     # cv2.drawContours(img,conts,-1,(255,0,0),3)
#     for i in range(len(conts)):
#         x,y,w,h = cv2.boundingRect(conts[i])
#         cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255), 2)
#         # cv2.circle(img,(int(x+(w/2)), int(y+(h/2))), int(((h/2)+(w/2))/2), (0,255,0), 2)
    
#     cv2.imshow("maskClose",maskClose)
#     # cv2.imshow("maskOpen",maskOpen)
#     # cv2.imshow("mask",mask)
#     cv2.imshow("img",img)
#     cv2.waitKey(5)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break


# cam.release
# cv2.destroyAllWindows