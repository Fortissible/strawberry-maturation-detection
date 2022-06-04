import cv2
import numpy as np
from StrawberryMaturation import *

# Wildan Fajri Alfarabi

def main():
    img = cv2.imread("maturationStage.png")
    img2 = cv2.imread("Strawberry-plant-1.jpg")
    img3 = cv2.imread("Strawberry-plant-2.jpg")
    width = int(img3.shape[1] * 60 / 100)
    height = int(img3.shape[0] * 60 / 100)
    dim = (width, height)
    img3 = cv2.resize(img3, dim, interpolation=cv2.INTER_AREA)

    (img_a,img_b,img_c) = processing(img,cv2.COLOR_BGR2LAB)
    # parameternya img,ch,lower_bias=0,upper_limit=255,kernelBlurSize=0,scaleResize
    img,mask = rmvBackground(img,img_a,-50,245, 15)
    output = colorCoding(img)
    cv2.imwrite("colorCode1.jpg", output)

    (img_a, img_b, img_c) = processing(img2, cv2.COLOR_BGR2RGB)
    img_a = medianBlurring(img_a,33)
    img,mask = rmvBackground(img2, img_a, 15, 245, 33,70)
    output = colorCoding(img)
    cv2.imwrite("colorCode2.jpg", output)

    (img_a, img_b, img_c) = processing(img3, cv2.COLOR_BGR2LAB)
    cv2.imwrite("img3_a.jpg",img_a)
    cv2.imwrite("img3_b.jpg", img_b)
    cv2.imwrite("img3_c.jpg", img_c)
    img_b = medianBlurring(img_b, 63)
    img,msk = rmvBackground(img3, img_b, 20, 245, 33, 15)
    img,msk2 = rmvBackground(img3, img_b, -25, 125, 33, 15)
    segment = cv2.bitwise_or(msk,msk2)
    img = cv2.bitwise_and(img3,img3,mask=segment)
    width = int(img.shape[1] * 60 / 100)
    height = int(img.shape[0] * 60 / 100)
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    output = colorCoding(img)
    cv2.imwrite("colorCode3.jpg", output)

if __name__ == "__main__":
    main()

# contrast and brightness control if needed
'''
alpha = 1.3 # Simple contrast control
beta = 0    # Simple brightness control

def loops(image):
    new_img = np.zeros(image.shape, image.dtype)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_img[y,x,c] = np.clip(alpha*image[y,x,c] + beta, 0, 255)
    return new_img
'''
