import cv2
import os
from PIL import Image
import pickle
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
current_id=0
label_id={}
y_label=[]
x_train=[]
image_dir=os.path.join(BASE_DIR,"image")
for root,dir,files in os.walk(image_dir):
    for file in files:
        if file.endswith("png")or file.endswith("jpg")or file.endswith("JPEG"):
            path=os.path.join(root,file)
            label=os.path.basename(root).replace(" ","-").lower()
            if not label in label_id:
                label_id[label]=current_id
                current_id+=1
            _id=label_id[label]
            # print(label_id)
            print(label, path)
            pil_image = Image.open(path).convert("L")
            size=(550,550)
            final_imag=pil_image.resize(size,Image.ANTIALIAS)
            image_array = np.array(pil_image, "uint8")
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for x, y, w, h in faces:
                roi = image_array[x:x + w, y:y + h]
                x_train.append(roi)
                y_label.append(_id)

with open('labels.pickle',"wb") as f:
    pickle.dump(label_id,f )


recognizer.train(x_train,np.array(y_label))
recognizer.save("trainer.yml")
