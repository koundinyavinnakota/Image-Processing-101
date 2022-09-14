import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# converts the numpy array back to PIL image (so that you can save them back to disk). 
def arrayToImage(I):
    img = Image.fromarray(np.uint8(I))
    return img
  

#Ths function plots the required row on the scanline
def scanLine(imgArray,row):
    temp = imgArray[row,:]
    r, g, b = list(imgArray[row,:,0]), list(imgArray[row,:,1]),list(imgArray[row,:,2])
    plt.plot(r,'-',color='red')
    plt.plot(g,'-',color='green')
    plt.plot(b,'-',color='blue')
    plt.savefig('Resources/1_scanline.png')
    

#To stack the three color channels vertically
def verticalStack(imgArray):
    r_channel = imgArray[:,:,0]
    g_channel = imgArray[:,:,1]
    b_channel = imgArray[:,:,2]

    final_img_arr = np.vstack((r_channel,g_channel,b_channel))
    final_img = arrayToImage(final_img_arr)
    final_img.save("Resources/2_concat.png")

#Swapping the color channels red to green and vice versa.
def swapChannels(imgArray):
    temp = imgArray[:,:,1]
    imgArray[:,:,1] = imgArray[:,:,0]
    imgArray[:,:,0] = temp
    

    final_img = arrayToImage(imgArray)
    final_img.save("Resources/3_swapchannel.png")

# RGB to Grayscale conversion 
def rgbToGrayscale(imgArray):
    r_channel = imgArray[:,:,0]
    g_channel = imgArray[:,:,1]
    b_channel = imgArray[:,:,2]

    Grayscale_img = b_channel* 0.2126 + g_channel * 0.7152 + r_channel * 0.0722
    # print(Average_Gray)
    final_img = arrayToImage(np.uint8(Grayscale_img))
    final_img.save("Resources/4_grayscale.png")


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

# Average method
def average(imgArray):
    r_channel = imgArray[:,:,0]
    g_channel = imgArray[:,:,1]
    b_channel = imgArray[:,:,2]
    Average_Gray = (b_channel + g_channel + r_channel)/3
    # print(Average_Gray)
    final_img = arrayToImage(Average_Gray)
    final_img.save("Resources/5_grayscale.png")


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

    scanLine(I,250)
    verticalStack(I)
    swapChannels(I)
    rgbToGrayscale(I)
    average(I)
    negativeImageConverter(I)
    cropRotateStack(I)
    imgMask(I)
    maskRGBValues(I)
    nonMax(I)


