## Import numpy for array operations
import numpy as np

## Import OpenCV to load and display images and histograms
import cv2

## Function for Point Operation
def apply_mask(img_a:str, img_b:str, img_mask:str)->None:
        
    global img1, img2, mask, mask_shape, out_img
    
    img1 = cv2.imread(img_a, -1)    
    img2 = cv2.imread(img_b, -1)
    mask = cv2.imread(img_mask, -1)
    mask = np.array(mask)
    
    mask_shape = mask.shape
    
    out_img = np.empty([mask_shape[0], mask_shape[1]], dtype=np.uint8)
    
    for i in range(mask_shape[0]):
        for j in range(mask_shape[1]):
           if(mask[i,j] > 0):
               out_img[i,j] = img1[i,j]
               
           if(mask[i,j] == 0):
               out_img[i,j] = img2[i,j]

    cv2.imshow("img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()        
    