import cv2
import datetime
cap=cv2.VideoCapture(0)
cap.set(3,760)
cap.set(4,760)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_COMPLEX
        text="Width="+str(cap.get(3))+ ", Height="+str(cap.get(4))
        datet=str(datetime.datetime.now())
        frame=cv2.putText(frame,datet,(10,50),font,1,(255,255,0),2,cv2.LINE_AA)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()