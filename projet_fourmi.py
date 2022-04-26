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

fourmis_list = []
direction = [0,0,0,1]
coo_fourmis = [GRILLE_HEIGHT//2,GRILLE_WIDTH//2]
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
    global fourmis_list
    for i in range(GRILLE_HEIGHT):
        fourmis_list.append([])
        idrectangle.append([])
        for j in range(GRILLE_WIDTH):
            fourmis_list[i].append(0)
            idrectangle[i].append("none")
            


def start():
    """Changement de direction et de couleur de la fourmi en fonction de la grille"""
    global fourmis_list,direction,coo_fourmis,idduafter,idrectangle,nb,vitesse
    
    if fourmis_list[coo_fourmis[0]][coo_fourmis[1]] == len(forme_algo)-1:
        fourmis_list[coo_fourmis[0]][coo_fourmis[1]] = 0
        canvas.delete(idrectangle[coo_fourmis[0]][coo_fourmis[1]])
        idrectangle[coo_fourmis[0]][coo_fourmis[1]] = "none"

    else:
        fourmis_list[coo_fourmis[0]][coo_fourmis[1]] += 1
        canvas.delete(idrectangle[coo_fourmis[0]][coo_fourmis[1]])
        idrectangle[coo_fourmis[0]][coo_fourmis[1]] = canvas.create_rectangle(
                                                    (coo_fourmis[0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                    (coo_fourmis[1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                    ((coo_fourmis[0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                    ((coo_fourmis[1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                    width=0,
                                                    fill=couleur[fourmis_list[coo_fourmis[0]][coo_fourmis[1]]]
                                                    )
    
    if(forme_algo[fourmis_list[coo_fourmis[0]][coo_fourmis[1]]] == "G" or forme_algo[fourmis_list[coo_fourmis[0]][coo_fourmis[1]]] == "g"):
        direction_linéaire(True)
    else:
        direction_linéaire(False)

    if coo_fourmis[0] >= GRILLE_HEIGHT-1 and direction[1] == 1:
            coo_fourmis[0] = 0
    else:
        coo_fourmis[0] += direction[1]

    if coo_fourmis[1] >= GRILLE_WIDTH-1 and direction[2] == 1:
        coo_fourmis[1] = 0
    else:
        coo_fourmis[1] += direction[2]

    if coo_fourmis[0] <= 0 and direction[3] == 1:
        coo_fourmis[0] = GRILLE_HEIGHT-1
    else:
        coo_fourmis[0] -= direction[3]

    if coo_fourmis[1] <= 0 and direction[0] == 1:
        coo_fourmis[1] = GRILLE_WIDTH-1
    else:
        coo_fourmis[1] -= direction[0]
        
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

def direction_linéaire(direc):
    global direction
    if(direc):
        if direction[0] == 1:
            direction[3] = 1
            direction[0] = 0
        elif direction[1] == 1:
            direction[0] = 1
            direction[1] = 0
        elif direction[2] == 1:
            direction[1] = 1
            direction[2] = 0
        elif direction[3] == 1:
            direction[2] = 1
            direction[3] = 0
    else:
        if direction[0] == 1:
            direction[1] = 1
            direction[0] = 0
        elif direction[1] == 1:
            direction[2] = 1
            direction[1] = 0
        elif direction[2] == 1:
            direction[3] = 1
            direction[2] = 0
        elif direction[3] == 1:
            direction[0] = 1
            direction[3] = 0


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

    print("direction: ",direction)
    print("case: ",fourmis_list[coo_fourmis[0]][coo_fourmis[1]])

def sauvegarde():
    """Sauvegarde de la grille"""
    global fourmis_list,coo_fourmis,direction
    list_coo_fourmis = [fourmis_list,coo_fourmis,direction]

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
    global fourmis_list,coo_fourmis,direction

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

    data.close()

    affiche()

def reset():
    global direction,coo_fourmis,fourmis_list,nb
    canvas.delete("all")
    nb = 0
    direction = [0,0,0,1]
    coo_fourmis = [GRILLE_HEIGHT//2,GRILLE_WIDTH//2]
    nb_iteration.config(text=str(nb))
    for i in range(GRILLE_HEIGHT):
        for j in range(GRILLE_WIDTH):
            fourmis_list[i][j] = 0
            idrectangle[i][j] = "none"

def changement_algo():
    global nouvel_fenetre
    nouvel_fenetre = tk.Toplevel()
    texte = tk.Label(nouvel_fenetre,text="Entrez une suite de gauche droite exp \"GDDG\"") # création du widget
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

    if coo_fourmis[0] >= GRILLE_HEIGHT-1 and direction[1] == 1:
            coo_fourmis[0] = 0
    else:
        coo_fourmis[0] -= direction[1]

    if coo_fourmis[1] >= GRILLE_WIDTH-1 and direction[2] == 1:
        coo_fourmis[1] = 0
    else:
        coo_fourmis[1] -= direction[2]

    if coo_fourmis[0] <= 0 and direction[3] == 1:
        coo_fourmis[0] = GRILLE_HEIGHT-1
    else:
        coo_fourmis[0] += direction[3]

    if coo_fourmis[1] <= 0 and direction[0] == 1:
        coo_fourmis[1] = GRILLE_WIDTH-1
    else:
        coo_fourmis[1] += direction[0]

    if(forme_algo[fourmis_list[coo_fourmis[0]][coo_fourmis[1]]] == "G" or forme_algo[fourmis_list[coo_fourmis[0]][coo_fourmis[1]]] == "g"):
        direction_linéaire(False)
    else:
        direction_linéaire(True)

    if fourmis_list[coo_fourmis[0]][coo_fourmis[1]] == 0:
        canvas.delete(idrectangle[coo_fourmis[0]][coo_fourmis[1]])
        idrectangle[coo_fourmis[0]][coo_fourmis[1]] = "none"
        fourmis_list[coo_fourmis[0]][coo_fourmis[1]] = len(forme_algo)-1
        
    else:
        canvas.delete(idrectangle[coo_fourmis[0]][coo_fourmis[1]])
        idrectangle[coo_fourmis[0]][coo_fourmis[1]] = canvas.create_rectangle(
                                                    (coo_fourmis[0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                    (coo_fourmis[1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                    ((coo_fourmis[0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                    ((coo_fourmis[1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                    width=0,
                                                    fill=couleur[fourmis_list[coo_fourmis[0]][coo_fourmis[1]]]
                                                    )
        fourmis_list[coo_fourmis[0]][coo_fourmis[1]] -= 1

    print("direction: ",direction)
    print("case: ",fourmis_list[coo_fourmis[0]][coo_fourmis[1]])
        
    nb-=1

    nb_iteration.config(text=str(nb))
    
               

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

bouton_stop = tk.Button(root, text="Pause", font = ("helvetica", "10"), bg="pink",command=stop
                  ) # création du widget
bouton_stop.grid(row=0, column=1) # positionnement du widget

bouton_start = tk.Button(root, text="Play", font = ("helvetica", "10"), bg="pink",command=start
                  ) # création du widget
bouton_start.grid(row=0, column=2) # positionnement du widget

bouton_next = tk.Button(root, text="Next", font = ("helvetica", "10"), bg="pink",command=next
                  ) # création du widget
bouton_next.grid(row=0, column=3) # positionnement du widget

bouton_back = tk.Button(root, text="back", font = ("helvetica", "10"), bg="pink",command=back
                  ) # création du widget
bouton_back.grid(row=0, column=4) # positionnement du widget

bouton_reset = tk.Button(root, text="reset", font = ("helvetica", "10"), bg="pink",command=reset
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
