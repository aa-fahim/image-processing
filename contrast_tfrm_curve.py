## Imports
import numpy as np
import cv2

def contrast_tfrm_curve(img:str, LUT:str):
    
    ## Initializing variables
    global image, image_shape, out_img 
    
    ## Reading LUT 
    array = []
    with open(LUT) as f:
        for line in f:
            array.append(line)
    
    ## Reading Input Image
    image = cv2.imread(img, -1)
    
    ## Finding size of input image and setting size of output image
    image = np.array(image)
    image_shape = image.shape
    out_img = np.empty([image_shape[0], image_shape[1]], dtype=np.uint8)
   
    ## Operation Algorithm
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            for k in range(255):
                if image[i,j]==k:
                    out_img[i,j]=array[k]
    
    ## Output 
    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   