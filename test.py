import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
      ret, img = cap.read()
      cv2.imshow('frame',img)
      k = cv2.waitKey(27) & 0xFF
      if k == ord('q'):
         break



cap.release()
cv2.destroyAllWindows()
