import tkinter as tk

GRILLE_WIDTH, GRILLE_HEIGHT = 100, 100
CANVAS_WIDTH, CANVAS_HEIGHT = 600, 600
fourmis_list = []
direction = [0,1,0,0]
coo_fourmis = [GRILLE_HEIGHT//2,GRILLE_WIDTH//2]
idrectangle = []
nb=0
vitesse = 1

def make_grille():
    global fourmis_list
    for i in range(GRILLE_HEIGHT):
        fourmis_list.append([])
        idrectangle.append([])
        for j in range(GRILLE_WIDTH):
            fourmis_list[i].append(0)
            idrectangle[i].append("none")
            


def start():
    global fourmis_list,direction,coo_fourmis,idduafter,idrectangle,nb,vitesse

    
    
    if fourmis_list[coo_fourmis[0]][coo_fourmis[1]] == 1:
        fourmis_list[coo_fourmis[0]][coo_fourmis[1]] = 0

        canvas.delete(idrectangle[coo_fourmis[0]][coo_fourmis[1]])

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


    else:
        fourmis_list[coo_fourmis[0]][coo_fourmis[1]] = 1

        idrectangle[coo_fourmis[0]][coo_fourmis[1]] = canvas.create_rectangle(
                                                    (coo_fourmis[0]*CANVAS_HEIGHT)//GRILLE_HEIGHT,
                                                    (coo_fourmis[1]*CANVAS_WIDTH)//GRILLE_WIDTH,
                                                    ((coo_fourmis[0]*CANVAS_HEIGHT)//GRILLE_HEIGHT)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                    ((coo_fourmis[1]*CANVAS_WIDTH)//GRILLE_WIDTH)+(CANVAS_HEIGHT//GRILLE_HEIGHT),
                                                    width=0,
                                                    fill="black"
                                                    )

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


def stop():
    global idduafter

    root.after_cancel(idduafter)

def changement_vitesse(vitesses):
    global vitesse
    vitesse = vitesses

def next():
    start()
    stop()

def sauvegarde():
    pass

def charger():
    pass

def back():
    pass
               

# programme principal définition des widgets/événements

root = tk.Tk()
root.title("Mon dessin")
root.geometry("+0+0")


# gestion des événements

canvas = tk.Canvas(root, bg="white", width = CANVAS_WIDTH, height = CANVAS_HEIGHT, borderwidth=0,highlightthickness=0)

menu = tk.Menubutton(root,text="Option",relief='raised')
menu.grid(row=0, column=0) # positionnement du widget

menu_bar = tk.Menu(menu,tearoff=0)
menu["menu"] = menu_bar

menu_bar.add_cascade(label="Sauvegarder",command=sauvegarde)

menu_bar.add_cascade(label="Charger",command=charger)

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

nb_iteration = tk.Label(root,text=nb)

nb_iteration.grid(row=0, column=5)

barre_vitesse = tk.Scale(root, orient='horizontal', from_=1, to=20,
                        resolution=1, tickinterval=1, length=350,
                        label='Vitesse',command=changement_vitesse)

barre_vitesse.grid(row=0, column=6)

canvas.grid(row=1, column=0,columnspan=7)

# Fin de votre code

make_grille()

root.mainloop()
