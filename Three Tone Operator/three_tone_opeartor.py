import cv2
import math
import numpy as np

def f(img:str, t1:int, t2:int, phi_constant:int):
    
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    image = np.array(image, dtype = np.double)
    
    image_size = image.shape
    
    out_img = image.copy()
    
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            a = 0
            b = 0
            if (image[i,j] > t2):
                out_img[i,j] = 255
            elif (image[i,j] > t1):
                a = phi_constant*(image[i,j] - t2)
                b = 255 + 255*math.tanh(a)
                out_img[i,j] = b
            else:
                a = phi_constant*(image[i,j] - t1)
                b = 255 + 255*math.tanh(a)
                out_img[i,j] = b
                
    cv2.imshow('three tone result image', out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("threetone _output.png", out_img)
