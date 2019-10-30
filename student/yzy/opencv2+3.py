import numpy as np
import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('E:/visual studio/share/Python37_64/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('E:/visual studio/share/Python37_64/Lib/site-packages/cv2/data/haarcascade_eye.xml')
while(True): # Capture frame-by-frame 
    ret, frame = cap.read() # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Display the resulting frame 
    cv2.imshow('frame',gray)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    img = ret
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
# When everything done, release the capture 
cap.release()
cv2.destroyAllWindows()