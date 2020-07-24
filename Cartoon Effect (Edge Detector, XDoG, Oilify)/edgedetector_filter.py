## Assignment 4
## Problem 3.2.2
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Import numpy for array operations
import numpy as np

## Import OpenCV to load and display images and histograms
import cv2

### For plotting histograms
#from matplotlib import pyplot as plt

## For math functions
from math import exp, pi, floor, sqrt

## Function for 3.2.2
def edgedetector_filter(image:str):
    
    ## Initialize global variables
    global img,img_size,Sobel,Sobel2
    global output1,output2,out_img_temp,output
    
    ## Read input image
    x = cv2.imread(image, 0)
    
    ## Set the image variable to another, change data type to double
    img = np.array(x, dtype=np.uint8) 
    
    ## Determine image size
    img_size = img.shape
    
    ## Make edge detector mask
    Sobel = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
    Sobel2 = Sobel.T
            
    ## Initialize output arrays
    output1 = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    output2 = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    out_img_temp = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    output = np.zeros([img_size[0],img_size[1]],dtype=np.double)
    
    ## Convolve vertical mask and input image
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            for k in range(-1, 2):
                for l in range(-1, 2):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            output1[i,j] = output1[i,j] + img[i+k,j+l]*Sobel[k+1,l+1]                    
                    except IndexError:                               
                        continue
    
    ## Convolve horizontal mask and input image
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            for k in range(-1, 2):
                for l in range(-1, 2):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            output2[i,j] = output2[i,j] + img[i+k,j+l]*Sobel2[k+1,l+1]                    
                    except IndexError:                               
                        continue   
    
    ## Fill output with gradient magnitude                
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            out_img_temp[i,j] = sqrt(output1[i,j]**2 + output2[i,j]**2)

    ## For scaling to [0,255]                          
    minimum = np.amin(out_img_temp)
    if(minimum < 0):
        for i in range(img_size[0]):
            for j in range(img_size[1]):
                output[i,j] = out_img_temp[i,j] + minimum
    else:
        for i in range(img_size[0]):
            for j in range(img_size[1]):
                output[i,j] = out_img_temp[i,j]
                
    difference = np.amax(out_img_temp) - np.amin(out_img_temp)
    if(difference > 255):
        ratio = difference/255
        for i in range(img_size[0]):
            for j in range(img_size[1]):
                output[i,j] = output[i,j]/ratio
    
    ## Threshold
    threshold = 0.05*np.amax(output)          
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            if(output[i,j] > threshold):
                output[i,j] = 255
            else:
                output[i,j] = 0
    
    output = np.array(output, dtype=np.uint8) 
    
#    ## For displaying results
#    cv2.imshow("gradient magnitude scaled", output)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    
    return output
#   cv2.imwrite("output.png", output)
    
    
    
    
    
    
 