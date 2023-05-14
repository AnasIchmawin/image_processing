from tkinter import *
from partie1 import *
from partie2 import *
from partie3 import *
from partie4 import *
from tkinter import messagebox

window = Tk()
window.geometry('800x800')
window.geometry(f"+{710}+{30}")
window.title("Traitment d'image")
window.configure(bg="#414DC4")
window.resizable(False, False)



def poserimage(img,zon2,choice,window1):
    img2 = ouvrirImage(zon2.get())
    window1.destroy()
    if choice == "13":
        AfficherImg(poserH(img,img2))
    else:
        AfficherImg(poserV(img,img2))


def image():
    img = zon1.get()
    if img == "":
        messagebox.showwarning("Tu n'a pas saisir une image ... !!!")
    return img

def widthlenth(zon5,zon6,choice,window1):
    
    w = int(zon5.get())
    l = int(zon6.get())
    window1.destroy()
    if choice == "4":
        AfficherImg(image_noire(w,l))
    elif choice =="5":
        AfficherImg(image_blanche(w,l),1)
    elif choice == "15":
        AfficherImg(initImageRGB(w,l))
    else:
        AfficherImg(creerImgBlancNoir(w,l),1)

def exit(window1):
    window1.destroy()


def menu():
    

    img = ouvrirImage(image())
    choice = zon.get()
    if choice == "1":
        pic = plt.imread(image())
        AfficherImg(pic)
    elif choice == "2" or choice == "3" or choice == "4" or choice == "5" or choice == "6" or choice == "8" or choice == "9" or choice == "10" or choice == "15" or choice == "13" or choice == "14":
        window1 = Tk()
        window1.geometry('600x300')
        window1.title("Resultat")
        window1.geometry(f"+{100}+{30}")
        window1.resizable(False, False)

        if choice =="3" or choice == "8"or choice == "9" or choice == "10":
            window1.destroy()
            fen = Tk()
            fen.geometry("500x200")
            fen.title("resultat")
            fen.geometry(f"+{1000}+{600}")
            fen.resizable(False, False)
            if choice == "3":
                saveImage(img)
                lbl4 = Label(fen,text="Save done",font=('arial' , 25),fg= "#1825A6")
                lbl4.pack()
                lbl4.place(x = 125,y = 70)
            elif choice == "10":
                lbl1 = Label(fen,text="la valeur de la profondeur est: "+str(profondeur(img)),font=('arial' , 17),fg= "#1825A6")
                lbl1.pack()
                lbl1.place(x = 50,y=70)
            elif choice == "9":
                lbl1 = Label(fen,text="la valeur de la constrast est: \n"+str(constrast(img)),font=('arial' , 17),fg= "#1825A6")
                lbl1.pack()
                lbl1.place(x = 50,y=70)
            else:
                lbl1 = Label(fen,text="la valeur de la luminance est: "+str(luminance(img)),font=('arial' , 17),fg= "#1825A6")
                lbl1.pack()
                lbl1.place(x = 50,y=70)
        elif choice == "2":
                lbl = Label(window1,text=str(img))
                lbl.pack()
                btn5 = Button(window1, text='OK' , font=('arial' , 18) ,command=lambda:exit(window1))
                btn5.pack()
                btn5.place(x= 470,y=400)
        elif choice == "13" or choice == "14":
            lbl = Label(window1,text = "Donner l'autre image: ",font=('arial' , 17))
            lbl.pack()
            zon2 = Entry(window1,font=('arial' , 15),width= 50, justify=CENTER)
            zon2.pack()
            btn2 = Button(window1, text='Valider' , font=('arial' , 18) ,command=lambda:poserimage(img,zon2,choice,window1))
            btn2.pack()

        else :
            lbl2 = Label(window1,text="width",font=('arial' , 19) ,fg= "#1825A6")
            lbl2.pack()
            zon5 = Entry(window1,font=('arial' , 15), justify=CENTER)
            zon5.pack()
            lbl3 = Label(window1,text="length",font=('arial' , 19) ,fg= "#1825A6")
            lbl3.pack()
            zon6 = Entry(window1,font=('arial' , 15), justify=CENTER)
            zon6.pack()
            btn5 = Button(window1, text='Valider' , font=('arial' , 18) , command=lambda:widthlenth(zon5,zon6,choice,window1))
            btn5.pack()
         
    elif choice == "7":
        AfficherImg(negatif(img))
    elif choice == "11":
        AfficherImg(inverser(img))
    elif choice == "12":
        AfficherImg(flipH(img))
    elif choice == "16":
        AfficherImg(symetrieH(img))
    elif choice == "17":
        AfficherImg(symetrieV(img))
    elif choice == "18":
        window2 = Tk()
        window2.geometry('460x200')
        window2.resizable(False, False)

        lbl = Label(window2,text="MERCI POUR VOTRE TEMP",font=('arial' , 19) ,fg= "#1825A6")
        
        lbl.pack()
        lbl.place(x=20,y=70)
        window2.after(2500, lbl.pack_forget)
        window2.after(2500, window2.destroy)
        window.after(500,window.destroy)
        
    else :
        messagebox.showwarning("Donner un correct nombre ... !!!")

frame = Frame(window,bg="#1825A6") #bon arrangement

lbl3 = Label(frame ,text="Donner l'adresse de l'image",font=('arial' , 19) , bg="#414DC4",fg= "#ffffff")
lbl3.pack()
zon1 = Entry(frame,font=('arial' , 15),width= 50, justify=CENTER)
zon1.pack()


lbl2 = Label(frame , text='''
______________Partie 01:______________
    1. Afficher Image                              
    2. Ouvrir Image                                
    3. Save Image                                  
______________Partie 02:______________
    4. Creer Image Noire                        
    5. Creer Image Blanche                   
    6. Creer Imgage BlancNoir               
    7. Negatif de l'image                         
______________Partie 03:______________
    8. Calcule la luminance                     
    9. Calcule de constrast                     
    10. Calcule de profondeur                  
______________Partie 04:______________
    11. Inverser l'image                             
    12. Flip Horizental de l'image              
    13. Poser virtical de deux images       
    14. Poser horisentale de deux images
______________Partie 05:______________
    15. Initialiser image RGB                     
    16. Symétrique horizontal de l'image  
    17. Symétrique verticale de l'image    
    18. Quit                                               
    ''' , font=('arial' , 16) , bg="#414DC4",fg= "#ffffff")
lbl2.pack()


lbl = Label(frame , text='Entrer votre choix :' , font=('arial' , 19) , bg="#414DC4",fg="#ffffff")
lbl.pack()

zon = Entry(frame,font=('arial' , 18) , justify=CENTER)
zon.pack()

btn = Button(frame , text='Valider' , font=('arial' , 18) , command=menu , bg="#414DC4",fg = "#ffffff")
btn.pack()



frame.pack(expand=YES)

window.mainloop()