## Assignment 5
## Problem 3.1.3
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Import numpy for array operations
import numpy as np

## Import OpenCV to load and display images and histograms
import cv2

## For plotting histograms
from matplotlib import pyplot as plt

## For math functions
from math import exp, pi, floor

## Function for 3.1.3
def rgb_to_ycbcr(image:str):
    
    global x,img,img_size,B,G,R,Yprime,Cb,Cr,output
    
    x = cv2.imread(image);  img = np.array(x,dtype = np.double);    img_size = img.shape
    B = img[:,:,0];     G = img[:,:,1];     R = img[:,:,2]
    Yprime = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    Cb = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    Cr = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    output = np.zeros([img_size[0], img_size[1], 3],dtype = np.double)
    
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            Yprime[i,j] = 0.299*R[i,j] + 0.587*G[i,j] + 0.114*B[i,j] + 0
            Cb[i,j] = -0.1687*R[i,j] - 0.3313*G[i,j] + 0.5*B[i,j] + 128
            Cr[i,j] = 0.5*R[i,j] - 0.4187*G[i,j] - 0.0813*B[i,j] + 128
            output[i,j,0] = Yprime[i,j]
            output[i,j,1] = Cb[i,j]
            output[i,j,2] = Cr[i,j]
            
    Yprime = np.array(Yprime,dtype=np.uint8)  
    Cb = np.array(Cb,dtype=np.uint8) 
    Cr = np.array(Cr,dtype=np.uint8)       
    output = np.array(output, dtype=np.uint8)
    
    return output
            
            
            
            