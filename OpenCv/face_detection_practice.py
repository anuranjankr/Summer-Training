import cv2
'''
cas =cv2.CascadeClassifier("frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
while 1:
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=cas.detectMultiScale(gray)
    try:
        print(faces)
        print(len(faces))
        print(faces.shape)
    except:
        pass
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        cv2.putText(frame, "Face", (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA) 
    cv2.imshow('face',frame)
    k=cv2.waitKey(1000)
    if k==ord('q'):
        cv2.destroyAllWindows()
        break

cap.release()
'''
cas =cv2.CascadeClassifier("frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
frame=cv2.imread("group_photo2.webp")
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
faces=cas.detectMultiScale(gray)
try:
    print(faces)
    print(len(faces))
    print(faces.shape)
except:
    pass
for (x,y,w,h) in faces:
    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),4)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = frame[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.putText(frame, "Face", (x, h), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA) 
cv2.imshow('face',frame)
k=cv2.waitKey(0)
if k==ord('q'):
    cv2.destroyAllWindows()
    
