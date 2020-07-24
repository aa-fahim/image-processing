import cv2
import numpy as np
import generate_Gaussian_kernel as g

def unsharp_mask(img:str, r :int, k:int):
    
    global image, mask, mask_size, out_img, out_img1, image_size
    
    
    ## Finding dimenions of Gaussian mask and standard deviation(sigma)
    mask_size = (2*r) + 1
    sigma = r/3
    
    ## Creating Gaussian filter mask
    mask = g.generate_Gaussian_kernel((mask_size, mask_size), sigma)
    
    ## Reading input image and setting dimenions of output image
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    image_size = image.shape   
    out_img = image.copy()
    out_img1 = out_img.copy()
    
    
    ## Applying Gaussian filter
    for i in np.arange(r, image_size[0] - r):
        for j in np.arange(r, image_size[1] - r):
            sum = 0
            for k in np.arange(-r, r + 1):
                for l in np.arange(-r, r + 1):
                    a = image.item(i+k, j+l)
                    b = mask[r+k, r+l]
                    sum = sum + (a*b)
            c = sum
            out_img.itemset((i,j), c)
    
    ## Subtracting blurred image from input image then multiplying by a factor 
    ## and re-adding to input image
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            d = image.item(i,j) + k*(image.item(i,j) - out_img.item(i,j))
            out_img1.itemset((i,j), d) 
    
    cv2.imshow('image', out_img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
                    
                    
            
            
