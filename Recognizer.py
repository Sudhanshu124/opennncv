import cv2
import numpy as np
import pickle
cap = cv2.VideoCapture(0)
cap.set(3, 640) #WIDTH
cap.set(4, 480) #HEIGHT

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
labels={"person_name":1}
with open('labels.pickle','rb') as f:
   alabels= pickle.load(f)
   labels={v:k for k,v in alabels.items()}
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(faces))
    # Display the resulting frame
    for (x,y,w,h) in faces:
         stroke = 2
         #cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y : y+h, x : x+w]
         roi_color = frame[y : y+h, x : x+w]
         id_, conf = recognizer.predict(roi_gray)
         if conf >= 45 :# and conf <= 85:
            print(id_)
            print(labels[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            color=(255,255,255)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
            img_item="1.png"
            cv2.imwrite(img_item,roi_gray)
            #color = (0, 255, 0)
        # eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
            # cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
         end_x_cord = x + w
         end_y_cord = y + h
         cv2.rectangle(frame, (x, y), (end_x_cord, end_y_cord), (0,255,0), stroke)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()