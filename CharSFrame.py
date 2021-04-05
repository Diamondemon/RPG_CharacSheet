from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QWidget, QListWidget, QGridLayout, QPushButton)
from PySide6.QtGui import QAction
import pickle as pk
from functools import partial


class CharSFrame(QWidget):
    """Suppression d'un personnage"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.charac_list = QListWidget()
        self.suppr_choice = QPushButton("Supprimer le personnage")

        self.grid.addWidget(self.charac_list, 0, 0)
        self.grid.addWidget(self.suppr_choice, 0, 1)

        self.connect(self.suppr_choice, SIGNAL("clicked()"), self.suppr_choose)

    def refresh(self):
        for character in self.get_characlist():
            self.charac_list.addItem(character.get_name())

    @Slot()
    def suppr_choose(self):
        if self.charac_list.currentRow() != -1:
            self.master.characlist.pop(self.charac_list.currentRow())
        # self.master.Menubar.refresh()
        """
        with open("characters", "wb") as fichier:
            pk.Pickler(fichier).dump(self.master.characlist)"""

    def get_characlist(self):
        """Method to get the list of characters from the main window"""
        return self.parent().get_characlist()
