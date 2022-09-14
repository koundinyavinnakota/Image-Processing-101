import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# converts the numpy array back to PIL image (so that you can save them back to disk). 
def arrayToImage(I):
    img = Image.fromarray(np.uint8(I))
    return img


# Negative image converter from grayscale
def negativeImageConverter(imgArray):
    h,w,_ = imgArray.shape
    r_channel = imgArray[:,:,0]
    g_channel = imgArray[:,:,1]
    b_channel = imgArray[:,:,2]

    Average_Gray = b_channel//3 + g_channel//3 + r_channel//3
    for i in range(0,h-1):
        for j in range(0,w-1):

            Average_Gray[i,j] = 255 - Average_Gray[i,j]
            
    final_img = arrayToImage(Average_Gray)
    final_img.save("Resources/6_negative.png")


if __name__ == "__main__":  
    relative_path = os.path.dirname(__file__)
    # parent_folder = os.path.dirname(relative_path)
    resources_path = os.path.join(relative_path,"Resources/")
    if os.path.exists(resources_path) != True:

        os.mkdir(resources_path)

    I = np.array(Image.open('Utils/iribefront.jpg'))
    negativeImageConverter(I)