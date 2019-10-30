import numpy as np
import cv2

BASE = "F:/Python37/Lib/site-packages/cv2/data/"

face_cascade = cv2.CascadeClassifier(BASE+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(BASE+'haarcascade_eye.xml')

#img = cv2.imread('people.png')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.rectangle(frame,(x-w,y),(x,y+h),(255,0,0),2)
        cv2.rectangle(frame,(x-w,y-h),(x,y),(255,0,0),2)
        cv2.rectangle(frame,(x-w,y+h),(x,y+2*h),(255,0,0),2)
        cv2.rectangle(frame,(x,y-h),(x+w,y),(255,0,0),2)
        cv2.rectangle(frame,(x,y+h),(x+w,y+2*h),(255,0,0),2)
        cv2.rectangle(frame,(x+w,y-h),(x+2*w,y),(255,0,0),2)
        cv2.rectangle(frame,(x+w,y),(x+2*w,y+h),(255,0,0),2)
        cv2.rectangle(frame,(x+w,y+h),(x+2*w,y+2*h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('Girafboy', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
#img[0:200, 0:200] = img[300:500,300:500]

cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()
