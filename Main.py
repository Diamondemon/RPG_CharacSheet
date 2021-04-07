from os import path, chdir
from pickle import Pickler
from PySide6.QtWidgets import QApplication
import sys

chdir(path.dirname(__file__))
from MainWindow import UIWindow as UI_W

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_W()
    window.show()
    sys.exit(app.exec_())

    """window = UI_Window()

    window.mainloop()"""