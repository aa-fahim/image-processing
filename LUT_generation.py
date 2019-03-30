## Imports
import numpy as np
import cv2

def contrast_stretch(img:str):
    
    global image, image_shape
    
    image = cv2.imread(img, -1)
    image = np.array(image)
    image_shape = image.shape
  
    T = np.array [256]
    
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
           T[i] = 255*((image[i,j]/difference)-(r_min/difference)) 

    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)