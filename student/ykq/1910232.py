import numpy as np
import cv2

def drawface(img):
    face_cascade = cv2.CascadeClassifier('D:\software\python\Python3.6.8\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        for i in range(3):
            for j in range(3):
                img = cv2.rectangle(img,(x+i*int(w/3),y+j*int(h/3)),(x+(i+1)*int(w/3),y+(j+1)*int(h/3)),(255,100,20),2)
    cv2.imshow('img',img)
    
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',frame)
    drawface(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
