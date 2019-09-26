import numpy as np 			
import cv2  				
import vlc			

 
cap = cv2.VideoCapture(0) 


player=vlc.MediaPlayer("Bekhayali - Kabir Singh.mp3")


face_cascade = cv2.CascadeClassifier('frontalface_default.xml') 


flag = 0 


while True:
    ret , img = cap.read() 
    faces = face_cascade.detectMultiScale(img, 1.3, 5)

    if(len(faces)>0):
        for (x, y, w, h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            print ("Face is facing front")
            if(flag==0):
                player.play()
                flag = 1

    elif len(faces)==0 and flag==1:
            print ("Face is not facing front")
            player.pause()
            flag=0
            
    cv2.imshow('Face',img)
    k=cv2.waitKey(1)
    if(k==ord('q')):
        break 


cap.release() 
cv2.destroyAllWindows()
