import numpy as np
import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
def drawface(x,y,w,h,img):
    cv2.rectangle(img,(0,0),(x,y),(255,0,0),5)
    cv2.rectangle(img,(x,0),(x+w,y),(255,0,0),5)
    cv2.rectangle(img,(x+w,0),(511,y),(255,0,0),5)
    cv2.rectangle(img,(0,y),(x,y+h),(255,0,0),5)
    cv2.rectangle(img,(x+w,y),(511,y+h),(255,0,0),5)
    cv2.rectangle(img,(0,y+h),(x,511),(255,0,0),5)
    cv2.rectangle(img,(x,y+h),(x+w,511),(255,0,0),5)
    cv2.rectangle(img,(x+w,y+h),(511,511),(255,0,0),5)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.resize(frame,(511,511),interpolation=cv2.INTER_CUBIC)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        drawface(x,y,w,h,gray)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
