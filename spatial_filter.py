import numpy as np
import cv2
import math

def spatial_filter(img:float, h)->None:
    
    global image, x, image_size, size_mask, out_img, image_padded, weighted_pixel_sum
    
    ## Convert color image to grayscale
    x = cv2.imread(img, cv2.IMREAD_GRAYSCALE).astype('float')/255.0
    
    ## Finding size of image
    image = np.array(x)
    image_size = image.shape

    ## Reading matrix file and finding size
    mask = np.loadtxt(h, dtype='i', delimiter=', ')
    size_mask = mask.shape
    mask_sum = mask.sum()
    
    ## Padding image with zeros
    ##image_padded=np.zeros((image.shape[0]+size_mask[0], image.shape[1]+size_mask[1]))
    
    ## Setting output image
    out_img=np.zeros([image.shape[0], image.shape[1]])
    
    ## Applying spatial filter
    for i in range(image_size[0]):
        for j in range(image_size[1]):
            weighted_pixel_sum = 0
                       
            for k in range(-math.floor(size_mask[0]/2), (size_mask[0]-1)):
                for l in range(-math.floor(size_mask[1]/2), (size_mask[1]-1)):
                    pixel = 0
                    pixel_x = i - k
                    pixel_y = j - l
                    
                    if (pixel_x >= 0) and (pixel_x < image_size[0]) and (pixel_y >=0) and (pixel_y < image_size[1]):
                        pixel = image[pixel_y, pixel_x]
                    
                    weight = mask[k + (size_mask[0]/2) ,l + (size_mask[1]/2)]
                    weighted_pixel_sum += pixel * weight
            
            out_img[i, j] = weighted_pixel_sum / mask_sum
     
    ## Output
    cv2.imshow("img", out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()   