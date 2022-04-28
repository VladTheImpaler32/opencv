import cv2
from deepface import DeepFace

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)

    result = DeepFace.analyze(img_path = frame , actions=['emotion'], enforce_detection=False )
    emotion = result["dominant_emotion"]
    txt = str(emotion)
    cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)

    # race_result = DeepFace.analyze(img_path = frame , actions=['race'], enforce_detection=False )
    # race = race_result["dominant_race"]
    # txt2 = str(race)
    # cv2.putText(frame,txt2,(50,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)

    # age_result = DeepFace.analyze(img_path = frame , actions=['age'], enforce_detection=False )
    # age = age_result["age"]
    # txt3 = str(age)
    # cv2.putText(frame,txt3,(50,70),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)

    # gender_result = DeepFace.analyze(img_path = frame , actions=['gender'], enforce_detection=False )
    # gender = gender_result["gender"]
    # txt4 = str(gender)
    # cv2.putText(frame,txt4,(50,90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),1)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()