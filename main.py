import cv2
import poseModule as pm
import numpy as np


cap = cv2.VideoCapture(r'C:\Users\Nanthu s\Downloads\computer vision\open cv\Pushup_counter\istockphoto-1340785171-640_adpp_is.mp4')

detector = pm.poseDetector()

count = 0
dir = 0

while True:

 #1. image preprocessing
    success,image = cap.read()
    image = cv2.resize(image,(1280,720))


 #2.find body
    image = detector.findPose(image,draw=False)
    #print(image)
    lmlist = detector.findPosition(image,draw=False)
    #print(lmlist)


 #3. find angles of specific landmarks
    if len(lmlist)!=0:

        #angle = detector.findAngle(image,11,13,15)
        #print(angle)
        angle = detector.findAngle(image,12,14,16)
        #print(angle)



 #4. counting

    per = np.interp(angle,(70,180),(0,100))
    #print(per)

    #print(angle,'----->',per)

    if per== 100:
        if dir == 1:
           count += 0.5
           dir = 0

    if per == 0:
        if dir == 0:
            count += 0.5
            dir = 1
    
    #print(count)

    cv2.rectangle(image,(0,0),(150,150),(0,255,0),cv2.FILLED)
    cv2.putText(image,str(int(count)),(50,100),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,0),5)
    cv2.putText(image,'COUNT',(0,200),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),5)

    bar = np.interp(angle,(70,180),(600,100))

    #print(bar)

    cv2.rectangle(image,(1100,100),(1200,600),(0,255,0),3)
    cv2.putText(image,'PER%',(1100,650),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,0,255),5)

    

    cv2.rectangle(image,(1100,int(bar)),(1200,600),(0,255,0),cv2.FILLED)


    cv2.putText(image,str(int(per)),(1100,100),cv2.FONT_HERSHEY_COMPLEX,3,(0,0,0),5)



    cv2.imshow('Pushup counter',image)
    if cv2.waitKey(1) & 0xFF == 27:
        break