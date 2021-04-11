from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QPlainTextEdit, QComboBox, QPushButton,
                               QTreeWidget, QTreeWidgetItem)
from CharAtkMFrame import CharAtkMFrame
from CharBundleFrame import CharBundleFrame


class CharCaracFrame(QWidget):
    """Affichage des statistiques d'un personnage"""

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.grid = QGridLayout(self)

        self.BNDL = CharBundleFrame(self)
        self.grid.addWidget(self.BNDL, 0, 0)
        self.MATK = CharAtkMFrame(self)

        """self.MDEF = CharDefMFrame(self)

        self.MPHY = CharPhyMFrame(self)

        self.MABI = CharAbiMFrame(self)

        self.MSOC = CharSocMFrame(self)

        self.METH = CharEthMFrame(self)"""

    def refresh(self):
        for i in self.grid_slaves():
            i.grid_forget()
        self.BNDL.grid(row=0, column=0, sticky="N")

    def get_selectedchar(self):
        return self.parent().get_selectedchar()