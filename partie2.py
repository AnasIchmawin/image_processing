##################  Les images Noir et blanc ##################
import numpy as np
from partie1 import AfficherImg
################## Q1 ##################
def image_noire(h, l):
    img=np.zeros((h,l))
    return img
################## Q2 ##################
def image_blanche(h, l):
    img=np.ones((h,l))
    return img
################## Q3 ##################
def creerImgBlancNoir(h,l):
    img=np.array([[(i+j)%2 for i in range(l)]for j in range(h)])
    return img
################## Q4 ##################
def negatif(Img):
    img=np.array([[1-j for j in i] for i in Img])
    return img

