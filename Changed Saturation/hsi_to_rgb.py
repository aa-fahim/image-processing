## Assignment 5
## Problem 3.1.2
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Import numpy for array operations
import numpy as np

## Import OpenCV to load and display images and histograms
import cv2

## For plotting histograms
from matplotlib import pyplot as plt

## For math functions
from math import exp, pi, floor, cos

## Function for 3.1.2
def hsi_to_rgb(image:str):
    
    global x,img,img_size,B,G,R,H,S,I,output
    
    img = np.array(image,dtype = np.double);    img_size = img.shape
    H = (2*pi)*img[:,:,0]/255.0;     S = img[:,:,1]/255.0;     I = img[:,:,2]/255.0
    B = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    G = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    R = np.zeros([img_size[0], img_size[1]],dtype = np.double)
    output = np.zeros([img_size[0], img_size[1], 3],dtype = np.double)
    
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            
            if(H[i,j] >= 0 and H[i,j] < pi*(2.0/3.0)):
                B[i,j] = I[i,j]*(1-S[i,j])
                R[i,j] = I[i,j] + (I[i,j]*S[i,j]*cos(H[i,j]))/cos((pi/3.0) - H[i,j])
                G[i,j] = 3*I[i,j] - R[i,j] - B[i,j]
            
            elif(H[i,j] >= pi*(2.0/3.0) and H[i,j] < pi*(4.0/3.0)):
                Hprime = H[i,j] - pi*(2.0/3.0)
                R[i,j] = I[i,j]*(1-S[i,j])
                G[i,j] = I[i,j] + (I[i,j]*S[i,j]*cos(Hprime))/cos((pi/3.0) - Hprime)
                B[i,j] = 3*I[i,j] - R[i,j] - G[i,j]
                
            elif(H[i,j] >= pi*(4.0/3.0)):
                Hdoubleprime = H[i,j] - pi*(4.0/3.0)
                G[i,j] = I[i,j]*(1-S[i,j])
                B[i,j] = I[i,j] + (I[i,j]*S[i,j]*cos(Hdoubleprime))/cos((pi/3.0) - Hdoubleprime)           
                R[i,j] = 3*I[i,j] - B[i,j] - G[i,j]
    
    R = R*255.0
    B = B*255.0
    G = G*255.0
    
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            if(R[i,j] > 255.0):
                R[i,j] = 255.0
            if(B[i,j] > 255.0):
                B[i,j] = 255.0
            if(G[i,j] > 255.0):
                G[i,j] = 255.0
            output[i,j,0] = B[i,j]
            output[i,j,1] = G[i,j]
            output[i,j,2] = R[i,j]

    R = np.array(R,dtype=np.uint8)  
    G = np.array(G,dtype=np.uint8)
    B = np.array(B,dtype=np.uint8)
    output = np.array(output,dtype=np.uint8)

    return output
    