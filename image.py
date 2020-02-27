import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('nitesh.jpg',0)
# cv2.imwrite('shiva.png',img)
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

# cv2.imshow('image',img)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # to hide tick values on X and Y axis
plt.show()


key = cv2.waitKey(0)
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('shiva1.png',img)
    cv2.destroyAllWindows()
