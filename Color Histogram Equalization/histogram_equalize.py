## Assignment 5
## Problem 3.1.3
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Imports
import numpy as np
import cv2
from matplotlib import pyplot as plt
import math
import histogram as h
import cum_hist as c_h

def histogram_equalize(image)-> None:
    
    global img, out_img, hist, cum_hist, B_equalized, G_equalized, R_equalized
    
     ## Reading our input image
    x = cv2.imread(image);  img = np.array(x,dtype = np.uint8);    image_size = img.shape   
    
    ## Creating output image and arrays for RGB equalized components
    out_img = np.zeros([image_size[0], image_size[1], 3],dtype = np.uint8)
    B_equalized = np.zeros([image_size[0], image_size[1]],dtype = np.uint8)
    G_equalized = np.zeros([image_size[0], image_size[1]],dtype = np.uint8)
    R_equalized = np.zeros([image_size[0], image_size[1]],dtype = np.uint8)
    
    ## Assigning RGB components to respective variables
    B = img[:,:,0];     G = img[:,:,1];     R = img[:,:,2]
    
    ## Finding total pixels of input image
    pixels = image_size[0] * image_size[1]
    
    ## Creating Initial Histogram
    B_hist = h.histogram(B, image)
    G_hist = h.histogram(G, image)
    R_hist = h.histogram(R, image)
    
    ## Finding Cumulative Histogram
    B_cum = c_h.cum_hist(B_hist)
    G_cum = c_h.cum_hist(G_hist)
    R_cum = c_h.cum_hist(R_hist)
    
    ## Equalizing RGB components  
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            a = img.item(i,j, 0)
            b = math.floor(B_cum[a] * 255.0 / pixels)
            B_equalized.itemset((i,j), b)

            c = img.item(i,j, 1)
            d = math.floor(G_cum[c] * 255.0 / pixels)
            G_equalized.itemset((i,j), d)
            
            e = img.item(i,j, 2)
            f = math.floor(R_cum[e] * 255.0 / pixels)
            R_equalized.itemset((i,j), f)
                   
    ## Assigning equalized RGB components to output image
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            out_img[i,j,0] = B_equalized[i,j]
            out_img[i,j,1] = G_equalized[i,j]
            out_img[i,j,2] = R_equalized[i,j]
        
    ## Plotting Equalized Histogram of RGB components
    plt.hist(B_equalized.ravel(), 256, [0,256])
    plt.show()
    plt.hist(G_equalized.ravel(), 256, [0,256])
    plt.show()
    plt.hist(R_equalized.ravel(), 256, [0,256])
    plt.show()
    
    ## Showing and writing output image
    cv2.imshow('image', out_img)
    cv2.imwrite('output.png', out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()