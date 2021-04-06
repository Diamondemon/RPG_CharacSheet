from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QMainWindow, QMenuBar)
from PySide6.QtGui import QAction
import pickle as pk
from functools import partial
import CharSFrame as CsF


# Fenêtre pricipale

class CharMenu(QMenuBar):
    """ Widget menu permettant d'accéder aux personnages ou la suppresion de personnage """

    def __init__(self, master):
        QMenuBar.__init__(self, master)
        self.menu_perso = self.addMenu(self.tr("Changer de perso"))
        self.action_create = QAction(self.tr("Créer"), self)
        self.menu_perso.addAction(self.action_create)
        self.connect(self.action_create, SIGNAL("triggered()"), self.goto_create)
        self.menu_perso.addSeparator()
        for i in enumerate(self.get_characlist()):
            self.menu_perso.addAction(i[1].get_name(), partial(self.goto_other, i[0]))

        self.addAction(self.tr("Supprimer"), self.goto_suppr)
        self.addAction(self.tr("Compétences"), self.goto_compet)
        self.addAction(self.tr("Sorts"), self.goto_spell)

    def get_characlist(self):
        """Method to get the list of characters from the main window"""
        return self.parent().get_characlist()

    @Slot()
    def goto_compet(self):
        print("Panneau des compétences")

    @Slot()
    def goto_create(self):
        """ Envoie dans l'environnement de création de personnage"""
        print("Panneau de création")

    @Slot()
    def goto_other(self, number):
        """ Emène vers la page caractéristique de l'autre personnage selectionné """

        print(self.get_characlist()[number].get_name())
        # self.set_selectedchar(number)

    @Slot()
    def goto_spell(self):
        print("Panneau des sorts")

    @Slot()
    def goto_suppr(self):
        """ Emmène vers la page de suppresion des personnages """
        self.parent().goto_suppr()

    def refresh(self):
        while len(self.menu_perso.actions()) > 2:
            self.menu_perso.removeAction(self.menu_perso.actions()[-1])
        for i in enumerate(self.get_characlist()):
            self.menu_perso.addAction(i[1].get_name(), partial(self.goto_other, i[0]))

    def set_selectedchar(self, character):

        self.parent().set_selectedchar(character)


class UIWindow(QMainWindow):
    """ Fenêtre de base, ne contient que le nécessaire """

    def __init__(self):
        QMainWindow.__init__(self)
        self.titre = "Solo Leveling"

        with open("characters", "rb") as fichier:
            self.characlist = pk.Unpickler(fichier).load()

        with open("competences", "rb") as fichier:
            self.competlist = pk.Unpickler(fichier).load()

        with open("spells", "rb") as fichier:
            self.spelllist = pk.Unpickler(fichier).load()

        self.menubar = CharMenu(self)
        self.setWindowTitle(self.titre)
        self.setMenuBar(self.menubar)
        self.CSFrame = CsF.CharSFrame()

    def get_characlist(self):

        return self.characlist

    def goto_suppr(self):
        self.takeCentralWidget()
        self.setCentralWidget(self.CSFrame)
        self.CSFrame.refresh()

    def pop(self, index: int):
        if index < len(self.characlist):
            self.characlist.pop(index)

            with open("characters", "wb") as fichier:
                pk.Pickler(fichier).dump(self.master.characlist)

    def set_selectedchar(self, number):

        self.CDF.set_selectedchar(self.characlist[number])
