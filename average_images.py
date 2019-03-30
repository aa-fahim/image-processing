## Imports
import numpy as np
import cv2

def average_images(*args:str):
    
    ## Initializing variables
    global out_img, total_imgs, size_img, x, y
    
    ## Finding how many images were entered
    total_imgs = 0
    for i in args:
        total_imgs = total_imgs +1
        
    imgs = list(args) 
    
    ## Finding size of first image
    size_img = (cv2.imread(imgs[0], 0)).shape
    
    ## Setting size of arrays to be used
    x = np.empty([size_img[0], size_img[1]], dtype=np.uint32)
    y = np.empty([size_img[0], size_img[1]], dtype=np.uint32)
    
    ## Operation Algorithm
    for i in range(total_imgs):
        x = cv2.imread(imgs[i], 0)
        for j in range(size_img[0]):
            for k in range(size_img[1]):
                y[j,k] = y[j,k] + x[j,k]
    
    for i in range(size_img[0]):
        for j in range(size_img[1]):
            y[i,j] = y[i,j]/total_imgs
            
    out_img = np.array(y, dtype=np.uint8)
    
    ## Output
    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



