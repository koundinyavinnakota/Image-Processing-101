import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# converts the numpy array back to PIL image (so that you can save them back to disk). 
def arrayToImage(I):
    img = Image.fromarray(np.uint8(I))
    return img


#Creating a mask according to the given criteria
def imgMask(imgArray):
    rows,cols,channels = imgArray.shape
    new_img = np.zeros([rows,cols,channels],dtype = np.uint8)

    new_img[np.where(imgArray>127)] = 255
    final_img = arrayToImage(new_img)
    final_img.save("Resources/8_mask.png")

def maskRGBValues(imgArray):
    temp_array = np.where(imgArray>127)

    red_arr =imgArray[temp_array][0]
    green_arr =imgArray[temp_array][1]
    blue_arr =imgArray[temp_array][2]
    print("Red Chanel: ", np.mean(red_arr))
    print("Green Chanel: ", np.mean(green_arr))
    print("Blue Chanel: ", np.mean(blue_arr))


if __name__ == "__main__":  
    relative_path = os.path.dirname(__file__)
    # parent_folder = os.path.dirname(relative_path)
    resources_path = os.path.join(relative_path,"Resources/")
    if os.path.exists(resources_path) != True:

        os.mkdir(resources_path)

    I = np.array(Image.open('Utils/iribefront.jpg'))
    imgMask(I)
    maskRGBValues(I)