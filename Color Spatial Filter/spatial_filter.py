## Assignment 5
## Problem 3.1.3
## Michael Santorelli 500458369 and,
## Ashif Fahim 500584641

## Imports
import numpy as np
import cv2

def spatial_filter(image:str, h:str):
    global x, img, img_size, size_mask, mask, mask_sum, a, b, c, d, e, f
    global weighted_sum_R, weighted_sum_B, weighted_sum_G
    
    ## Reading input iamge
    x = cv2.imread(image);  img = np.array(x,dtype = np.uint8);    img_size = img.shape
    
    ## Assinging RGB components to respective variables
    B = img[:,:,0];  G = img[:,:,1];   R = img[:,:,2];
    
    ## Reading mask file and finding size of filter
    mask = np.loadtxt(h, dtype='i', delimiter=', ')
    size_mask = mask.shape
    mask_sum = mask.sum()
    radius_h = size_mask[0]//2
    radius_w = size_mask[1]//2
    
    ## Creating output image
    out_img = np.zeros([img_size[0], img_size[1], 3],dtype = np.uint8) 
    
    ## Applying spatial filter to each individual RGB component and assigning to output
    for i in range(radius_h, img_size[0]-radius_h):
        for j in range(radius_w, img_size[1]-radius_w):
            weighted_sum_R = 0
            weighted_sum_G = 0
            weighted_sum_B = 0
            for k in range(-radius_h, radius_h+1):
                for l in range(-radius_w, radius_w+1):
                    a = B[i+k,j+l]*mask[radius_h+k,radius_w+l]
                    b = G[i+k,j+l]*mask[radius_h+k,radius_w+l]
                    c = R[i+k,j+l]*mask[radius_h+k,radius_w+l]
                    weighted_sum_B = weighted_sum_B + a
                    weighted_sum_G = weighted_sum_G + b
                    weighted_sum_R = weighted_sum_R + c
            d = int(weighted_sum_B/ mask_sum)
            e = int(weighted_sum_G/ mask_sum)
            f = int(weighted_sum_R/ mask_sum)
            out_img.itemset((i,j,0), d)
            out_img.itemset((i,j,1), e)
            out_img.itemset((i,j,2), f)
    
    ## Showing and writing output image
    cv2.imshow("img", out_img)
    cv2.imwrite("spatial_result.png", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   