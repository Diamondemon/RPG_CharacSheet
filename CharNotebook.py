from PySide6.QtCore import SIGNAL, Slot
from PySide6.QtWidgets import (QWidget, QTabWidget)
from CharCaracFrame import CharCaracFrame
from CharUsefulFrame import CharUsefulFrame
from CharIFrame import CharIFrame
from CharCompetFrame import CharCompetFrame
from CharSpellFrame import CharSpellFrame
import CDF


class CharNotebook(QTabWidget):
    """ Widget that contains all the wigets used to display and manage the character """

    def __init__(self, parent):
        QTabWidget.__init__(self, parent)

        self.CharCF = CharCaracFrame()
        self.addTab(self.CharCF, self.tr("Caractéristiques"))
        self.CharUF = CharUsefulFrame()
        self.addTab(self.CharUF, self.tr("Statistiques utiles"))
        self.CharIF = CharIFrame()
        self.addTab(self.CharIF, self.tr("Inventaire"))
        self.CharCompF = CharCompetFrame()
        self.addTab(self.CharCompF, self.tr("Compétences"))
        self.CharSpellF = CharSpellFrame()

        self.connect(self, SIGNAL("tabBarClicked(int)"), self.refresh)

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
        Method called to get the available spells

        :return: Reference to the list of spells
        """
        return self.parent().get_spelllist()

    def handle_spells(self):
        """
        Method called to handle the display of the spell tab

        :return: None
        """
        if self.get_selectedchar().ismage():
            self.removeTab(4)
            self.addTab(self.CharSpellF, self.tr("Sorts"))
        else:
            self.removeTab(4)

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
