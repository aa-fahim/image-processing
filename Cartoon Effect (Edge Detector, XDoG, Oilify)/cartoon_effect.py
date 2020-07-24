from oilify import oilify
from XDoG import xdog
import cv2
import numpy as np

original = cv2.imread("original.png", 0)
original = np.array(original, dtype=np.double)
img_size = original.shape
cartoon = np.zeros([img_size[0], img_size[1]], dtype=np.uint8)

blurred = oilify("original.png", 45, 5, 5)
edges = xdog("original.png", 1.0, 1.6, 2.0)

for i in range(img_size[0]):
    for j in range(img_size[1]):
        if(edges[i,j] > 0):
            cartoon[i,j] = 0
        else:
            if(blurred[i,j] < 236):
                cartoon[i,j] = blurred[i,j] + 20
            else:
                cartoon[i,j] = blurred[i,j]
            
cv2.imshow("cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("cartoon.png", cartoon)
