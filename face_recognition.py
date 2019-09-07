import argparse
import cv2 as cv
import datetime

# These classifiers are part of opencv source code
# they're in opencv/data/haarcascade
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')

cap = cv.VideoCapture(0)

while(True):
    ret, img = cap.read()
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv.imshow("Face recognized", img)

    k = cv.waitKey(1)
    if k == 27: # ESC
        print('ESC')
        break
    elif k == 115: # s
        print('shoot')
        cv.imwrite('robot-{}.jpg'.format(datetime.datetime.now().time()), img)

cap.release()
cv.destroyAllWindows()
