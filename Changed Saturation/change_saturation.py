## Assignment 5
## Problem 3.1.3
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Imports
import cv2
import numpy as np
from rgb_to_hsi import rgb_to_hsi
from hsi_to_rgb import hsi_to_rgb

def change_saturation(image:str, sat:int):
    ''' sat can be negative'''
    
    global x, img, img_size, hsi, rgb_output
    
    ## Reading input image
    x = cv2.imread(image);  img = np.array(x,dtype = np.double);    img_size = img.shape
    
    ## Confirm and adjust so sat is greater or equal to 0 and less than or 
    ## equal to 1
    if (sat > 1):
        sat = sat % 1;
    elif (sat <0):
        sat = (sat % 1) + 1;
    
    ## Converting to HSI space    
    hsi = rgb_to_hsi(img)
    
    ## Applying change in saturation to output image
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            hsi[i, j, 1] = (((hsi[i, j, 1]/255.0) + sat) % 1.0) * 255.0 
    
    ## Converting back into RGB space
    rgb_output = hsi_to_rgb(hsi)
    
    ## Showing and writing output image
    cv2.imshow('rgb image with hue changed', rgb_output)
    cv2.imwrite('changed_sat_output.jpg', rgb_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    