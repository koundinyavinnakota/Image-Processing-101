import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# converts the numpy array back to PIL image (so that you can save them back to disk). 
def arrayToImage(I):
    img = Image.fromarray(np.uint8(I))
    return img


def nonMax(imgArray):
    r_channel = imgArray[:,:,0]
    g_channel = imgArray[:,:,1]
    b_channel = imgArray[:,:,2]
    grayscale = (r_channel + g_channel + b_channel)//3
    # average = int(average)
    rows,cols = grayscale.shape
    new_img = np.zeros([rows,cols],dtype = np.uint8)
 
    for i in range(0,rows-4):
        for j in range(0,cols-4):
            window = grayscale[i:i+5,j:j+5]
            max = np.amax(window) 
            index = np.where(window == max)
            new_img[i:i+5,j:j+5][index] = 255

   
    final_img = arrayToImage(new_img)
    final_img.save("Resources/10_nonmax.png")


if __name__ == "__main__":  
    relative_path = os.path.dirname(__file__)
    # parent_folder = os.path.dirname(relative_path)
    resources_path = os.path.join(relative_path,"Resources/")
    if os.path.exists(resources_path) != True:

        os.mkdir(resources_path)

    I = np.array(Image.open('Utils/iribefront.jpg'))
    nonMax(I)