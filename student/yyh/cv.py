import cv2

def drawboard(img, x, y, w, h):
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            img = cv2.rectangle(img, (int(x + i * w), int(y + j * h)),
                                (int(x + (i + 1) * w), int(y + (j + 1) * h)), (255, 0, 0), 2)
    return img

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('D:/python/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('D:/python/Lib/site-packages/cv2/data/haarcascade_eye.xml')
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        img = drawboard(img, x, y, w, h)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

