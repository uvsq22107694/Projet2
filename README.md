
# Projet Fourmis de Langton

La Fourmi de Langton est un automate cellulaire composé d’une grille à
deux dimensions et d’une fourmi. Dans ce projet, il faudra implémenter une
interface graphique à l’aide de la bibliothèque Tkinter permettant d’afficher le
comportement de cet automate.

![Animation fourmis](https://user-images.githubusercontent.com/91540224/167257503-e6f7d059-4ecf-4c82-86d8-f2555524c07f.gif)


## Informations

Math Informatique TD 3

[Lien du projet](https://github.com/uvsq22107694/Projet2)
## Contributeurs

* [Basile Lauriola](https://github.com/uvsq22107694)
* [Camilia Boukebouche](https://github.com/uvsq22106169)
* [Julien Hrelja](https://github.com/uvsq22106999)
## Fonctionnalités

- Bouton :
    - Play (dérouler des étapes tant que celui-ci est actif)
    - Pause (mettre en pause le déroulement des étapes)
    - Next (permettant de passer 1 étape à la fois)
    - Reset (Réinitialiser le déroulement)
    - Back (Revenir en arrière d'une étape)
- Modification de la vitesse (1 étant le plus rapide)
- Option (boutton cascade) :
    - Sauvegarder une instance en cours
    - Charger une instance dejà sauvegarder
    - Changement de l'algorithme (de base Gauche,Droite)
    - Pouvoir placer plusieurs fourmis (via leur coordonées)

## Utilisation détaillée

### Boutons :

![bouttons](https://user-images.githubusercontent.com/91540224/167256682-5539d983-a673-43b6-8b3d-24c84f57b305.png)

### Modification de la vitesse

Pour changer la vitesse il suffit de faire glisser le bouton de gauche à droite.

![vitesse](https://user-images.githubusercontent.com/91540224/167256797-d4ee7fe7-3bcf-4fa6-87f4-f8020382ea60.png)

### Options :

Il suffit de cliquer sur le bouton option pour avoir une liste déroulante des paramètres

![options](https://user-images.githubusercontent.com/91540224/167256866-0c2187c5-4071-4904-b2c4-6093b50a20b2.png)

#### Sauvegarde :

Vous devez choisir le nom du fichier à sauvegarder (en .txt)

![sauvegarde](https://user-images.githubusercontent.com/91540224/167256978-22b44107-3cda-4bfb-bd0f-40088d4ad155.png)

#### Charger :

Vous devez choisir le fichier à charger pour l'afficher

![charger](https://user-images.githubusercontent.com/91540224/167257047-d3a3d166-1136-4433-835a-2f86941f6d8b.png)

#### Changement algorithme :

Vous devez entrez un algorithme avec une suite de "gauche" et de "droite" ("GDDG" par exemple)

![changer algo](https://user-images.githubusercontent.com/91540224/167257162-d395679f-f58f-4d6b-8b59-dd99ebeac982.png)

#### Placer fourmis :

Vous devez entrez des coordonnées d'un nouvelle fourmis sous la forme "\{coordonnée1} \{coordonnée2}" exemple "20 20"

![placer fourmis](https://user-images.githubusercontent.com/91540224/167257256-73f5b457-3503-4cf4-9490-5bbab7884edf.png)