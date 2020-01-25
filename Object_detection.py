import cv2
import numpy as np
def kuch(x):
    pass
reco=cv2.VideoCapture(0)
cv2.namedWindow("tracking")
cv2.createTrackbar("LH","tracking",0,255,kuch)
cv2.createTrackbar("Ls","tracking",0,255,kuch)
cv2.createTrackbar("Lv","tracking",0,255,kuch)
cv2.createTrackbar("Uh","tracking",255,255,kuch)
cv2.createTrackbar("Us","tracking",255,255,kuch)
cv2.createTrackbar("Uv","tracking",255,255,kuch)
while True:
   _, frame=reco.read()
   hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
   l_h=cv2.getTrackbarPos("LH","tracking")
   l_s = cv2.getTrackbarPos("Ls", "tracking")
   l_v = cv2.getTrackbarPos("Lv", "tracking")
   u_h = cv2.getTrackbarPos("Uh", "tracking")
   u_s = cv2.getTrackbarPos("Us", "tracking")
   u_v = cv2.getTrackbarPos("Uv", "tracking")
   l_b=np.array([l_h,l_s,l_v])
   l_u = np.array([u_h, u_s, u_v])
   mask=cv2.inRange(hsv,l_b,l_u)
   res=cv2.bitwise_and(frame,frame,mask=mask)
   cv2.imshow("frame",frame)
   cv2.imshow("mask", mask)
   cv2.imshow("res", res)
   key=cv2.waitKey(1)
   if key==27:
       break
reco.release()
cv2.destroyAllWindows()
