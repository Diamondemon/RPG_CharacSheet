from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)
from PySide6.QtSvgWidgets import QSvgWidget

import CBF


class CharDefFrame(QGroupBox):
    """ Widget to display the defensive abilities of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Armure ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["armor"]
        self.images = {}
        self.labels = []

        self.images["armor"] = QSvgWidget("./Images/symb-armor.svg")
        self.images["armor"].setFixedSize(12, 20)
        self.grid.addWidget(self.images["armor"], 0, 1)
        self.labels.append(QLabel("= "))
        self.grid.addWidget(self.labels[0], 0, 2)

        self.grid.addWidget(QLabel("Armure"), 0, 0)
        self.progressBar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

        self.progressBar.setStyleSheet("QProgressBar::chunk { background-color: pink;}"
                                       "QProgressBar {margin-right: 20px; text-align : right; color: black; }")
        self.grid.addWidget(self.progressBar, 1, 0)

        self.labels.append(QLabel("Palier d'armure"))
        self.grid.addWidget(self.labels[1], 2, 0)

    def refresh(self):
        """
        Method called to refresh all the information displayed on the frame

        :return: None
        """
        selectedchar = self.get_selectedchar()
        basestats = selectedchar.get_basestats()
        secondstats = selectedchar.get_secondstats()
        self.labels[0].setText("= " + str(secondstats["symb-armor"]))
        self.labels[1].setText("Palier d'armure = " + str(secondstats["armor-level"]))

        self.progressBar.setValue(basestats["armor"][0])

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
