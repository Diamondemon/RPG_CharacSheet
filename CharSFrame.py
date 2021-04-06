from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QWidget, QListWidget, QGridLayout, QPushButton)


class CharSFrame(QWidget):
    """Suppression d'un personnage"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.charac_list = QListWidget()
        self.suppr_choice = QPushButton(self.tr("Supprimer le personnage"))

        self.grid.addWidget(self.charac_list, 0, 0)
        self.grid.addWidget(self.suppr_choice, 0, 1)

        self.connect(self.suppr_choice, SIGNAL("clicked()"), self.suppr_choose)

    def get_characlist(self):
        """Method to get the list of characters from the main window"""
        return self.parent().get_characlist()

    def refresh(self):
        self.charac_list.clear()
        for character in self.get_characlist():
            self.charac_list.addItem(character.get_name())

    @Slot()
    def suppr_choose(self):
        if self.charac_list.currentRow() != -1:
            self.parent().pop(self.charac_list.currentRow())
            self.refresh()
