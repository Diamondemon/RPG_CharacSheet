from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)

import CBF


class CharEthFrame(QGroupBox):
    """ Widget to display the magical abilities of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Ether ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["power", "mastery", "sensitivity"]
        self.secondlist = ["lightning", "sensi", "aura"]
        self.sizelist = {"lightning": (12, 15), "sensi": (12, 15), "aura": (15, 15)}
        self.images = {}
        self.labels = []

        for key in self.secondlist:
            self.images[key] = QSvgWidget("./Images/symb-" + key + ".svg")
            self.images[key].setFixedSize(self.sizelist[key][0], self.sizelist[key][1])

        self.progressBars = {}
        i = 0
        for key in ["Puissance", "Maîtrise", "Sensibilité", "Aura"]:
            if i != 1:
                self.labels.append(QLabel("= "))
                if i > 1:
                    self.grid.addWidget(self.images[self.secondlist[i - 1]], 2 * i, 1)
                    self.grid.addWidget(self.labels[i - 1], 2 * i, 2)
                else:
                    self.grid.addWidget(self.images[self.secondlist[i]], 2 * i, 1)
                    self.grid.addWidget(self.labels[i], 2 * i, 2)

            self.grid.addWidget(QLabel(self.tr(key)), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

            bar.setStyleSheet("QProgressBar::chunk { background-color: green;}"
                              "QProgressBar {margin-right: 20px; text-align : right; color: black; }")
            if i < 3:
                self.progressBars[self.baselist[i]] = bar
            else:
                self.progressBars[self.secondlist[2]] = bar
            self.grid.addWidget(bar, 2 * i + 1, 0)
            i += 1

    def refresh(self):
        """
        Method called to refresh all the information displayed on the frame

        :return: None
        """
        selectedchar = self.get_selectedchar()
        basestats = selectedchar.get_basestats()
        secondstats = selectedchar.get_secondstats()
        i = 0
        for key in self.secondlist:
            self.labels[i].setText("= " + str(secondstats["symb-" + key]))
            i += 1

        for key in self.baselist:
            self.progressBars[key].setValue(basestats[key][0])

        self.progressBars["aura"].setValue(secondstats["aura"][0])

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
