import random
import numpy as np
from math import floor
# M=[[[210, 100, 255],[100, 50, 255],[90, 90, 255],[90, 90, 255],[90, 90, 255],[90, 80, 255]],
# [[190, 255,89],[ 201, 255,29],[200, 255,100],[100, 255,90],[20, 255,200], [100, 255,80]],
# [[255,0, 0],[ 255,0, 0],[255,0, 0],[255,0, 0],[255,0, 0], [255,0, 0]]]

# # print(M[0][1][1])
# # print(M[1][0][1])
# # print(M[2][1][0])
################## Q3 ##################
def initImageRGB(h,l):
    img=[[[random.randrange(255) for i in range(3)] for j in range(l) ]for k in range(h)]
    return img
################## Q4 ##################
def symetrieH(img):
    return img[::-1]
################## Q5 ##################
def symetrieV(img):
    img3=[[[0] for i in range(len(img[0]))]for j in range(len(img))]
    for i in range(len(img)):
        img3[i]=list(img[i][::-1])
    return np.array(img3)
################## Q6 ##################
def grayscale(imageRGB):
    e=[[floor(((j.max()+j.min())/2))for j in i]for i in np.array(imageRGB)]
    return e

