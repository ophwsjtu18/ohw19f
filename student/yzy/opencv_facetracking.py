import numpy as np
import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('E:/visual studio/share/Python37_64/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('E:/visual studio/share/Python37_64/Lib/site-packages/cv2/data/haarcascade_eye.xml')
while(True): # Capture frame-by-frame 
    ret, frame = cap.read() # Our operations on the frame come here
    
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x,y,w,h) in faces:
        #frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        frame = cv2.line(frame,(x,y-h),(x,y+h+h),(255,0,0),2) 
        frame = cv2.line(frame,(x+w,y-h),(x+w,y+h+h),(255,0,0),2) 
        frame = cv2.line(frame,(x-w,y),(x+w+w,y),(255,0,0),2) 
        frame = cv2.line(frame,(x-w,y+h),(x+w+w,y+h),(255,0,0),2)
        frame = cv2.rectangle(frame,(x-w,y-h),(x+w+w,y+h+h),(255,0,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
# When everything done, release the capture 
cap.release()
cv2.destroyAllWindows()