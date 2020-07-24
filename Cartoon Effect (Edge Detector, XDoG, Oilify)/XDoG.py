## Assignment 4
## Problem 3.1.1.1
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Import numpy for array operations
import numpy as np

## Import OpenCV to load and display images and histograms
import cv2

### For plotting histograms
#from matplotlib import pyplot as plt

## For math functions
from math import exp, pi, floor

## Function for 3.1.1.1
def xdog(image:str, r:float, k:float, p:float):
    
    ## Initialize global variables
    global x,img,img_size,scale,sigma,dev2,radius1,radius2,mask1,mask1_size,mask2,mask2_size
    global Gsigma,Gksigma,Edge_Map,output
    
    ## Read input image
    x = cv2.imread(image, 0)
    
    ## Set the image variable to another, change data type to double
    img = np.array(x, dtype=np.double) 
    
    ## Determine image size
    img_size = img.shape
    
    ## Set both Gaussian radii
    sigma = r
    dev2 = k
    if(k < 0):
        raise Exception("You have entered a negative value for k. Please try again with k >= 0")
    radius1 = 3*sigma
    radius2 = 3*sigma*dev2
    
    ## Initialize both Gaussian masks
    mask1 = np.zeros([round(2*radius1 + 1), round(2*radius1 + 1)], dtype=np.double) 
    mask1_size = mask1.shape
    if(mask1_size[0] % 2 == 0 or mask1_size[1] % 2 == 0):
        raise Exception("The standard deviation you have entered has resulted in a even length/width Gaussian filter.\
                         We wish for an odd length/width Gaussian filter. Please try again with a new value for 'r'.")
    
    mask2 = np.zeros([round(2*radius2 + 1), round(2*radius2 + 1)], dtype=np.double)
    mask2_size = mask2.shape  
    if(mask2_size[0] % 2 == 0 or mask2_size[1] % 2 == 0):
        raise Exception("The standard deviation you have entered has resulted in a even length/width Gaussian filter.\
                         We wish for an odd length/width Gaussian filter. Please try again with a new value for 'k'.")
    
    ## Create both Gaussian masks
    for i in range(-round(radius1),round(radius1)+1):
        for j in range(-round(radius1),round(radius1)+1):
            mask1[i+round(radius1),j+round(radius1)] = (1.0/(2*pi*(sigma**2)))*exp(-(i**2+j**2)/(2*(sigma**2)))

    for i in range(-floor(mask2_size[0]/2),floor(mask2_size[0]/2)+1):
        for j in range(-floor(mask2_size[0]/2),floor(mask2_size[0]/2)+1):
            mask2[i+floor(mask2_size[0]/2),j+floor(mask2_size[0]/2)] = (1.0/(2*pi*((sigma*dev2)**2)))*exp(-((i**2+j**2)/(2*((sigma*dev2)**2))))     
            
    ## Make blurred output arrays
    Gsigma = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    Gksigma = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    
    ## Fill blurred output arrays
    ## Fill blurred array 1
    width = mask1_size[0]
    num_added_rows = floor(width/2.0)
    num_added_cols = floor(width/2.0)
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            for k in range(-num_added_rows, num_added_rows+1):
                for l in range(-num_added_cols, num_added_cols+1):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            Gsigma[i,j] =Gsigma[i,j] + img[i+k,j+l]*mask1[k+num_added_rows,l+num_added_cols]                    
                    except IndexError:                               
                        continue
                    
    ## Fill blurred array 2                   
    width = mask2_size[0]
    num_added_rows = floor(width/2.0)
    num_added_cols = floor(width/2.0)
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            for k in range(-num_added_rows, num_added_rows+1):
                for l in range(-num_added_cols, num_added_cols+1):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            Gksigma[i,j] =Gksigma[i,j] + img[i+k,j+l]*mask2[k+num_added_rows,l+num_added_cols]                    
                    except IndexError:                               
                        continue
    
    ## Create output
    scale = p
    Edge_Map = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    output = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            Edge_Map[i,j] = Gsigma[i,j] - Gksigma[i,j]
                
    ## Convert output arrays to uint8 to be displayable 
    Edge_Map = np.array(Edge_Map, dtype=np.uint8)      
    
    return Edge_Map