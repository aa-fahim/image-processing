## Imports
import numpy as np
import cv2

def contrast_highlight(img:str, A:int, B:int, I_min:int):
    
    ## Initializing variables
    global image, image_shape, out_img 
    
    ## Reading input image
    image = cv2.imread(img, -1)
    
    ## Finding size of input image and setting size of output image
    image = np.array(image)
    image_shape = image.shape
    out_img = np.empty([image_shape[0], image_shape[1]], dtype=np.uint8)
    
    ## Operation Algorithm
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
           if(image[i,j] < A):
               out_img[i,j] = I_min
           elif (image[i,j] > B):
               out_img[i,j] = I_min
           else:
               out_img[i,j] = image[i,j]
    
    ## Output
    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   
