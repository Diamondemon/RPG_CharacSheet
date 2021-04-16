from PySide6.QtCore import SIGNAL
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout, QSplitter, QFrame)
from PySide6.QtGui import (QPixmap, Qt)

import CUF


class CharPercepFrame(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)

        self.perceplist = [["intention", "thing-info", "bestiary"], ["trap", "find", "tracking"],
                           ["ennemies", "threat", "curse"]]
        self.labels = []

        self.percep_image = QSvgWidget("./Images/symb-perception.svg")
        self.percep_image.setFixedSize(12, 15)
        self.grid.addWidget(QLabel("Analyse/Perception "), 0, 0, 1, 2)
        self.grid.addWidget(self.percep_image, 0, 2)

        i = 2
        for key in ["Vue :", "Ouïe :", "Odorat :"]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 0)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i-2], i, 1)
            i += 1

        separator = QFrame(self)
        separator.setFrameShape(QFrame.VLine)
        self.grid.addWidget(separator, 1, 2, 4, 1)

        i = 0
        for key in ["Indice : ", "Terrain : ", "Embuscade : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 1, 2 * i + 3)
            i += 1

        i = 2
        for key in ["Intention : ", "Objet-info : ", "Bestiaire : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 3)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i+1], i, 4)
            i += 1

        i = 2
        for key in ["Piège : ", "Trouver Objets : ", "Pistage : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 5)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i+4], i, 6)
            i += 1

        i = 2
        for key in ["Adversaires : ", "Menace : ", "Malédiction : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 7)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i+7], i, 8)
            i += 1

    def refresh(self):
        thirdstats = self.get_selectedchar().get_thirdstats()

        i = 2
        for key in ["sight", "hearing", "smell"]:
            self.labels[i-2].setText(str(thirdstats[key]))
            i += 1

        j = 0
        for key in ["clue", "field", "ambush"]:
            i = 2
            for stat in self.perceplist[j]:
                self.labels[3 * j + i + 1].setText(str(thirdstats[key][stat]))
                i += 1
            j += 1

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
        return self.parentWidget()
