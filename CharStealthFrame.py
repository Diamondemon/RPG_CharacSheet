from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout)

import CUF


class CharStealthFrame(QWidget):
    """ Widget qui affiche l'investissement de la furtivité dans la fiche résumé """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setMaximumHeight(120)

        self.furtiflist = [["ground", "moving", "assassination"], ["shadow", "not-moving", "identity"],
                           ["smell", "disguise", "nature-field"]]
        self.labels = []

        self.stealth_image = QSvgWidget("./Images/symb-stealth.svg")
        self.stealth_image.setFixedSize(18, 8)
        self.grid.addWidget(QLabel("Furtivité "), 0, 0)
        self.grid.addWidget(self.stealth_image, 0, 1)

        i = 0
        for key in ["Silence : ", "Dissimulation : ", "Camouflage : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 1, 2 * i)
            i += 1

        i = 2
        for key in ["Sol : ", "Déplacement : ", "Assassinat : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 0)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i - 2], i, 1)
            i += 1

        i = 2
        for key in ["Ombre : ", "Immobilité : ", "Identité : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 2)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i + 1], i, 3)
            i += 1

        i = 2
        for key in ["Odeur : ", "Déguisement : ", "Nature/Terrain : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 4)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i + 4], i, 5)
            i += 1

    def refresh(self):
        thirdstats = self.get_selectedchar().get_thirdstats()
        j = 0
        for key in ["silence", "hiding", "camo"]:
            i = 2
            for stat in self.furtiflist[j]:
                self.labels[3 * j + i - 2].setText(str(thirdstats[key][stat]))
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
