import numpy as np
import cv2

igniter = 8880 # just a random number to avoid overwriting file names
detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(1)

id =input('enter the ID #')
sampleNum = 1;
while(True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        
        sampleNum = sampleNum+1
        cv2.imwrite("dataSet/User." + str(id) + "." + str(sampleNum*igniter) + ".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100)
    cv2.imshow('frame',img)
    cv2.waitKey(1)
    if(sampleNum > 210):
        break
cap.release()
cv2.destroyAllWindows()

print('collection complete!!!')
