from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QWidget, QListWidget, QGridLayout, QPushButton, QFileDialog)
from os import path
import pickle as pk
import Perso_class as Pc


class HomeFrame(QWidget):
    """ Widget to create a new character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.Char_create = QPushButton(self.tr("Créer un personnage"))  # bouton de création de personnage
        self.Char_import = QPushButton(self.tr("Importer un personnage"))  # bouton d'import de personnage
        self.Char_modif = QPushButton(self.tr("Consulter le personnage"))  # bouton de consultation/modification de personnage
        self.Char_export = QPushButton(self.tr("Exporter le personnage"))  # bouton de consultation/modification de personnage
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
        self.connect(self.Char_list, SIGNAL("itemDoubleClicked()"), self.modify_char) # QListWidgetItem *

    @Slot()
    def create_char(self):
        """ Ouvre le panneau de création de personnage"""
        self.parent().goto_create()

    @Slot()
    def modify_char(self, event=None):
        """ Si un personnage a été sélectionné dans la liste, le définit comme personnage sélectionné
        et ouvre le panneau de consultation de personnage, en fermant le panneau d'accueil """
        if self.Char_list.curselection() != ():
            self.set_selectedchar(self.Char_list.curselection()[0])  # le numéro du personnage dans la liste correspond au numéro du personnage sur l'affichage
            for i in self.master.grid_slaves():
                i.grid_forget()
            self.parent().goto_modify()

    @Slot()
    def import_char(self):
        """ permet d'importer des personnages dans la liste """

        # on demande le fichier de personnage à importer
        filenames = QFileDialog.getOpenFileNames(self, self.tr("Choisissez le fichier de personnage"),
                                                 path.dirname(__file__), self.tr("Tous fichiers (*)"))

        if filenames:
            for filename in filenames[0]:
                with open(filename, "rb") as fichier:
                    # si le fichier importé est bien celui d'un personnage, on le stocke dans la liste des personnages
                    perso = pk.Unpickler(fichier).load()
                    if type(perso) == Pc.player:
                        self.parent().characlist.append(perso)
            self.charlist_reload()
            self.parent().menubar.refresh()

    @Slot()
    def export_char(self):
        if self.Char_list.currentRow() != -1:
            perso = self.get_characlist()[self.Char_list.currentRow()]
            filename = QFileDialog.getSaveFileName(self, self.tr("Choisissez le fichier de personnage"),
                                                   path.dirname(__file__) + "/Personnages/" + perso.get_name(),
                                                   self.tr("Tous fichiers (*)"))

            if filename[0]:
                with open(filename[0], "wb") as fichier:
                    # on enregistre le personnage
                    pk.Pickler(fichier).dump(perso)

    def charlist_reload(self):
        self.Char_list.clear()
        for i in self.get_characlist():
            self.Char_list.addItem(i.get_name())

    def set_selectedchar(self, number: int):
        self.parent().set_selectedchar(number)

    def get_characlist(self):
        """Method to get the list of characters from the main window"""
        return self.parent().get_characlist()

