from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout)

import CUF


class CharFirstSymbFrame(QWidget):
    """ Widget to display the 3 most important symb stats of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.SymbList = ["strength", "mobility", "init"]
        self.sizelist = {"strength": (24, 40), "mobility": (30, 20), "init": (30, 20)}
        self.images = {}
        self.labels = []

        i = 0
        for key in self.SymbList:
            self.images[key] = QSvgWidget("./Images/symb-" + key + ".svg")
            self.images[key].setFixedSize(self.sizelist[key][0], self.sizelist[key][1])
            self.grid.addWidget(self.images[key], 0, 2 * i)
            self.labels.append(QLabel(""))
            self.labels[i].setAlignment(Qt.AlignCenter)
            self.grid.addWidget(self.labels[i], 0, 2 * i + 1)
            i += 1

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CUF.CharUsefulFrame:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def refresh(self):
        """
        Method called torefresh the 3 most important symbol stats of the character

        :return: None
        """
        secondstats = self.get_selectedchar().get_secondstats()
        i = 0
        for key in self.SymbList:
            if key == "strength":
                self.labels[i].setText(str(secondstats["symb-"+key][0]))
            else:
                self.labels[i].setText(str(secondstats["symb-" + key]))
            i += 1
