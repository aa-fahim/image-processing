import numpy as np
import cv2

def histogram(channel, img)->None:
    global image_size
    x = cv2.imread(img);
    ##image = img.copy()
    image_size = x.shape
    
    
    
    hist = np.zeros((256))
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            a = channel.item(i,j)
            hist[a] += 1
    return hist

