import cv2
import vlc

cas =cv2.CascadeClassifier("frontalface_default.xml")
cap=cv2.VideoCapture(0)
player = vlc.MediaPlayer("Bekhayali - Kabir Singh.mp3")
count=0
face_visible=0
while 1:
    try:
        ret,frame=cap.read()
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=cas.detectMultiScale(gray)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
        if len(faces)>0:
            face_visible=1
        else:
            face_visible=0
            
        if face_visible==1 and count==0:
            player.play()
            count+=1
        elif face_visible==0:
            player.pause()

        cv2.imshow('face',frame)
        k=cv2.waitKey(1)
        if k==ord('q'):
            cv2.destroyAllWindows()
            break

            
    except:
        pass

cap.release()
