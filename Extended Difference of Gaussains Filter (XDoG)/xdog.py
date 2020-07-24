import cv2
import convolve as c
import generate_Gaussian_kernel as g

def xdog(img:str, std_deviation:int, k:int, p:int):
    global image, first_mask_size
    
    image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    
    ## im_g = cv2.im2double(image)
    
    first_mask_size = round((2*3*std_deviation) + 1)
    first_kernel = g.generate_Gaussian_kernel(shape=
        (first_mask_size,first_mask_size),sigma=std_deviation)
        
    blur_strength = k * std_deviation
    second_mask_size = round((2*3*blur_strength) + 1)
    second_kernel = g.generate_Gaussian_kernel(shape=
        (second_mask_size,second_mask_size),sigma=blur_strength)
    
    
    first_blurred_img = image.copy()
    second_blurred_img = image.copy()
    out_img = image.copy()
    
    first_blurred_img = c.convolve(image, first_kernel)
    second_blurred_img = c.convolve(image, second_kernel)
    
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            out_img[i,j] = ((1+p)*first_blurred_img[i,j]) 
            - (p*second_blurred_img[i,j])
            
    
    
    cv2.imshow('first blurred image', first_blurred_img)
    cv2.imshow('second blurred image', second_blurred_img)
    cv2.imshow('sharpend result', out_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
    
    ## out = np.zeros([image_shape[0],image_shape[1]],dtype=np.double)