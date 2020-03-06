import numpy as np 
import cv2

cap = cv2.VideoCapture(0)

while(True):
     #capture frame by frame
     ret,frame = cap.read()
   
     #opt on frame is here
     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
     
     #display 
     cv2.imshow('frame',gray)
     
     key = cv2.waitKey(1)
     if key & 0xFF == ord('q'):
         break



cap.release()
cv2.destroyAllWindows()
