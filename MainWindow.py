from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QMainWindow, QMenuBar)
from PySide6.QtGui import QAction
import pickle as pk
from functools import partial
import Perso_class as Pc
import CharSFrame as CsF
import CharCFrame as CcF
import HomeFrame as Hf
import CompetFrame as Cf
import SpellFrame as Sf
import CharDisplayFrame as CdF


# Fenêtre pricipale

class CharMenu(QMenuBar):
    """ Widget menu permettant d'accéder aux personnages ou la suppresion de personnage """

    def __init__(self, master):
        QMenuBar.__init__(self, master)
        self.addAction(self.tr("Accueil"), self.goto_home)
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
        self.parent().goto_compet()

    @Slot()
    def goto_create(self):
        """ Envoie dans l'environnement de création de personnage"""
        self.parent().goto_create()

    @Slot()
    def goto_home(self):
        """

        :return: None
        """
        self.parent().goto_home()

    @Slot()
    def goto_other(self, number):
        """ Emène vers la page caractéristique de l'autre personnage selectionné """

        print(self.get_characlist()[number].get_name())
        # self.set_selectedchar(number)

    @Slot()
    def goto_spell(self):
        self.parent().goto_spell()

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
        self.HFrame = Hf.HomeFrame()
        self.CSFrame = CsF.CharSFrame()
        self.CCFrame = CcF.CharCFrame()
        self.CompCFrame = Cf.CompetCreatorFrame()
        self.SpellCFrame = Sf.SpellCreatorFrame()
        self.CharDFrame = CdF.CharDisplayFrame()

        self.setCentralWidget(self.HFrame)
        self.HFrame.charlist_reload()

    def generate(self, name: str, xp: int, mage: bool):
        character = Pc.player(name, xp, mage)  # create a character with the specified name and experience
        self.characlist.append(character)
        self.save_characlist()
        self.menubar.refresh()

    def generate_competence(self, categ: str, subcateg: str, name: str, effect: str):
        new_compet = Pc.Competence(categ, subcateg, name, effect)
        self.competlist.append(new_compet)
        self.save_competlist()

    def get_characlist(self):
        """
        Getter for the characlist attribute
        :return: Reference to the list of characters
        """

        return self.characlist

    def get_competlist(self):
        """
        Getter for the competlist attribute
        :return: Reference to the list of competences
        """

        return self.competlist

    def get_spelllist(self):
        """
        Getter for the spelllist attribute
        :return: Reference to the list of spells
        """

        return self.spelllist

    def goto_compet(self):
        """
        Method called to display the CompetCreatorFrame (competence creator) as the central widget
        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.CompCFrame)
        self.CompCFrame.refresh()

    def goto_create(self):
        """
        Method called to display the CharCFrame (character creator) as the central widget
        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.CCFrame)

    def goto_home(self):
        """
        Method called to display the HomeFrame as the central widget
        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.HFrame)
        self.HFrame.charlist_reload()

    def goto_modify(self):
        """

        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.CharDFrame)
        self.CharDFrame.refresh()

    def goto_spell(self):
        """

        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.SpellCFrame)

    def goto_suppr(self):
        """

        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.CSFrame)
        self.CSFrame.refresh()

    def import_char(self, characters_list: list[Pc.player]):
        """
        Method called to add characters to the list
        :param characters_list: list of characters
        :return: None
        """
        self.characlist += characters_list
        self.save_characlist()
        self.menubar.refresh()

    def pop(self, index: int):
        if index < len(self.characlist):
            self.characlist.pop(index)
            self.save_characlist()
            self.menubar.refresh()

    def pop_compet(self, index: int):
        if index < len(self.competlist):
            self.competlist.pop(index)
            self.save_competlist()
            self.CompCFrame.refresh()

    def save_characlist(self):
        with open("characters", "wb") as fichier:
            pk.Pickler(fichier).dump(self.characlist)

    def save_competlist(self):
        with open("competences", "wb") as fichier:
            pk.Pickler(fichier).dump(self.competlist)

    def set_selectedchar(self, number: int):
        self.CharDFrame.set_selectedchar(self.characlist[number])
