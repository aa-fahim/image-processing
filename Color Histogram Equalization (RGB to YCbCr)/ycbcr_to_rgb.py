## Assignment 5
## Problem 3.1.4
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

## Function for 3.1.4
def ycbcr_to_rgb(img:str):
    
    global x,img_size,B,G,R,Yprime,Cb,Cr,output
    
    img_size = img.shape
    Yprime = img[:,:,0];     Cb = img[:,:,1];     Cr = img[:,:,2]
    B = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    G = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    R = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    output = np.zeros([img_size[0], img_size[1], 3],dtype = np.double)
    
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            R[i,j] = 1.0*Yprime[i,j] + 1.402*(Cr[i,j]-128)
            G[i,j] = 1.0*Yprime[i,j] - 0.34414*(Cb[i,j]-128) - 0.71414*(Cr[i,j]-128)
            B[i,j] = 1.0*Yprime[i,j] + 1.772*(Cb[i,j]-128)
            
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            output[i,j,0] = B[i,j]
            output[i,j,1] = G[i,j]
            output[i,j,2] = R[i,j]
    
    return output
    