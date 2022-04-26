#########################################
# groupe MI TD3
# Basile Lauriola
# Camilia Boukebouche
# Julien Hrelja
# https://github.com/uvsq22107694/Projet2
# https://github.com/uvsq-info/l1-python
#########################################

# import des librairies

import tkinter as tk
from tkinter import filedialog as fd
import pickle
import os

# définition des constantes

GRILLE_WIDTH, GRILLE_HEIGHT = 100, 100
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600

# définition des variables globales

nombre_fourmis = 1
coo_fourmis = []
coo_fourmis.append([])
coo_fourmis[0] = [GRILLE_HEIGHT//2,GRILLE_WIDTH//2]
fourmis_list = []
direction = []
direction.append([])
direction[0] = [0,0,0,1]
idrectangle = []
nb = 0 # Nonbre itérations
vitesse = 1 # vitesse du after
couleur = ["#FFFFFF","#000000", "#FF0000", "#00FF00", 
           "#0000FF", "#FFFF00", "#FF00FF", 
           "#00FFFF", "#646464", "#3C8F3A",
           "#F0F0F0", "#64285A", "#EE5AAA",
           "#D50053"]

forme_algo = "GD"           

# définition des fonctions

def make_grille():
    """Créer une grille"""
    global fourmis_list,idrectangle
    for i in range(GRILLE_HEIGHT):
        fourmis_list.append([])
        idrectangle.append([])
        for j in range(GRILLE_WIDTH):
            fourmis_list[i].append(0)
            idrectangle[i].append("none")
            


def start():
    """Changement de direction et de couleur de la fourmi en fonction de la grille"""
    global fourmis_list,direction,coo_fourmis,idduafter,idrectangle,nb,vitesse

    for i in range(nombre_fourmis):
        if fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] == len(forme_algo)-1:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] = 0
            canvas.delete(idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = "none"

        else:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] += 1
            canvas.delete(idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = canvas.create_rectangle(
                                                        (coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                        (coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                        ((coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        ((coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        width=0,
                                                        fill=couleur[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]]
                                                        )
        
        if(forme_algo[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]] == "G" or forme_algo[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]] == "g"):
            direction_linéaire(True,i)
        else:
            direction_linéaire(False,i)

        if coo_fourmis[i][0] >= GRILLE_HEIGHT-1 and direction[i][1] == 1:
                coo_fourmis[i][0] = 0
        else:
            coo_fourmis[i][0] += direction[i][1]

        if coo_fourmis[i][1] >= GRILLE_WIDTH-1 and direction[i][2] == 1:
            coo_fourmis[i][1] = 0
        else:
            coo_fourmis[i][1] += direction[i][2]

        if coo_fourmis[i][0] <= 0 and direction[i][3] == 1:
            coo_fourmis[i][0] = GRILLE_HEIGHT-1
        else:
            coo_fourmis[i][0] -= direction[i][3]

        if coo_fourmis[i][1] <= 0 and direction[i][0] == 1:
            coo_fourmis[i][1] = GRILLE_WIDTH-1
        else:
            coo_fourmis[i][1] -= direction[i][0]
        
    nb+=1

    nb_iteration.config(text=str(nb))
    
    idduafter = root.after(vitesse,start)

def affiche():
    """ Afficher la grille"""
    global fourmis_list,idrectangle
    canvas.delete("all")
    for i in range(GRILLE_HEIGHT):
        for j in range(GRILLE_WIDTH):
            if(fourmis_list[i][j] == 1):
                idrectangle[i][j] = canvas.create_rectangle(
                                                            (i*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                            (j*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                            ((i*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                            ((j*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                            width=0,
                                                            fill="black"
                                                            )
            else:
                idrectangle[i][j] = "none"

def direction_linéaire(direc,fourmis):
    global direction
    
    if(direc):
        if direction[fourmis][0] == 1:
            direction[fourmis][3] = 1
            direction[fourmis][0] = 0
        elif direction[fourmis][1] == 1:
            direction[fourmis][0] = 1
            direction[fourmis][1] = 0
        elif direction[fourmis][2] == 1:
            direction[fourmis][1] = 1
            direction[fourmis][2] = 0
        elif direction[fourmis][3] == 1:
            direction[fourmis][2] = 1
            direction[fourmis][3] = 0
    else:
        if direction[fourmis][0] == 1:
            direction[fourmis][1] = 1
            direction[fourmis][0] = 0
        elif direction[fourmis][1] == 1:
            direction[fourmis][2] = 1
            direction[fourmis][1] = 0
        elif direction[fourmis][2] == 1:
            direction[fourmis][3] = 1
            direction[fourmis][2] = 0
        elif direction[fourmis][3] == 1:
            direction[fourmis][0] = 1
            direction[fourmis][3] = 0


def stop():
    """Mettre pause ou reprendre le programme"""
    global idduafter

    root.after_cancel(idduafter)

def changement_vitesse(parametre):
    """Changement de vitesse du calcul"""
    global vitesse
    vitesse = parametre

def next():
    """Avance d'une itération"""
    global fourmis_list,direction,coo_fourmis,idduafter,idrectangle,nb,vitesse

    start()
    stop()

def sauvegarde():
    """Sauvegarde de la grille"""
    global fourmis_list,coo_fourmis,direction,nb
    list_coo_fourmis = [fourmis_list,coo_fourmis,direction,nb]

    filetypes = [('All Files', '*.*'), 
             ('Python Files', '*.py'),
             ('Text Document', '*.txt')]

    file = fd.asksaveasfile(
            mode="wb",
            filetypes = filetypes,
            defaultextension = filetypes
            )

    pickle.dump(list_coo_fourmis, file)

    file.close()

def charger():
    """Charger la grille"""
    global fourmis_list,coo_fourmis,direction,nb

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
                initialdir=os.getcwd()+"/Grilles",
                filetypes=filetypes
                )

    with open(filename, "rb") as data:

        list_coo_fourmis = pickle.load(data)
    
    fourmis_list = list_coo_fourmis[0]
    coo_fourmis = list_coo_fourmis[1]
    direction = list_coo_fourmis[2]
    nb = list_coo_fourmis[3]
    nb_iteration.config(text=str(nb))

    data.close()

    affiche()

def reset():
    global direction,coo_fourmis,fourmis_list,nb,nombre_fourmis
    canvas.delete("all")
    nb = 0
    for i in range(1,nombre_fourmis):
        del coo_fourmis[i]
        del direction[i]
    coo_fourmis[0] = [GRILLE_HEIGHT//2,GRILLE_WIDTH//2]
    direction[0] = [0,0,0,1]
    nb_iteration.config(text=str(nb))
    for i in range(GRILLE_HEIGHT):
        for j in range(GRILLE_WIDTH):
            fourmis_list[i][j] = 0
            idrectangle[i][j] = "none"
    nombre_fourmis = 1

def changement_algo():
    global nouvel_fenetre
    nouvel_fenetre = tk.Toplevel()
    texte = tk.Label(nouvel_fenetre,text="Entrez une suite de gauche droite exp \"GDDG\" de base celui ci est \"GD\"") # création du widget
    texte.grid(row=0, column=0) # positionnement du widget
    entrer = tk.Entry(nouvel_fenetre,width=50)
    entrer.grid(row=0,column=1,sticky='ew')
    boutton_entrer = tk.Button(nouvel_fenetre,text="Valider",command=lambda: valid_algo(entrer.get()))
    boutton_entrer.grid(row=1)

def valid_algo(text):
    global nouvel_fenetre,forme_algo
    forme_algo = text
    nouvel_fenetre.destroy()

def back():
    """Revenir en arrière d'une itération"""
    global fourmis_list,direction,coo_fourmis,idduafter,idrectangle,nb,vitesse


    for i in range(nombre_fourmis):

        if coo_fourmis[i][0] >= GRILLE_HEIGHT-1 and direction[i][1] == 1:
                coo_fourmis[i][0] = 0
        else:
            coo_fourmis[i][0] -= direction[i][1]

        if coo_fourmis[i][1] >= GRILLE_WIDTH-1 and direction[i][2] == 1:
            coo_fourmis[i][1] = 0
        else:
            coo_fourmis[i][1] -= direction[i][2]

        if coo_fourmis[i][0] <= 0 and direction[i][3] == 1:
            coo_fourmis[i][0] = GRILLE_HEIGHT-1
        else:
            coo_fourmis[i][0] += direction[i][3]

        if coo_fourmis[i][1] <= 0 and direction[i][0] == 1:
            coo_fourmis[i][1] = GRILLE_WIDTH-1
        else:
            coo_fourmis[i][1] += direction[i][0]

        if(forme_algo[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]] == "G" or forme_algo[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]] == "g"):
            direction_linéaire(False)
        else:
            direction_linéaire(True)


        if fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] == 0:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] = len(forme_algo)-1
            canvas.delete(idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = canvas.create_rectangle(
                                                        (coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                        (coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                        ((coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        ((coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        width=0,
                                                        fill=couleur[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]]
                                                        )     
            
        elif fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] == 1:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] -= 1
            canvas.delete(idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = "none"

        else:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] -= 1
            canvas.delete(idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            idrectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = canvas.create_rectangle(
                                                        (coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                        (coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                        ((coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        ((coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        width=0,
                                                        fill=couleur[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]]
                                                        )  
    nb-=1

    nb_iteration.config(text=str(nb))

def placer_fourmis():
    global nouvel_fenetre2
    nouvel_fenetre2 = tk.Toplevel()
    texte = tk.Label(nouvel_fenetre2,text="Entrez les coordonnées de la nouvelle fourmis Exemple: 50 50") # création du widget
    texte.grid(row=0, column=0) # positionnement du widget
    entrer = tk.Entry(nouvel_fenetre2,width=50)
    entrer.grid(row=0,column=1,sticky='ew')
    boutton_entrer = tk.Button(nouvel_fenetre2,text="Valider",command=lambda: valid_fourmis(entrer.get()))
    boutton_entrer.grid(row=1)
    
def valid_fourmis(text):
    global nouvel_fenetre2,nombre_fourmis,coo_fourmis,direction
    coordonee = list(text.split(" "))
    coo_fourmis.append([])
    coo_fourmis[nombre_fourmis] = [int(coordonee[0]),int(coordonee[1])]
    direction.append([])
    direction[nombre_fourmis] = [0,0,0,1]
    nombre_fourmis += 1
    nouvel_fenetre2.destroy()
               

# programme principal définition des widgets/événements

root = tk.Tk()
root.title("Fourmis de Longton")
root.geometry("+0+0")


# gestion des événements

canvas = tk.Canvas(root, bg="white", width = CANVAS_WIDTH, height = CANVAS_HEIGHT, borderwidth=0,highlightthickness=0) # création du canvas

menu = tk.Menubutton(root,text="Option",relief='raised') # création du widget menu boutton
menu.grid(row=0, column=0) # positionnement du widget

menu_bar = tk.Menu(menu,tearoff=0) # création du widget menu associé au menu boutton
menu["menu"] = menu_bar

menu_bar.add_cascade(label="Sauvegarder",command=sauvegarde) # création du widget cascade associé au menu

menu_bar.add_cascade(label="Charger",command=charger) # création du widget cascade associé au menu

menu_bar.add_cascade(label="Changer Algo",command=changement_algo) # création du widget cascade associé au menu

menu_bar.add_cascade(label="Placer Fourmis",command=placer_fourmis) # création du widget cascade associé au menu

bouton_stop = tk.Button(root, text="Pause", font = ("helvetica", "10"), bg="pink",command=stop
                  ) # création du widget
bouton_stop.grid(row=0, column=1) # positionnement du widget

bouton_start = tk.Button(root, text="Play", font = ("helvetica", "10"), bg="pink",command=start
                  ) # création du widget
bouton_start.grid(row=0, column=2) # positionnement du widget

bouton_next = tk.Button(root, text="Next", font = ("helvetica", "10"), bg="pink",command=next
                  ) # création du widget
bouton_next.grid(row=0, column=3) # positionnement du widget

bouton_back = tk.Button(root, text="Back", font = ("helvetica", "10"), bg="pink",command=back
                  ) # création du widget
bouton_back.grid(row=0, column=4) # positionnement du widget

bouton_reset = tk.Button(root, text="Reset", font = ("helvetica", "10"), bg="pink",command=reset
                  ) # création du widget
bouton_reset.grid(row=0, column=5) # positionnement du widget

nb_iteration = tk.Label(root,text=nb) # création du widget

nb_iteration.grid(row=0, column=6) # positionnement du widget

barre_vitesse = tk.Scale(root, orient='horizontal', from_=1, to=20,
                        resolution=1, tickinterval=1, length=350,
                        label='Vitesse',command=changement_vitesse) # création du widget

barre_vitesse.grid(row=0, column=7) # positionnement du widget

canvas.grid(row=1, column=0,columnspan=8) # positionnement du canvas

# Fin de votre code

make_grille()

root.mainloop()
