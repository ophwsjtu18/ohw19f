import numpy as np
import cv2


def draw_board(img, x, y, w, h):
    height, width, _ = img.shape
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    img = cv2.rectangle(img, (0, 0), (x, y), (255, 0, 0), 2)
    img = cv2.rectangle(img, (0, y), (x, y + h), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x, 0), (x + w, y), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x + w, 0), (width, y), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x + w, y), (width, y + h), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x + w, y + h), (width, height), (255, 0, 0), 2)
    img = cv2.rectangle(img, (x, y + h), (x + w, height), (255, 0, 0), 2)
    img = cv2.rectangle(img, (0, y + h), (x, height), (255, 0, 0), 2)
    return img



face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, 1.3, 5)
    for (x, y, w, h) in faces:
        gray = draw_board(frame, x, y, w, h)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

