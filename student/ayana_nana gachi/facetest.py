import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap=cv2.VideoCapture(1)


while(True):
    ret,frame=cap.read()

    #frame = cv2.imread('frame')
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    #print(faces)
    for (x,y,w,h) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        frame = cv2.rectangle(frame,(x+w,y),(x+2*w,y+h),(255,0,0),2)
        frame = cv2.rectangle(frame,(x-w,y+h),(x,y+2*h),(255,0,0),2)
        frame = cv2.rectangle(frame,(x,y+h),(x+w,y+2*h),(255,0,0),2)
        frame = cv2.rectangle(frame,(x,y-h),(x+w,y),(255,0,0),2)
        frame = cv2.rectangle(frame,(x-w,y),(x,y+h),(255,0,0),2)
        frame = cv2.rectangle(frame,(x-w,y-h),(x,y),(255,0,0),2)
        frame = cv2.rectangle(frame,(x+w,y+h),(x+2*w,y+2*h),(255,0,0),2)
        frame = cv2.rectangle(frame,(x+w,y-h),(x+2*w,y),(255,0,0),2)
        #roi_gray = frame[y:y+h, x:x+w]
        #roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()
