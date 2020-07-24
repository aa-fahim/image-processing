import numpy as np

def convolve(img:str, mask):
    
    image = img
    image_size = image.shape 
    
    mask_size = mask.shape
    mask_height = mask_size[0]//2
    mask_width = mask_size[1]//2
    
    out_img = image.copy()
    
    ## Applying Gaussian filter
    for i in np.arange(mask_height, image_size[0] - mask_height):
        for j in np.arange(mask_width, image_size[1] - mask_width):
            sum = 0
            for k in np.arange(-mask_height, mask_height + 1):
                for l in np.arange(-mask_width, mask_width + 1):
                    a = image.item(i+k, j+l)
                    b = mask[mask_height+k, mask_width+l]
                    sum = sum + (a*b)
            c = sum
            out_img.itemset((i,j), c)
    return out_img
    