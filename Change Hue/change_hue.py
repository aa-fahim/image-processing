## Assignment 5
## Problem 3.1.3
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Imports
import cv2
import numpy as np
from rgb_to_hsi import rgb_to_hsi
from hsi_to_rgb import hsi_to_rgb

def change_hue(image:str, hue_angle:int):
    ''' hue_angle must be given in degrees'''
    
    global x, img, img_size, hue, hsi, rgb_output
    
    ## Reading input image
    x = cv2.imread(image);  img = np.array(x,dtype = np.double);    img_size = img.shape
    
    ## Confirming and adjusting hue so it is within range of [0, 360]
    hue = hue_angle
    if (hue>360):
        hue = hue % 360;
    elif (hue <0):
        hue = (hue % 360) + 360;
    
    ## Converting to HSI space
    hsi = rgb_to_hsi(img)
    
    ## Applying change in hue to output image
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            hsi[i, j, 0] = (((hsi[i, j, 0]/255.0) + (hue/360.0)) % 1.0) *255.0  
    
    ## Converting back into RGB space
    rgb_output = hsi_to_rgb(hsi)
    
    ## Showing and writing output image
    cv2.imshow('rgb image with hue changed', rgb_output)
    cv2.imwrite('changed_hue_output.jpg', rgb_output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
        