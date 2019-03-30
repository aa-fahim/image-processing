## Imports
import numpy as np
import cv2

def contrast_stretch(img:str):
    
    ## Initializing variables
    global image, image_shape, out_img, r_min, r_max
    
    ## Reading input image
    image = cv2.imread(img, -1)
    
    ## Finding size of input image and setting size of output image
    image = np.array(image)
    image_shape = image.shape
    out_img = np.empty([image_shape[0], image_shape[1]], dtype=np.uint8)
    
    ## Finding max and min of input image
    r_min = np.amin(image)
    r_max = np.amax(image)
    difference = r_max - r_min
    
    ## Operation Algorithm
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
           out_img[i,j] = 255*((image[i,j]/difference)-(r_min/difference)) 
           
    ## Output       
    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()