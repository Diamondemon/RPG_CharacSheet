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


class UIWindow(QMainWindow):
    """ Fenêtre de base, ne contient que le nécessaire """

    def __init__(self):
        QMainWindow.__init__(self)
        self.titre = "Solo Leveling"
        # maxheight = self.screen().availableSize().height()
        # print(maxheight)
        # self.setMaximumHeight(maxheight)

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
        """
        Method called to create a new character for the user

        :param name: name of the character
        :param xp: experience points to give to the character
        :param mage: boolean indicating whether the character to create is a mage of not
        :return: None
        """
        character = Pc.player(name, xp, mage)  # create a character with the specified name and experience
        self.characlist.append(character)
        self.save_characlist()
        self.menubar.refresh()

    def generate_competence(self, categ: str, subcateg: str, name: str, effect: str):
        """
        Method called to create a new competence

        :param categ: category of the competence
        :param subcateg: subcategory of the competence
        :param name: name of the competence
        :param effect: description and effect of the competence
        :return: None
        """
        new_compet = Pc.Competence(categ, subcateg, name, effect)
        self.competlist.append(new_compet)
        self.save_competlist()

    def generate_spell(self, elem: str, subcateg: str, name: str, effect: str, description: str, cost: int):
        """
        Method called to create a new spell

        :param elem: element of the spell
        :param subcateg: subcategory of the spell
        :param name: name of the spell
        :param effect: effect of the spell
        :param description: lore descripton of the spell
        :param cost: points of mana needed to use the spell
        :return: None
        """
        new_spell = Pc.Spell(elem, subcateg, name, effect, description, cost)
        self.competlist.append(new_spell)
        self.save_spelllist()

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
        Method called to display the CharDisplayFrame and modify the selected character

        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.CharDFrame)
        self.CharDFrame.refresh()

    def goto_spell(self):
        """
        Method called to display the SpellCreator Frame as the central widget

        :return: None
        """
        self.takeCentralWidget()
        self.setCentralWidget(self.SpellCFrame)
        self.SpellCFrame.refresh()

    def goto_suppr(self):
        """
        Method to display the CharSFrame and delete characters

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
        """
        Method called to delete one character from the list

        :param index: index of the character to delete
        :return: None
        """
        if index < len(self.characlist):
            self.characlist.pop(index)
            self.save_characlist()
            self.menubar.refresh()

    def pop_compet(self, index: int):
        """
        Method called to delete one competence from the list

        :param index: index of the competence to delete
        :return: None
        """
        if index < len(self.competlist):
            self.competlist.pop(index)
            self.save_competlist()

    def pop_spell(self, index: int):
        """
        Method called to delete one spell from the list

        :param index: index of the spell to delete
        :return: None
        """
        if index < len(self.spelllist):
            self.spelllist.pop(index)
            self.save_spelllist()

    def save_characlist(self):
        """
        Method called to save the list of characters

        :return: None
        """
        with open("characters", "wb") as fichier:
            pk.Pickler(fichier).dump(self.characlist)

    def save_competlist(self):
        """
        Method called to save the list of competences

        :return: None
        """
        with open("competences", "wb") as fichier:
            pk.Pickler(fichier).dump(self.competlist)

    def save_spelllist(self):
        """
        Method called to save the list of spells

        :return: None
        """
        with open("competences", "wb") as fichier:
            pk.Pickler(fichier).dump(self.spelllist)

    def set_selectedchar(self, number: int):
        """
        Method called to select the character to load and edit

        :param number: index of the character to select
        :return: None
        """
        if self.CharDFrame:
            self.CharDFrame.set_selectedchar(self.characlist[number])


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
        """
        Method to get the list of characters from the main window

        :return: list of characters contained in the parent
        """
        return self.parent().get_characlist()

    @Slot()
    def goto_compet(self):
        """
        Slot called to load the widget used to manage competences

        :return: None
        """
        self.parent().goto_compet()

    @Slot()
    def goto_create(self):
        """
        Slot called to load the widget used to create a character

        :return: None
        """
        self.parent().goto_create()

    @Slot()
    def goto_home(self):
        """
        Slot called to load the HomeFrame

        :return: None
        """
        self.parent().goto_home()

    @Slot()
    def goto_other(self, number: int):
        """
        Slot called to load the selected character

        :param number: index of the character to load
        :return: None
        """
        self.set_selectedchar(number)
        self.parent().goto_modify()

    @Slot()
    def goto_spell(self):
        """
        Slot called to load the widget used to managed spells

        :return: None
        """
        self.parent().goto_spell()

    @Slot()
    def goto_suppr(self):
        """
        Slot called to load the widget used to delete characters

        :return: None
        """
        self.parent().goto_suppr()

    def parent(self) -> UIWindow:
        """
        Method that returns the parent of the widget (the main window)

        :return: parent widget
        """
        return QMenuBar.parent(self)

    def refresh(self):
        """
        Method called to refresh the names of the characters in the menu

        :return: None
        """
        while len(self.menu_perso.actions()) > 2:
            self.menu_perso.removeAction(self.menu_perso.actions()[-1])
        for i in enumerate(self.get_characlist()):
            self.menu_perso.addAction(i[1].get_name(), partial(self.goto_other, i[0]))

    def set_selectedchar(self, character):
        """
        Method called to set the character to load

        :param character: index of the character to load
        :return: None
        """
        self.parent().set_selectedchar(character)
