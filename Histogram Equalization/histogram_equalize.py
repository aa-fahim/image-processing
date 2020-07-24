import numpy as np
import cv2
from matplotlib import pyplot as plt

def histogram_equalize(image:str)->None:
    
    global x,img,img_size,hist,pdf,cdf,lin_cdf,new_cdf,bins,pdf1,cdf1,out,maximum,minimum
    
    x = cv2.imread(image, 0)
    img = np.array(x, dtype=np.uint8)
    img_size = img.shape
    
    hist,bins = np.histogram(img.ravel(),256,[0,256])
    bins = np.arange(256)
    
    pdf = np.zeros([256,1])
    for i in range(256):
        pdf[i] = hist[i]/(img_size[0]*img_size[1])
    
    cdf = np.zeros([256,1])
    for i in range(256):
        if(i == 0):
            cdf[i] = pdf[i]
        else:
            cdf[i] = cdf[i-1] + pdf[i]
    
    slope = 1.0/255.0
    lin_cdf = np.zeros([256,1])
    for i in range(256):
        lin_cdf[i] = i * slope
            
    maximum = np.amax(img)
    minimum = np.amin(img)
    L = 256
    
    out = np.zeros([img_size[0],img_size[1]],dtype=np.uint8)
    
    for i in range(img_size[0]):
        for j in range(img_size[1]):
            out[i,j] = (L-1)*((img[i,j] - minimum)/(maximum - minimum))
            
    
    hist1,bins = np.histogram(out.ravel(),256,[0,256])
    bins = np.arange(256)
    
    pdf1 = np.zeros([256,1])
    for i in range(256):
        pdf1[i] = hist1[i]/(img_size[0]*img_size[1])
    
    cdf1 = np.zeros([256,1])
    for i in range(256):
        if(i == 0):
            cdf1[i] = pdf1[i]
        else:
            cdf1[i] = cdf1[i-1] + pdf1[i]
    
    plt.subplot(2,1,1)
    plt.title("PDF of Input and Output Image")
    plt.plot(bins,pdf, label="Original PDF")
    plt.xlabel("Bin Number"); plt.ylabel("Input PDF Value")
    plt.subplot(2,1,2)
    plt.plot(bins,pdf1, label="New PDF")
    plt.xlabel("Bin Number"); plt.ylabel("Output PDF Value")
    plt.savefig("PDF.jpg")
    plt.show()
    
    
    plt.subplot(2,1,1)
    plt.title("CDF of Input and Output Image versus a Linear CDF")
    plt.plot(bins,cdf, label="Original CDF"); plt.plot(bins,lin_cdf, label="Linear CDF")
    plt.legend(loc='upper left')
    plt.xlabel("Bin Number"); plt.ylabel("CDF Value")
    plt.subplot(2,1,2)
    plt.plot(bins,cdf1, label="New CDF"); plt.plot(bins,lin_cdf, label="Linear CDF")
    plt.legend(loc='upper left')
    plt.xlabel("Bin Number"); plt.ylabel("CDF Value")
    plt.savefig("CDF.jpg")
    plt.show()
    
    cv2.imshow("in", img)
    cv2.imshow("out", out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("out_image.jpg", out)
    
    
            
            
            
            
            
            