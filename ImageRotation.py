import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# converts the numpy array back to PIL image (so that you can save them back to disk). 
def arrayToImage(I):
    img = Image.fromarray(np.uint8(I))
    return img


# Cropping a square image, rotating it and stacking it horizontally.
def cropRotateStack(imgArray):
    squaredCropImg = imgArray[354:726,774:1146]

    rows,cols,channels = squaredCropImg.shape
    new_img_1 = np.zeros([rows,cols,channels],dtype = np.uint8)
    new_img_2 = np.zeros([rows,cols,channels],dtype = np.uint8)
    new_img_3 = np.zeros([rows,cols,channels],dtype = np.uint8)

    #Rotating it by 90degrees left
    for i in range(rows):
        for j in range(cols):
            new_img_1[i,j] = squaredCropImg[j-1,i-1]
            new_img_1 = new_img_1[0:rows,0:cols]
    
    #Rotating it by 180 degrees
    for i in range(rows):
        for j in range(cols):
            new_img_2[i,j] = squaredCropImg[rows - i-1,cols - j-1]
            new_img_2 = new_img_2[0:rows,0:cols]
    

    #Rotating it by 270 degrees left
    for i in range(rows):
        for j in range(cols):
            new_img_3[i,j] = squaredCropImg[rows - j-1,cols - i-1]
            new_img_3 = new_img_3[0:rows,0:cols]
    

    final_img_arr = np.hstack((squaredCropImg,new_img_1,new_img_2,new_img_3))
    final_img = arrayToImage(final_img_arr)
    final_img.save("Resources/7_rotation.png")


if __name__ == "__main__":  
    relative_path = os.path.dirname(__file__)
    # parent_folder = os.path.dirname(relative_path)
    resources_path = os.path.join(relative_path,"Resources/")
    if os.path.exists(resources_path) != True:

        os.mkdir(resources_path)

    I = np.array(Image.open('Utils/iribefront.jpg'))

    cropRotateStack(I)