import numpy as np
import cv2
capture = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('C:\\Users\\DING-DING\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\DING-DING\\AppData\\Local\\Programs\\Python\\Python36\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml')
while(True):

    ret, frame = capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(gray,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
            
    def hhh( lists ):
        for (x,y,w,h) in lists:
            a = x
            for  num in range(1,4):
                for num in range(1,4):
                  cv2.rectangle(img,(x,y),(x+int(w/3),y+int(h/3)),(255,0,0),2)
                  x+=int(w/3)
                
                x=a
                y+=int(h/3)    
    hhh(faces)
    cv2.imshow('frame',gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
