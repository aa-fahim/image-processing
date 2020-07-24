## Assignment 4
## Problem 3.2.1
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

## Function for 3.2.1
def edgepass_filter(image:str):
    
    ## Initialize global variables
    global img,img_size
    global output1,output2,output3,output4
    
    ## Read input image
    x = cv2.imread(image, 0)
    
    ## Set the image variable to another, change data type to double
    img = np.array(x, dtype=np.uint8) 
    
    ## Determine image size
    img_size = img.shape
            
    ## Initialize output arrays
    output1 = np.zeros([img_size[0],img_size[1]],dtype=np.uint8)
    output2 = np.zeros([img_size[0],img_size[1]],dtype=np.uint8)
    output3 = np.zeros([img_size[0],img_size[1]],dtype=np.uint8)
    output4 = np.zeros([img_size[0],img_size[1]],dtype=np.uint8)
    
    ## First median filter - 3x3
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            median_array = []
            for k in range(-1, 2):
                for l in range(-1, 2):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            median_array.append(img[i+k,j+l])
                            if(k == 1 and l == 1):
                                median_array.sort()
                                output1[i,j] = median_array[4]
                    except IndexError:                               
                   
                        continue
                    
    ## Second median filter - 5x5
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            median_array = []
            for k in range(-2, 3):
                for l in range(-2, 3):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            median_array.append(img[i+k,j+l])
                            if(k == 2 and l == 2):
                                median_array.sort()
                                output2[i,j] = median_array[12]
                    except IndexError:                               
                        continue  
    
    ## Third median filter - 7x7
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            median_array = []
            for k in range(-3, 4):
                for l in range(-3, 4):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            median_array.append(img[i+k,j+l])
                            if(k == 3 and l == 3):
                                median_array.sort()
                                output3[i,j] = median_array[24]
                    except IndexError:                               
                        continue    
                    
    ## Fourth median filter - 9x9
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            median_array = []
            for k in range(-4, 5):
                for l in range(-4, 5):                       
                    try:                                
                        if(i+k < 0 or i+k > img_size[0]-1 or j+l < 0 or j+l > img_size[1]-1):
                            continue
                        else:    
                            median_array.append(img[i+k,j+l])
                            if(k == 4 and l == 4):
                                median_array.sort()
                                output4[i,j] = median_array[40]
                    except IndexError:                               
                        continue        
                    
#    ## For displaying results
#    cv2.imshow("output first", output1)
#    cv2.imshow("output second", output2)
#    cv2.imshow("output third", output3)
#    cv2.imshow("output fourth", output4)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
#    
    return output4
#    cv2.imwrite("first_iteration.png", output1)
#    cv2.imwrite("second_iteration.png", output2)
#    cv2.imwrite("third_iteration.png", output3)
#    cv2.imwrite("fourth_iteration.png", output4)
    
    
    