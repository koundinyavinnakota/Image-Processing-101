import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# converts the numpy array back to PIL image (so that you can save them back to disk). 
def arrayToImage(I):
    img = Image.fromarray(np.uint8(I))
    return img


# RGB to Grayscale conversion 
def rgbToGrayscale(imgArray):
    r_channel = imgArray[:,:,0]
    g_channel = imgArray[:,:,1]
    b_channel = imgArray[:,:,2]

    Grayscale_img = b_channel* 0.2126 + g_channel * 0.7152 + r_channel * 0.0722
    # print(Average_Gray)
    final_img = arrayToImage(np.uint8(Grayscale_img))
    final_img.save("Resources/4_grayscale.png")


if __name__ == "__main__":  
    relative_path = os.path.dirname(__file__)
    # parent_folder = os.path.dirname(relative_path)
    resources_path = os.path.join(relative_path,"Resources/")
    if os.path.exists(resources_path) != True:

        os.mkdir(resources_path)

    I = np.array(Image.open('Utils/iribefront.jpg'))
    rgbToGrayscale(I)