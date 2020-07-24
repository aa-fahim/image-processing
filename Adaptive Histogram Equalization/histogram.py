import numpy as np

def histogram(img:str)->None:
    global image_size
    image = img.copy()
    image_size = image.shape
    
    hist = np.zeros((256))
    for i in np.arange(image_size[0]):
        for j in np.arange(image_size[1]):
            a = image.item(i,j)
            hist[a] += 1
    return hist

