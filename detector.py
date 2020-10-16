
### SRI KANIPAKALA COVID-19 project 2020

import cv2
import numpy as np
import time
import os
from pynput.mouse import Button, Controller


##recognizer = cv2.createLBPHFaceRecognizer_create()
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

os.system("START.mp3") # play when starting face scan
cam = cv2.VideoCapture(1)
#font = cv2.FONT_HERSHEY_SIMPLEX
##font = cv2.InitFont(cv2.FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
font = cv2.FONT_HERSHEY_SIMPLEX
##cv2.putText()
font2 = cv2.FONT_HERSHEY_DUPLEX

readingA =0
readingB =0
readingC =0
readingD =0
response=""

def sayIt(name):
    ##os.system("start rashmi_good.mp3")
    print('[+] playing audio', name)
    os.system("start " + name)
    
def light():
    mouse = Controller()    
    mouse.position = (1529,205)
    mouse.click(Button.left, 1)
    print("[+] Changing light to Green")
    time.sleep(3)
    mouse.position = (1529,205)
    mouse.click(Button.left, 1)
    print("[+] Resetting Light")
while True:
    color = (0,0,255) ## RED
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    
   ## cv2.putText(im, status, (100, 100), font2, 2, color , 2) ## my print status
    status= "Denied"
        
    check=0
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
       
        print("[+] Confidence Level = " + str(conf))
        
        #print("Confidence = " + str(conf))
        
        if(conf<61):      
            status = "ID Match"                
            color = (0,255,0) ## update GREEN
            if(Id==1):
                
                Id="MASTER"
                if(conf < 52):
                    
                    response = "START.mp3"
                    ##os.system("start adiAllow.mp3")
                    check=1
                    readingA = readingA +1
                    ##time.sleep(3)
                    
                    
                
            elif(Id==2):
                Id="USER1"
               ## readingA= 0;                
                readingA = readingA +1
                response = "USER1.mp3"
                check =1
                
            elif(Id==3):
                Id="USER2"
                                
                readingA = readingA +1
                response = "USER2.mp3"
                check =1
            elif(Id==4):
                Id="USER3"
                ##readingA= 0;                
                readingA = readingA +1
                response = "USER3.mp3"
                check =1
            elif(Id==5):
                Id="USER4"
                ##readingA= 0;                
                readingA = readingA +1
                response = "USER4.mp3"
                check =1
            elif(Id==6):
                check=2
                Id="USER5"
                readingA= 0;
                
                readingB = readingB +1
                response = "USER5.mp3"
            elif(Id==7):
                check=2
                Id="USER6"
                readingA= 0;
                
                readingB = readingB +1
                response = "USER6.mp3" 
                
        else:
            Id="Unknown"
            readingA=0
            readingB=0
            readingC=0
            readingD=0
        
        cv2.putText(im, Id, (x - 1, y - 1), font,2,(0, 255, 0),7)
        
        
        cv2.imshow('Face Recognition', im )
        ##cv2.PutText(cv2.fromarray(im),str(Id), (x,y+h),font, 255)
        progress =  str(  (readingA/10)*100 )
        cv2.putText(im, "Scaning%: " + progress , (900, 100), font2, 1, (255,0,0) , 2)        
    cv2.putText(im, status, (100, 100), font2, 2, color , 2) ## my print status
   
    
   
    if(check==2 and readingB == 5):
        sayIt(response)
    if(check==1 and readingA>=10):
        time.sleep(1)
        print('[!!!] Security Bypassed!')
        sayIt(response)
        light()
        ##time.sleep(2)
        readingA=0
    cv2.imshow('Face Recognition', im )
    
    if cv2.waitKey(10) ==ord('q'):
        break
    


    
cam.release()
cv2.destroyAllWindows()
