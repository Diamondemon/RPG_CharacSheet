from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QTabWidget)
from CharCaracFrame import CharCaracFrame
from CharUsefulFrame import CharUsefulFrame
import CDF


class CharNotebook(QTabWidget):

    def __init__(self, parent):
        QTabWidget.__init__(self, parent)

        self.CharCF = CharCaracFrame()
        self.addTab(self.CharCF, "Caractéristiques")
        self.CharUF = CharUsefulFrame()
        self.addTab(self.CharUF, "Statistiques utiles")


        """
        self.CharIF = CharIFrame(self)
        self.CharCompF = CharCompetFrame(self)
        self.CharSpellF = CharSpellFrame(self)
        self.addTab(self.CharIF, "Inventaire")
        self.addTab(self.CharCompF, "Compétences")"""
        self.connect(self, SIGNAL("currentChanged(int)"), self.refresh)

    def refresh(self):
        self.CharCF.refresh()
        # self.CharUF.refresh()
        """if self.parent().get_selectedchar().ismage():
            self.CharSpellF.refresh()"""

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CDF.CharDisplayFrame:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        return QWidget.parent(self)
