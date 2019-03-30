## Import 
import numpy as np
import cv2

def contrast_tfrm_curve(image:str)->None:
    
    ## Initialize global variables
    global x, img, img_size, out_img, LUT, minimum, maximum
    
    ## Read input image
    x = cv2.imread(image, 0)
    ## Set the image variable to another, change data type to 64 bits to prevent overflow and modulo
    img = np.array(x, dtype=np.uint8)  
    ## Determine image size
    img_size = img.shape
    ## Determine max and min of original image
    minimum = np.amin(img)
    maximum = np.amax(img)

    ## Make output image of 8 bits 
    out_img = np.empty([img_size[0], img_size[1]], dtype=np.uint8)
    
    ## Make empty dictionary to store LUT
    LUT = {}

    ## Create .txt file to store LUT    
    f = open("LUT.txt", "w+")
        
    for i in range(256):
        ## Write LUT
        if(i >= minimum):
            if((255.0*( ( i/ (maximum-minimum) ) - ( minimum/ (maximum - minimum) ) )) > 255):
                f.write(str(i) + " , " + str(255) + "\n")
            else:
                f.write(str(i) + " , " + str(int(255.0*( ( i/ (maximum-minimum) ) - ( minimum/ (maximum - minimum) ) ))) + "\n")

            
    ## Close file        
    f.close()       
    
    f = open("LUT.txt", "r")
        
    for line in f:
            
        LUT[int(line.split(',')[0])] = int(line.split(',')[1]) 
            
    f.close() 
            
    ## Apply transformation in LUT_generation.py file
    for i in range(img_size[0]):
        for j in range(img_size[1]):
              
            if img[i,j] in LUT:
                out_img[i,j] = LUT[img[i,j]]

    ## Display output image
    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   


          