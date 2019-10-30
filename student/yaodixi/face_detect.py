import numpy as np
import cv2

def draw_chess_board(faces,img):
    for (x,y,w,h) in faces:
        x_interval=int(w/3)
        y_interval=int(h/3)
        for i in range(2):
            img = cv2.line(img, (x+(i+1)*x_interval,y),(x+(i+1)*x_interval,y+h),(0,0,255),1)
            img = cv2.line(img, (x,y+(i+1)*y_interval),(x+w,y+(i+1)*y_interval),(0,0,255),1)
    return img

cap =cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')
while(True):
    ret,img=cap.read()   
    #img = cv2.imread('test.jpg')
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_color)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    img=draw_chess_board(faces,img)
    cv2.imshow('img',img)
    if cv2.waitKey(1)& 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
