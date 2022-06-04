import cv2
import numpy as np

def colorCoding(img):
    img = medianBlurring(img,3)
    intensityR_map = np.zeros((img.shape[0],img.shape[1]), img.dtype)
    intensityG_map = np.zeros((img.shape[0],img.shape[1]), img.dtype)
    intensityB_map = np.zeros((img.shape[0], img.shape[1]), img.dtype)
    new_image = np.zeros((img.shape[0],img.shape[1],img.shape[2]), img.dtype)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if int(img[i,j,0])+int(img[i,j,1])+int(img[i,j,2])==0 :
                intensityR_map[i, j] = 0
                intensityG_map[i, j] = 0
                intensityB_map[i, j] = 0
            else :
                intensityR_map[i,j] = int((int(img[i,j,2])/(int(img[i, j, 0]) + int(img[i, j, 1]) + int(img[i, j, 2]))) * 255)
                intensityG_map[i,j] = int((int(img[i,j,1])/(int(img[i, j, 0]) + int(img[i, j, 1]) + int(img[i, j, 2]))) * 255)
                intensityB_map[i, j] = int((int(img[i,j,0]) / (int(img[i, j, 0]) + int(img[i, j, 1]) + int(img[i, j, 2]))) * 255)
            # biru
            if intensityR_map[i,j] >140 and intensityG_map[i,j] <50 and intensityB_map[i,j]<75:
                new_image[i, j, 0] = intensityR_map[i,j]    #B
                new_image[i, j, 1] = 0                      #G
                new_image[i, j, 2] = 0                      #R
            # ungu
            elif intensityR_map[i,j] <170 and intensityR_map[i,j] >115 and intensityG_map[i,j]<90:
                new_image[i, j, 0] = intensityR_map[i,j]    #B
                new_image[i, j, 1] = 0                      #G
                new_image[i, j, 2] = intensityR_map[i,j]    #R
            # orange
            elif intensityR_map[i,j] <150 and intensityG_map[i,j] <150 and intensityG_map[i,j] >20 and intensityB_map[i,j] >50:
                new_image[i, j, 0] = 0                      #B
                new_image[i, j, 1] = 85                     #G
                new_image[i, j, 2] = 255                    #R
            # kuning
            elif intensityR_map[i,j] <150 and intensityG_map[i,j] <150 and intensityG_map[i,j] >30 and intensityB_map[i,j] <60:
                new_image[i, j, 0] = 0                      #B
                new_image[i, j, 1] = 200                    #G
                new_image[i, j, 2] = 255                    #R

    showImgResized(new_image,50)
    return new_image

def showImgResized(img,scale_percent=100):
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow("Resized image", resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def medianBlurring(ch,kernelSize):
    blurred = cv2.medianBlur(ch, kernelSize)  # image smoothing lagi
    return blurred

def rmvBackground(img,ch,lower_bias=0,upper_limit=255,kernelBlurSize=0,scaleResize=100):
    lower = np.array([int(np.average(np.ravel(ch)))+lower_bias])
    upper = np.array([upper_limit])
    mask = cv2.inRange(ch, lower, upper)
    if kernelBlurSize != 0 :
        mask = medianBlurring(mask,kernelBlurSize)
    segment = cv2.bitwise_and(img, img, mask=mask)
    showImgResized(segment,scaleResize)
    return segment,mask

def splitChannel(img):
    (img_a, img_b, img_c) = cv2.split(img)
    return img_a,img_b,img_c

def cvtColor(img,colorSpace):
    img = cv2.cvtColor(img,colorSpace)
    return img

def processing(img,colorSpace):
    img_chl_col = cvtColor(img,colorSpace)
    (a,b,c) = splitChannel(img_chl_col)
    return a,b,c