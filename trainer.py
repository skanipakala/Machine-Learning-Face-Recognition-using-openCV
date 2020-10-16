import cv2,os
import numpy as np
from PIL import Image
import time

##recognizer = cv2.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

def getImagesAndLabels(path):
    
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    
    faceSamples=[]

    Ids=[]
   
    for imagePath in imagePaths:
   
        if(os.path.split(imagePath)[-1].split(".")[-1]!='jpg'):
            continue
        
        pilImage=Image.open(imagePath).convert('L')
        print(imagePath)        
        imageNp=np.array(pilImage,'uint8')      
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        
        faces=detector.detectMultiScale(imageNp)
        print('Extracting Face...')
               for (x,y,w,h) in faces:
            print('adding cropped image to face sample archive')
            faceSamples.append(imageNp[y:y+h,x:x+w])
            Ids.append(Id)
    return faceSamples,Ids


faces,Ids = getImagesAndLabels('dataSet')
print('[+] Analysis in progress...')
recognizer.train(faces, np.array(Ids))
recognizer.save('trainer/trainner.yml')
print('[!!!] Image Analysis Complete!')
time.sleep(2)
