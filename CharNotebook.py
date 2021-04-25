from PySide6.QtCore import SIGNAL, Slot
from PySide6.QtWidgets import (QWidget, QTabWidget)
from CharCaracFrame import CharCaracFrame
from CharUsefulFrame import CharUsefulFrame
from CharIFrame import CharIFrame
from CharCompetFrame import CharCompetFrame
from CharSpellFrame import CharSpellFrame
import CDF


class CharNotebook(QTabWidget):

    def __init__(self, parent):
        QTabWidget.__init__(self, parent)

        self.CharCF = CharCaracFrame()
        self.addTab(self.CharCF, "Caractéristiques")
        self.CharUF = CharUsefulFrame()
        self.addTab(self.CharUF, "Statistiques utiles")
        self.CharIF = CharIFrame()
        self.addTab(self.CharIF, "Inventaire")
        self.CharCompF = CharCompetFrame()
        self.addTab(self.CharCompF, "Compétences")
        self.CharSpellF = CharSpellFrame()
        self.addTab(self.CharSpellF, "Sorts")

        self.connect(self, SIGNAL("currentChanged(int)"), self.refresh)

    def get_competlist(self):
        """
        Method called to get the available competences

        :return: Reference to the list of competences
        """
        return self.parent().get_competlist()

    def get_selectedchar(self):
        """
        Method called to get the character to be displayed

        :return: the reference to the character
        """
        return self.parent().get_selectedchar()

    def get_spelllist(self):
        """
        Method called to get the available competences

        :return: Reference to the list of competences
        """
        return self.parent().get_spelllist()

    def parent(self) -> CDF.CharDisplayFrame:
        """
        Method called to get the parent widget (the char display)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    @Slot()
    def refresh(self):
        """
        Method called to refresh all the widgets contained

        :return: None
        """
        self.CharCF.refresh()
        self.CharUF.refresh()
        self.CharIF.refresh()
        self.CharCompF.refresh()
        if self.get_selectedchar().ismage():
            self.CharSpellF.refresh()

    def refresh_base(self):
        """
        Method called to refresh the base frame of the CharDisplay

        :return: None
        """
        self.parent().refresh_base()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()
