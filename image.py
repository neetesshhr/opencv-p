import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('shiva.png')

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OM NAMAH SHIVAY',(10,500), font, 4,(255,255,255),6,cv2.LINE_AA)



# cv2.imwrite('shiva.png',img)

cv2.namedWindow('image',cv2.WINDOW_NORMAL)

cv2.imshow('image',img)


# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
# plt.show()


key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('shiva1.png',img)
    cv2.destroyAllWindows()
