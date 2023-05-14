################## Les images en niveau de gris ##################
import numpy as np
from partie1 import ouvrirImage
################## Q1 ##################
def luminance(Img):
    return (Img.max()+Img.min())/2
################## Q2 ##################
def constrast(Img):
    s=0
    for i in Img:
        for j in i:
            s+=(j[0]-luminance(Img))**2
    # au lieu de transformer à deux dimension j'ai pris un j[0] puisque les trois en la meme valeur
    return (1/(len(Img)*len(Img[0])))*s
################## Q3 ##################
def profondeur(Img):
    if Img.ndim==2:
        if Img.max()==1:
            return 1
        else: return 8
    else:
        return 24
    #par unité bit
################## Q4 ##################
def ouvrir(Img):
    return ouvrirImage(Img)
################## Q5 ##################
def inverser(img):
    inv=np.array([[255-j for j in i] for i in img])
    return inv
################## Q6 ##################  
def flipH(img):
    t=[]
    for i in range(len(img)):
        t=t+[img[i][::-1]]
    return t
################## Q7 ##################     
def poserV(img1,img2):
    img3=[]
    if profondeur(img1)==profondeur(img2):
        if len(img1[0])==len(img2[0]):
            img3+=list(img1)+list(img2)
            np.array(img3)
    return img3
################## Q8 ##################
def poserH(img1, img2):
    img3=[[[0] for i in range(len(img1[0])+len(img2[0]))]for j in range(len(img1))]
    if profondeur(img1)==profondeur(img2):
        if len(img1)==len(img2):
            for i in range(len(img1)):
                img3[i]= list(img1[i])+list(img2[i])
    return np.array(img3)

