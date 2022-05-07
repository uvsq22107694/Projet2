#########################################
# groupe MI TD3
# Basile Lauriola
# Camilia Boukebouche
# Julien Hrelja
# https://github.com/uvsq22107694/Projet2
# https://github.com/uvsq-info/l1-python
#########################################

# import des librairies
#########################################

import tkinter as tk 
from tkinter import filedialog as fd
import pickle # Utilisé pour la sauvegarde et le chargement des fichiers
import os # Utilisé pour rendre universel le chargement les dossiers sur toutes les machines

# définition des constantes
#########################################

GRILLE_WIDTH, GRILLE_HEIGHT = 100, 100
# Taille de la grille ou se déplace la fourmis
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
# Taille du canvas en pixel

# définition des variables globales
#########################################

nombre_fourmis = 1

# Nombre de fourmis

coo_fourmis = []
coo_fourmis.append([])

# Liste a deux dimentions avec les coordonnées des differentes fourmis

coo_fourmis[0] = [GRILLE_HEIGHT//2,GRILLE_WIDTH//2]

# Par exemple ici la fourmis 0 est initialisé au millieu de la grille

fourmis_list = []

# Liste des fourmis dans la grille qui sera initialisé dans contruire_grille de base avec que des 0

direction = []
direction.append([])

# Liste a deux dimentions avec les directions des differentes fourmis

direction[0] = [0,0,0,1]

# Par exemple ici la fourmis 0 est initialisé avec la direction gauche
# [1,0,0,0] = haut
# [0,1,0,0] = droite
# [0,0,1,0] = bas
# [0,0,0,1] = gauche

id_rectangle = []

# Liste des id des rectangles qui sera initialisé dans contruire_grille de base avec que des "none"

nombre_iteration = 0 # Nombre itérations

vitesse = 1 # vitesse du after initialisé à 1

couleur = ["#FFFFFF","#000000", "#FF0000", "#00FF00", 
           "#0000FF", "#FFFF00", "#FF00FF", 
           "#00FFFF", "#646464", "#3C8F3A",
           "#F0F0F0", "#64285A", "#EE5AAA",
           "#D50053"]

# les differentes couleurs que peut prendre la fourmis 0 étant blanc 1 étant noir etc...

forme_algo = "GD"    

# forme de l'algorithme qui peut etre changer, initialisé à GD qui est l'agorithme de base

# définition des fonctions
#########################################

def contruire_grille():
    """Créer une grille"""
    global fourmis_list,id_rectangle
    for i in range(GRILLE_HEIGHT):
        fourmis_list.append([])
        id_rectangle.append([])
        for j in range(GRILLE_WIDTH):
            fourmis_list[i].append(0)
            id_rectangle[i].append("none")
            


def start():
    """Changement de direction et de couleur de la fourmi en fonction de la grille"""
    global fourmis_list,direction,coo_fourmis,id_after,id_rectangle,nombre_iteration,vitesse

    for i in range(nombre_fourmis):
        if fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] == len(forme_algo)-1: # si la fourmis change la case en blanc il suprime simplement le canvas et change donc l'id en "none"
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] = 0
            canvas.delete(id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = "none"

        else:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] += 1 # On passe à la couleur suivante
            canvas.delete(id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = canvas.create_rectangle(
                                                        (coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                        (coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                        ((coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        ((coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        width=0,
                                                        fill=couleur[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]] # On rempli le canvas de la couleur correspondante
                                                        )
        
        if(forme_algo[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]] == "G" or forme_algo[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]] == "g"):
            direction_linéaire(True,i) # True = gauche
        else:
            direction_linéaire(False,i) # False = droite

        # Les if suivants correspondes aux bord de la grille ils transformes les coordonnées pour les faire aller de l'autre coté du canvas
        # Les else font juste avancer la fourmis si la direction est a 1

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
        
    nombre_iteration+=1

    nombre_iteration_iteration.config(text=str(nombre_iteration)) # On refresh les itérations
    
    id_after = root.after(vitesse,start)

def affiche():
    """Afficher la grille"""
    global fourmis_list,id_rectangle
    canvas.delete("all")
    for i in range(GRILLE_HEIGHT):
        for j in range(GRILLE_WIDTH):
            if(fourmis_list[i][j] == 0):

                id_rectangle[i][j] = "none"
                
            else:

                id_rectangle[i][j] = canvas.create_rectangle(
                                                            (i*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                            (j*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                            ((i*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                            ((j*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                            width=0,
                                                            fill=couleur[fourmis_list[i][j]]
                                                            )
                

def direction_linéaire(direc,fourmis):
    """Changement de la direction de la fourmi"""
    """
    G = True
    D = False
    """
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
    global id_after

    root.after_cancel(id_after)

def changement_vitesse(parametre):
    """Changement de vitesse du calcul"""
    global vitesse
    vitesse = parametre

def next():
    """Avance d'une itération"""
    global fourmis_list,direction,coo_fourmis,id_after,id_rectangle,nombre_iteration,vitesse

    start()
    stop()

def sauvegarde():
    """Sauvegarde de la grille"""
    global fourmis_list,coo_fourmis,direction,nombre_iteration,forme_algo
    list_coo_fourmis = [fourmis_list,coo_fourmis,direction,nombre_iteration,forme_algo]

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
    global fourmis_list,coo_fourmis,direction,nombre_iteration,forme_algo

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
    nombre_iteration = list_coo_fourmis[3]
    forme_algo = list_coo_fourmis[4]
    nombre_iteration_iteration.config(text=str(nombre_iteration))

    data.close()

    affiche()

def reset():
    """Réinitialiser la grille"""
    global direction,coo_fourmis,fourmis_list,nombre_iteration,nombre_fourmis
    canvas.delete("all")
    nombre_iteration = 0
    for i in range(1,nombre_fourmis-1):
        del coo_fourmis[i]
        del direction[i]
    coo_fourmis[0] = [GRILLE_HEIGHT//2,GRILLE_WIDTH//2]
    direction[0] = [0,0,0,1]
    nombre_iteration_iteration.config(text=str(nombre_iteration))
    for i in range(GRILLE_HEIGHT):
        for j in range(GRILLE_WIDTH):
            fourmis_list[i][j] = 0
            id_rectangle[i][j] = "none"
    nombre_fourmis = 1

def changement_algo():
    """Changement de l'algorithme"""
    global nouvel_fenetre
    nouvel_fenetre = tk.Toplevel()
    texte = tk.Label(nouvel_fenetre,text="Entrez une suite de gauche droite exemple \"GDDG\" de base celui ci est \"GD\"") # création du widget
    texte.grid(row=0, column=0) # positionnement du widget
    entrer = tk.Entry(nouvel_fenetre,width=50)
    entrer.grid(row=0,column=1,sticky='ew')
    boutton_entrer = tk.Button(nouvel_fenetre,text="Valider",command=lambda: valid_algo(entrer.get()))
    boutton_entrer.grid(row=1)

def valid_algo(text):
    """Valide l'algorithme"""
    global nouvel_fenetre,forme_algo
    forme_algo = text
    nouvel_fenetre.destroy()

def back():
    """Revenir en arrière d'une itération"""
    global fourmis_list,direction,coo_fourmis,id_after,id_rectangle,nombre_iteration,vitesse


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
            direction_linéaire(False,i)
        else:
            direction_linéaire(True,i)


        if fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] == 0:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] = len(forme_algo)-1
            canvas.delete(id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = canvas.create_rectangle(
                                                        (coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                        (coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                        ((coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        ((coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        width=0,
                                                        fill=couleur[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]]
                                                        )     
            
        elif fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] == 1:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] -= 1
            canvas.delete(id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = "none"

        else:
            fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]] -= 1
            canvas.delete(id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]])
            id_rectangle[coo_fourmis[i][0]][coo_fourmis[i][1]] = canvas.create_rectangle(
                                                        (coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                        (coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                        ((coo_fourmis[i][0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        ((coo_fourmis[i][1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                        width=0,
                                                        fill=couleur[fourmis_list[coo_fourmis[i][0]][coo_fourmis[i][1]]]
                                                        )  
    nombre_iteration-=1

    nombre_iteration_iteration.config(text=str(nombre_iteration))

def placer_fourmis():
    """Placement des fourmis"""
    global nouvel_fenetre2
    nouvel_fenetre2 = tk.Toplevel()
    texte = tk.Label(nouvel_fenetre2,text="Entrez les coordonnées de la nouvelle fourmis exemple: 50 50") # création du widget
    texte.grid(row=0, column=0) # positionnement du widget
    entrer = tk.Entry(nouvel_fenetre2,width=50)
    entrer.grid(row=0,column=1,sticky='ew')
    boutton_entrer = tk.Button(nouvel_fenetre2,text="Valider",command=lambda: valid_fourmis(entrer.get()))
    boutton_entrer.grid(row=1)
    
def valid_fourmis(text):
    """Valide la position des fourmis"""
    global nouvel_fenetre2,nombre_fourmis,coo_fourmis,direction
    coordonee = list(text.split(" "))
    coo_fourmis.append([])
    coo_fourmis[nombre_fourmis] = [int(coordonee[0]),int(coordonee[1])]
    direction.append([])
    direction[nombre_fourmis] = [0,0,0,1]
    nombre_fourmis += 1
    nouvel_fenetre2.destroy()
               

# programme principal définition des widgets/événements
#########################################

root = tk.Tk()
root.title("Fourmis de Langton")
root.geometry("+0+0")


# gestion des événements
#########################################

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

nombre_iteration_iteration = tk.Label(root,text=nombre_iteration) # création du widget

nombre_iteration_iteration.grid(row=0, column=6) # positionnement du widget

barre_vitesse = tk.Scale(root, orient='horizontal', from_=1, to=20,
                        resolution=1, tickinterval=1, length=350,
                        label='Vitesse',command=changement_vitesse) # création du widget

barre_vitesse.grid(row=0, column=7) # positionnement du widget

canvas.grid(row=1, column=0,columnspan=8) # positionnement du canvas

# Fin de votre code
#########################################

contruire_grille()

root.mainloop()
