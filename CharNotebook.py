from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QTabWidget, QLineEdit, QLabel, QGridLayout, QPlainTextEdit, QComboBox, QPushButton,
                               QTreeWidget, QTreeWidgetItem)
from CharCaracFrame import CharCaracFrame
from CharUsefulFrame import CharUsefulFrame


class CharNotebook(QTabWidget):
    def __init__(self, parent):
        QTabWidget.__init__(self, parent)

        self.CharCF = CharCaracFrame(self)
        self.addTab(self.CharCF, "Caractéristiques")
        self.CharUF = CharUsefulFrame(self)
        self.addTab(self.CharUF, "Statistiques utiles")

        """
        self.CharIF = CharIFrame(self)
        self.CharCompF = CharCompetFrame(self)
        self.CharSpellF = CharSpellFrame(self)
        self.addTab(self.CharIF, "Inventaire")
        self.addTab(self.CharCompF, "Compétences")"""

    def refresh(self):
        self.CharCF.refresh()
        if self.parent().selectedchar.mage:
            self.CharSpellF.refresh()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()