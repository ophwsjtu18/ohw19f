#标题   
121

##标题  
121

###标题  
121

![第一次作业](https://github.com/ophwsjtu18/ohw19f/blob/master/student/xyz/%E6%8D%95%E8%8E%B7.PNG)
------------分割线-----------------------------------------------------------------------------------------
![第二次作业](https://github.com/ophwsjtu18/ohw19f/blob/master/student/xyz/1.PNG)
import numpy as np
import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('sachin.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detects objects of different sizes in the input image.
# The detected objects are returned as a list of rectangles.
#cv2.CascadeClassifier.detectMultiScale(image, scaleFactor, minNeighbors, flags, minSize, maxSize)
#scaleFactor – Parameter specifying how much the image size is reduced at each image
#scale.
#minNeighbors – Parameter specifying how many neighbors each candidate rectangle should
#have to retain it.
#minSize – Minimum possible object size. Objects smaller than that are ignored.
#maxSize – Maximum possible object size. Objects larger than that are ignored.
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
roi_gray = gray[y:y+h, x:x+w]
roi_color = img[y:y+h, x:x+w]
eyes = eye_cascade.detectMultiScale(roi_gray)
for (ex,ey,ew,eh) in eyes:
cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cap = cv2.VideoCapture(0)
 while(True):
 # Capture frame-by-frame
 ret, frame = cap.read()

# Our operations on the frame come here
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

 # Display the resulting frame
 cv2.imshow('frame',gray)
 if cv2.waitKey(1) & 0xFF == ord('q'):
break
# When everything done, release the capture
 cap.release()
cv2.destroyAllWindows()
