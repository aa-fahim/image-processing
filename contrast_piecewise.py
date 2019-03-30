## Imports
import numpy as np
import cv2

## Function for 2.2.2 Constrast Stretching
def contrast_piecewise(image:str, a, b)->None:
    
    if(a[0] < 1 or a[1] < 1):
        raise ValueError ("vector a must be greater than 0 in both dimensions")
    
    if(b[0] < a[0] or b[1] < a[1]):
        raise ValueError("vector b must be greater than vector a in both dimensions")
    
    ## Initialize global variables
    global x, img, img_size, out_img
    
    ## Read input image
    x = cv2.imread(image, 0)
    ## Set the image variable to another, change data type to 64 bits to prevent overflow and modulo
    img = np.array(x, dtype=np.uint64)  
    ## Determine image size
    img_size = img.shape
    # Define output levels
    L = 255
    # Define slopes of lines
    # Slope of first linear line
    m1 = (a[1] - 0) / (a[0] - 0)
    # Slope of second linear line
    m2 = (b[1] - a[1]) / (b[0] - a[0])
    # Slope of third linear line
    m3 = (L - b[1]) / (L - b[0])
    
    ## Apply transformation stated in 2.2.2 of Assignment 1 document
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            
            if(img[i,j] <= a[0]):
                img[i,j] = m1 * img[i,j]

            elif(img[i,j] >= b[0]):
                img[i,j] = b[1] + (m3 * (img[i,j] - b[0]))
                
            else:
                img[i,j] = a[1] + (m2 * (img[i,j] - a[0]))
                
            if(img[i,j] > 255):
                img[i,j] = 255
                
    ## Make output image of 8 bits 
    out_img = np.array(out_img, dtype=np.uint8)
    ## Display output image
    cv2.imshow("img", out_img)
    ## Press any key to close image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()   