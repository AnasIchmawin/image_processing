
from matplotlib import pyplot as plt
################## affichage ##################
def AfficherImg(img,m=255,n=0):
    plt.axis("off")
    plt.imshow(img,cmap = 'gray',interpolation="nearest",vmax=m,vmin=n) 
    # J'ai chosi m,n comme valeur pour assurer l'accer au choix des valeurs vmax 
    # pour assurer l'accer au choix des valeurs vmax et vmin ce qui donne le fait de choisir entre noire blanc et rgb
    plt.show()
################## open ##################
def ouvrirImage(chemin):
    img=plt.imread(chemin)
    return img
################## saveimage ##################
def saveImage(img):
    plt.imsave("image1.png",img)