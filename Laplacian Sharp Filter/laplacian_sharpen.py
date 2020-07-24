import cv2
import numpy as np
import generate_Gaussian_kernel as g

def laplacian_sharpen(img:str, k:int):
    global image, blurred_image, laplacian_img, image_size, laplacian_filter

    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    image_size = image.shape
    
    ## Creating Gaussian filter mask for pre-filtering
    mask = np.zeros([3,3],dtype=np.double)
    mask = g.generate_Gaussian_kernel((3, 3), 1)
    blurred_image = image.copy()
    
    ## Creating Laplacian filter
    laplacian_img = image.copy()
    laplacian_filter = np.zeros([3,3],dtype=np.double)
    for i in range(3):
        for j in range(3):
            laplacian_filter[i,j] = -abs(k)   
    laplacian_filter[1,1] = abs(k) + 8
    
    ## Applying Gaussian filter to input image
    for i in np.arange(1, image_size[0] - 1):
        for j in np.arange(1, image_size[1] - 1):
            sum = 0
            for k in np.arange(-1, 2):
                for l in np.arange(-1, 2):
                    a = image.item(i+k, j+l)
                    b = mask[1+k, 1+l]
                    sum = sum + (a*b)
            c = sum
            blurred_image.itemset((i,j), c)
    
    ## Applying Laplacian sharpening filter to blurred image
    for i in range(1, image_size[0]-1):
        for j in range(1, image_size[1]-1):
            sum = 0
            for k in range(-1, 2):
                for l in range(-1, 2):
                    a = blurred_image.item(i+k, j+l)
                    w = laplacian_filter[1+k, 1+l]
                    sum = sum + (w*a)
            b = sum
            laplacian_img.itemset((i,j), b)
            
    cv2.imshow('input image', image)
    cv2.imshow('blurred image', blurred_image)
    cv2.imshow('sharpened image', laplacian_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()