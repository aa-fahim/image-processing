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
from rgb_to_ycbcr import rgb_to_ycbcr
from ycbcr_to_rgb import ycbcr_to_rgb

def histogram_equalize(image)-> None:
    
    global img, out_img, Yprime_hist, Yprime_cum_hist
    
     ## Reading our input image
    x = cv2.imread(image);  img = np.array(x,dtype = np.uint8);    image_size = img.shape   
    
    ## Creating output image and Array for Y'CbCr histogram equalized values
    out_img = np.zeros([image_size[0], image_size[1], 3],dtype = np.uint8)
    Ycbcr_equalized = np.zeros([image_size[0], image_size[1]],dtype = np.uint8)
    
    ## Finding total pixels of input image
    pixels = image_size[0] * image_size[1]
    
    ## Retrieving ycbcr image and yprime 
    Ycbcr_image = rgb_to_ycbcr(image)
    Yprime = Ycbcr_image[:,:,0];
    
    ## Initial Yprime histogram plot, rest continued later 
    plt.subplot(2,1,1)
    plt.title("Yprime input")
    plt.hist(Yprime.ravel(), 256, [0,256])
    cv2.imshow('Y before equalization', Ycbcr_image)
        
    ## Creating Histogram
    Yprime_hist = h.histogram(Yprime, image)
    
    ## Finding Cumulative Histogram
    Yprime_cum_hist = c_h.cum_hist(Yprime_hist)
    
    ## Equalizing Histogram and Setting Output Image    
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            a = Ycbcr_image.item(i,j, 0)
            b = math.floor(Yprime_cum_hist[a] * 255.0 / pixels)
            Ycbcr_equalized.itemset((i,j), b)
    
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            Ycbcr_image[i,j,0] = Ycbcr_equalized[i,j]
    
    ## Converting Y'CbCr image back to RGB
    out_img = ycbcr_to_rgb(Ycbcr_image)
    
    ## Setting initial RGB and equalized RGB values for histogram plots
    B = out_img[:,:,0];     G = out_img[:,:,1];     R = out_img[:,:,2]
    B_in = img[:,:,0];     G_in = img[:,:,1];     R_in = img[:,:,2]
              
    ## Plotting Histograms of Yprime before and 
    ## after histogram equalization
    plt.subplot(2,1,2)
    plt.title("Yprime output")
    plt.hist(Ycbcr_equalized.ravel(), 256, [0,256])
    plt.show()
    
    ## Plotting Histograms of RGB before histogram equalization
    plt.subplot(2,3,1)
    plt.title("B input")
    plt.hist(B_in.ravel(), 256, [0,256])
    plt.subplot(2,3,2)
    plt.title("G input")
    plt.hist(G_in.ravel(), 256, [0,256])
    plt.subplot(2,3,4)
    plt.title("R input")
    plt.hist(R_in.ravel(), 256, [0,256])
    plt.show()
    
    ## Plotting Histograms of RGB after histogram equalization
    plt.subplot(2,3,1)
    plt.title("B output")
    plt.hist(B.ravel(), 256, [0,256])
    plt.subplot(2,3,2)
    plt.title("G output")
    plt.hist(G.ravel(), 256, [0,256])
    plt.subplot(2,3,4)
    plt.title("R output")
    plt.hist(R.ravel(), 256, [0,256])
    plt.show()

    ## Writing output image  
    cv2.imwrite('Y_after_equalization.png', Ycbcr_image)
    cv2.imwrite('Output_image_RGB_space.png', out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()