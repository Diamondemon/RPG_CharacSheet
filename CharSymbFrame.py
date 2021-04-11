from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)


class CharSymbFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QGroupBox.__init__(self, " Bignous ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["parry", "armor", "ability", "mobility", "perception", "stealth", "init", "T", "ps_T", "S",
                         "light", "mental", "luck", "charisma", "trading", "lightning", "sensi", "aura"]
        i = 0
        self.images = {}

        for key in self.baselist:
            self.images[key] = QPixmap("./Images/symb-" + key + ".png")
            self.images[key] = self.images[key].scaled(12, 15)
            self.grid.addWidget(QLabel(pixmap=self.images[key]), i, 0)
            self.grid.addWidget(QLabel("= "), i, 1)
            i += 1

    def refresh(self):
        i = 0
        for key in self.baselist:
            """Label(self, text=self.master.master.master.master.selectedchar.secondstats["symb-" + key]).grid(row=i,
                                                                                                            column=1)"""
            i += 1

    def get_selectedchar(self):
        return self.master.get_selectedchar()
