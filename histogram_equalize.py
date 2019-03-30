import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

def histogram_equalize(img)-> None:
    
    global image, out_img, hist, cum_hist
    
    ## Finding size and total pixels of input image
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    image_size = image.shape
    pixels = image_size[0] * image_size[1]
    
    ## Creating Initial Histogram
    hist = np.zeros((256))
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            a = image.item(i,j)
            hist[a] += 1
    
    ## Finding Cumulative Histogram
    cum_hist = hist.copy()
    for i in np.arange(1, 256):
        cum_hist[i] = cum_hist[i-1] + cum_hist[i]
    
    ## Equalizing Histogram and Setting Output Image    
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            a = image.item(i,j)
            b = math.floor(cum_hist[a] * 255.0 / pixels)
            image.itemset((i,j), b)                   

    
    ## Plotting Histogram
    plt.hist(image.ravel(), 256, [0,256])
    plt.show()
    
    cv2.imshow('image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()