## Imports
import numpy as np
import cv2

def apply_point_tfrm(in_img:str, C:int, B:int):

    ## Checking if B is within our acceptable range
    while not int(B) in range(0, 255):
        break;
        print ("C is outside of the acceptable range")
        ##exit()
    
    ## Initializing variables
    global img1, out_img
    
    ## Reading our input image
    img1 = cv2.imread(in_img, -1)
    
    ## Finding size of input image and setting array for output image
    img1_shape = img1.shape
    out_img = np.empty([img1_shape[0], img1_shape[1]], dtype=np.uint64)
    
    ## Operation algorithm
    for i in range(img1_shape[0]):
        for j in range(img1_shape[1]):
            out_img[i,j] = (C*img1[i,j]) + B
            
    ## Output
    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

