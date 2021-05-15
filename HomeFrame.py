from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QWidget, QListWidget, QGridLayout, QPushButton, QFileDialog)
from os import path
import pickle as pk

import MW
import Perso_class as Pc


class HomeFrame(QWidget):
    """ Widget to select and manage characters """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.Char_create = QPushButton(self.tr("Créer un personnage"))  # bouton de création de personnage
        self.Char_import = QPushButton(self.tr("Importer un personnage"))  # bouton d'import de personnage
        self.Char_modif = QPushButton(self.tr("Consulter le personnage"))  # bouton de modification de personnage
        self.Char_export = QPushButton(self.tr("Exporter le personnage"))  # bouton d'exportation de personnage
        self.Char_list = QListWidget()  # liste de choix du personnage à consulter

        self.grid.addWidget(self.Char_create, 0, 1)
        self.grid.addWidget(self.Char_import, 1, 1)
        self.grid.addWidget(self.Char_modif, 2, 1)
        self.grid.addWidget(self.Char_export, 3, 1)
        self.grid.addWidget(self.Char_list, 0, 0, 4, 1)

        self.connect(self.Char_create, SIGNAL("clicked()"), self.create_char)
        self.connect(self.Char_import, SIGNAL("clicked()"), self.import_char)
        self.connect(self.Char_modif, SIGNAL("clicked()"), self.modify_char)
        self.connect(self.Char_export, SIGNAL("clicked()"), self.export_char)
        self.connect(self.Char_list, SIGNAL("itemDoubleClicked(QListWidgetItem *)"), self.modify_char)

    def charlist_reload(self):
        """
        Method called to refresh the ListWidget

        :return: None
        """
        self.Char_list.clear()
        for i in self.get_characlist():
            self.Char_list.addItem(i.get_name())

    @Slot()
    def create_char(self):
        """
        Slot called to open the pannel for creating characters

        :return: None
        """
        self.parent().goto_create()

    @Slot()
    def export_char(self):
        """
        Slot called to export characters created to share them with other users

        :return: None
        """
        if self.Char_list.currentRow() != -1:
            perso = self.get_characlist()[self.Char_list.currentRow()]
            filename = QFileDialog.getSaveFileName(self, self.tr("Choisissez le fichier de personnage"),
                                                   path.dirname(__file__) + "/Personnages/" + perso.get_name(),
                                                   self.tr("Tous fichiers (*)"))

            if filename[0]:
                with open(filename[0], "wb") as fichier:
                    # on enregistre le personnage
                    pk.Pickler(fichier).dump(perso)

    def get_characlist(self):
        """
        Method to get the list of characters from the main window*

        :return: list of Pc.player
        """
        return self.parent().get_characlist()

    @Slot()
    def import_char(self):
        """
        Slot called to import characters created by other users

        :return: None
        """

        # on demande le fichier de personnage à importer
        filenames = QFileDialog.getOpenFileNames(self, self.tr("Choisissez le fichier de personnage"),
                                                 path.dirname(__file__), self.tr("Tous fichiers (*)"))
        if filenames[0]:
            perso_list = []
            for filename in filenames[0]:
                with open(filename, "rb") as fichier:
                    # if file contains a character, it is added to the list in order to be imported
                    perso = pk.Unpickler(fichier).load()
                    if type(perso) == Pc.player:
                        perso_list.append(perso)
            self.parent().import_char(perso_list)
            self.charlist_reload()

    @Slot()
    def modify_char(self):
        """
        Slot called to display the full characteristics of the selected character

        :return: None
        """
        if self.Char_list.currentRow() != -1:
            self.set_selectedchar(self.Char_list.currentRow())  # indexes in list and ListWidget are equal
            self.parent().goto_modify()

    def parent(self) -> MW.UIWindow:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def set_selectedchar(self, number: int):
        """
        Method called to set the selected character for display, amongthe list

        :param number: index of the character to load
        :return: None
        """
        self.parent().set_selectedchar(number)
