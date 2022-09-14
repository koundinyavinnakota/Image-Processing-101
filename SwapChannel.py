import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# converts the numpy array back to PIL image (so that you can save them back to disk). 
def arrayToImage(I):
    img = Image.fromarray(np.uint8(I))
    return img


#Swapping the color channels red to green and vice versa.
def swapChannels(imgArray):
    temp = imgArray[:,:,1]
    imgArray[:,:,1] = imgArray[:,:,0]
    imgArray[:,:,0] = temp
    

    final_img = arrayToImage(imgArray)
    final_img.save("Resources/3_swapchannel.png")


if __name__ == "__main__":  
    relative_path = os.path.dirname(__file__)
    # parent_folder = os.path.dirname(relative_path)
    resources_path = os.path.join(relative_path,"Resources/")
    if os.path.exists(resources_path) != True:

        os.mkdir(resources_path)

    I = np.array(Image.open('Utils/iribefront.jpg'))
    swapChannels(I)