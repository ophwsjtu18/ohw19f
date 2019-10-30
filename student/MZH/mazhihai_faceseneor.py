import numpy as np
import cv2

def draw_nine(x,y,w,h,frame):
    for i in range(2):
        for j in range(3):
            cv2.rectangle(frame,(x-w-1+j*w+j*1,y-h-1+i*2+i*h*2),(x-1+j*w+j*1,y-1+i*2+i*h*2),(255,0,0),2)
    cv2.rectangle(frame,(x-w-1,y),(x-1,y+h),(255,0,0),2)
    cv2.rectangle(frame,(x+w+1,y),(x+2*w+1,y+h),(255,0,0),2)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        draw_nine(x,y,w,h,frame)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
