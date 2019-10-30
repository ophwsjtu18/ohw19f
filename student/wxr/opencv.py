import numpy as np
import cv2
def draw(img,x,y,w,h):
    img = cv2.rectangle(img, (x, y), (x + w, y + h),(255, 0, 0), 2)
    img = cv2.rectangle(img, (x-50,y-50), (x , y ),(255, 0, 0), 2)
    img = cv2.rectangle(img, (x,y-50), (x + w, y), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x+w, y-50), (x + w+50, y), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x-50, y), (x, y+h), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x, y), (x + w, y+h), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x + w, y), (x + w + 50, y+h), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x-50, y+h), (x, y + h+50), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x, y+h), (x + w, y + h+50), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x + w, y+h), (x + w + 50, y + h+50), (255, 0, 0), 2)
    return img
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        gray = draw(frame, x, y, w, h)
    cv2.imshow('wyc', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()





