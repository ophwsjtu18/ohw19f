import numpy as numpy
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.videoCapture(1)

while(1):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        coordinate = [(x,y),(x+w,y),(x+w,y+h),(x,y+h),(x-w,y+h),(x-w,y),(x-w,y-h),(x,y-h),(x+w,y-h)]
        for (eks,why) in coordinate:
            cv2.rectangle(frame,(eks,why),(eks+w,why+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    time.sleep(0.5) #refresh every 0.5 seconds

cap.release()
cv2.destroyAllWindows()