import numpy as np
import cv2
import histogram as h
import cum_hist as c_h
import math 
from matplotlib import pyplot as plt

def adaptive_histogram(img:str, H:int, W:int)-> None:
    
    global out_img, image_size, height, width
    
    ## Finding dimensions of input image
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    image_size = image.shape
    
    ## Finding size of kernel (half of width and height)
    height = H//2
    width = W//2     
    
    ## Initializing variables to be used
    out_img = image.copy()
    hist = np.zeros(256)
    
    
    
    for i in range(height, image_size[0]-height):
        for j in range(width, image_size[1]-width):
            
            ## Creating local nieghbourhood
            kernel = image[i-height:i+height, j-width:j+width]
            
            ## Finding histogram and CDF of local neighbourhood
            hist = h.histogram(kernel)
            cum_hist = c_h.cum_hist(hist)
            
            ## Equalizing local neighbourhood and assigning to output image
            kernel_size = kernel.shape
            for k in np.arange(kernel_size[0]):
                for l in np.arange(kernel_size[1]):
                    a = kernel.item(k,l)
                    b = math.floor(cum_hist[a] * 255.0/ (kernel_size[0]*kernel_size[1]))
                    out_img[i,j]=b
         
            
    ## Plotting Histogram        
    plt.hist(out_img.ravel(), 256, [0,256])
    plt.show()
    
    cv2.imshow('image', out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
                    
                        
    
                            
                    
                  
