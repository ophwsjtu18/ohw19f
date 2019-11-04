import numpy as np
import cv2
import time
import serial
import serial.tools.list_ports
def rectangle_img (frame,w,h):
    frame = cv2.rectangle(frame,(0,0),(w,h),(0,255,0),2)        #x是640，y是480
    frame = cv2.rectangle(frame,(w,h),(2*w,2*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(2*w,2*h),(3*w,3*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(0,h),(w,2*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(0,2*h),(w,3*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(w,0),(2*w,h),(0,255,0),2)
    frame = cv2.rectangle(frame,(2*w,0),(3*w,h),(0,255,0),2)
    frame = cv2.rectangle(frame,(2*w,h),(3*w,2*h),(0,255,0),2)
    frame = cv2.rectangle(frame,(w,2*h),(2*w,3*h),(0,255,0),2)

def choose(x0,y0,w,h):
    if x0 < w and y0 < h:
        return 20
    elif x0 > w and x0 < 2*w and y0 < h:
        return 40
    elif x0 > 2*w and x0 < 3*w and y0 < h:
        return 60
    elif x0 < w and y0 > h and y0 < 2*h:
        return 80
    elif x0 > w and x0 < 2*w and y0 > h and y0 < 2*h:
        return 100
    elif x0 > 2*w and x0 < 3*w and y0 > h and y0 < 2*h:
        return 120
    elif x0 < w and y0 > 2*h and y0 < 3 *h:
        return 140
    elif x0 > w and x0 < 2*w and y0 > 2*h and y0 < 3 *h:
        return 160
    elif x0 > 2*w and x0 < 3*w and y0 > 2*h and y0 < 3 *h:
        return 180

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

ret_1,img = cap.read()
print(img.shape)

w = int(img.shape[1]/3)
h = int(img.shape[0]/3)

x0 = 1
y0 = 1
while (True):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    rectangle_img(frame,w,h)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for list_1 in faces:
        x0 = int(list_1[0])
        y0 = int(list_1[1])
    for (x,y,w0,h0) in faces:
        frame = cv2.rectangle(frame,(x,y),(x+w0,y+h0),(125,125,125),2)
        roi_gray = gray[y:y+h0,x:x+w0]
        roi_color = frame[y:y+h0,x:x+w0]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        print(type(x))                                #x是一个元组中的int

        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)
    
    k = choose(x0,y0,w,h)
    print (k)

    cv2.imshow('frame',frame)

    ports = list(serial.tools.list_ports.comports())
    
    for p in ports:
        print (p[1])
        if "SERIAL" in p[1]:
	        ser = serial.Serial(port=p[0])
        else :
	        print ("No Arduino Device was found connected to the computer")
    time.sleep(2)
    action = str(k)+','+str(k)+','
    ser.write(action.encode())
    time.sleep(1)

    if cv2.waitKey(1) and 0xFF==ord('q'):
        break

cap.release()
cv2.destroyWindow()
