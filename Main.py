from os import path, chdir
from pickle import Pickler

chdir(path.dirname(__file__))
from UI_classes import UI_Window

if not path.exists("characters"):
    dico = []
    with open("characters", "wb") as fichier:
        Pickler(fichier).dump(dico)

if not path.exists("competences"):
    dico = []
    with open("competences", "wb") as fichier:
        Pickler(fichier).dump(dico)

if not path.exists("spells"):
    dico = []
    with open("spells", "wb") as fichier:
        Pickler(fichier).dump(dico)

window = UI_Window()

window.mainloop()
