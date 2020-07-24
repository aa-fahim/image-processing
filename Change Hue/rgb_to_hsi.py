## Assignment 5
## Problem 3.1.1
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Import numpy for array operations
import numpy as np

## Import OpenCV to load and display images and histograms
import cv2

### For plotting histograms
#from matplotlib import pyplot as plt

## For math functions
from math import acos, sqrt, radians, pi

from copy import deepcopy

## Function for 3.1.1
def rgb_to_hsi(image:str):
    
    global x,img,img_size,B,G,R,H,S,I,output,H_im,S_im,I_im
    
    img = np.array(image,dtype = np.double);    img_size = img.shape
    B = img[:,:,0]/255.0;     G = img[:,:,1]/255.0;     R = img[:,:,2]/255.0
    B_orig = img[:,:,0];     G_orig = img[:,:,1];     R_orig = img[:,:,2]
    H = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    S = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    I = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    H_im = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    S_im = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    I_im = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    output = np.zeros([img_size[0], img_size[1], 3],dtype = np.double)
    
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            if(((R[i,j] - G[i,j])**2) + ((R[i,j] - B[i,j])*(G[i,j] - B[i,j])) == 0.0):
                H[i,j] = 2*pi
            elif(B[i,j] <= G[i,j]):
                H[i,j] = acos(((R[i,j] - G[i,j]) + (R[i,j] - B[i,j]))/(2*sqrt(((R[i,j] - G[i,j])**2) + ((R[i,j] - B[i,j])*(G[i,j] - B[i,j])))))
            elif(B[i,j] > G[i,j]):
                H[i,j] = 2*pi - acos(((R[i,j] - G[i,j]) + (R[i,j] - B[i,j]))/(2*sqrt(((R[i,j] - G[i,j])**2) + ((R[i,j] - B[i,j])*(G[i,j] - B[i,j])))))
            minimum = 0.0
            if(R[i,j] == B[i,j] == G[i,j]):
                minimum = R[i,j]
            elif(R[i,j] < B[i,j] and R[i,j] < G[i,j]):
                minimum = R[i,j]
            elif(B[i,j] < R[i,j] and B[i,j] < G[i,j]):
                minimum = B[i,j]
            elif(G[i,j] < R[i,j] and G[i,j] < B[i,j]):
                minimum = G[i,j]
            elif(R[i,j] == B[i,j] and R[i,j] < G[i,j]):
                minimum = R[i,j]
            elif(G[i,j] == B[i,j] and G[i,j] < R[i,j]):
                minimum = G[i,j]
            elif(R[i,j] == G[i,j] and R[i,j] < B[i,j]):
                minimum = R[i,j]
            I[i,j] = (R[i,j] + B[i,j] + G[i,j])/3.0 
            if(I[i,j] != 0.0):
                S[i,j] = 1 - minimum/I[i,j]
            else:
                S[i,j] = 1.0
        
    
    H_im = deepcopy(H); H_im = H_im*255.0/(2*pi)
    S_im = deepcopy(S); S_im = S_im*255.0
    I_im = deepcopy(I); I_im = I_im*255.0
    
    H_im = np.array(H_im, dtype=np.uint8)
    S_im = np.array(S_im, dtype=np.uint8)
    I_im = np.array(I_im, dtype=np.uint8)
    
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            output[i,j,0] = H_im[i,j]
            output[i,j,1] = S_im[i,j]
            output[i,j,2] = I_im[i,j]
    
    output = np.array(output,dtype=np.uint8)
    
    return output