import numpy as np
import cv2

def image_threshold(img:str, T:float):
    
    global image, image_size, x, out_img
    
    x = cv2.imread(img, cv2.IMREAD_GRAYSCALE).astype('float')/255.0
    
    image = np.array(x)
    image_size = image.shape
    
    out_img = np.zeros([image.shape[0], image.shape[1]])
    
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            if image[i,j] >= T:
                out_img[i,j] = 255
            else:
                out_img[i,j] = 0
                
    cv2.imshow("out_img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  