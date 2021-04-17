from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout)
from PySide6.QtSvgWidgets import QSvgWidget
import CBF


class CharSymbFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self):
        QGroupBox.__init__(self, " Bignous ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["parry", "armor", "ability", "mobility", "perception", "stealth", "init", "T", "ps_T", "S",
                         "light", "mental", "luck", "charisma", "trading", "lightning", "sensi", "aura"]

        self.images = {}
        self.labels = []

        i = 0
        for key in self.baselist:
            self.images[key] = QSvgWidget("./Images/symb-" + key + ".svg")
            self.images[key].setFixedSize(12, 15)
            self.grid.addWidget(self.images[key], i, 0)
            self.labels.append(QLabel("= "))
            self.grid.addWidget(self.labels[i], i, 1)
            i += 1

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CBF.CharBundleFrame:
        """
        Method called to get the parent widget (the charBundleFrame)

        :return: the reference to the parent
        """
        return QGroupBox.parent(self)

    def refresh(self):
        """
        Method called to refresh all the information displayed on the frame

        :return: None
        """
        i = 0
        selectedchar = self.get_selectedchar()
        secondstats = selectedchar.get_secondstats()
        for key in self.baselist:
            self.labels[i].setText(f'= {secondstats["symb-" + key]}')
            i += 1
