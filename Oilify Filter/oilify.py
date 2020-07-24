import cv2
import numpy as np
from math import floor 

def oilify(img:str, N, R:int, γ:int):

    ## Read input image
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    
    ## Finding height and width of image
    image_size = image.shape
    
    ## Initializing output image of same size of input image
    out_img = image.copy()
    
    ## Finding radius of window size
    radius = R//2
    
    for i in range(radius, image_size[0]-radius):
        for j in range(radius, image_size[1]-radius):
            ## Initialize arrays h and acc for local histogram
            h = np.zeros(N)
            acc =  np.zeros(N)
            ## Finding local histogram
            for k in range(-radius, radius+1):
                for l in range(-radius, radius+1):
                    x = floor((image[i+k,j+l]/255)*(N-1))
                    h[x] = h[x] + 1
                    acc[x] = acc[x] + image[i+k, j+l]
            ## Finding max of local histogram
            h_max = max(h)
            ## Initialize A and B variables to 0
            A = 0
            B = 0
            ## Setting value of output image
            for m in range(0, N-1):
                if (h[m] != 0):
                    w = (h[m]/h_max)**γ
                    B = B + w
                    A = A + w*((acc[m])/(h[m]))
                    out_img[i,j] = A/B
                    
    
    cv2.imshow('original', image)
    cv2.imshow('oil painting', out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("oil_paint_version.jpg", out_img)

    
            