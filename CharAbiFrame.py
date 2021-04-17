from PySide6.QtGui import QMouseEvent
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtSvgWidgets import QSvgWidget
import CBF


class CharAbiFrame(QGroupBox):
    """ Widget to display the travelling abilities of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Habileté ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.setCursor(Qt.PointingHandCursor)

        self.baselist = ["perception", "stealth", "reflex", "wit", "mental-res"]
        self.secondlist = ["perception", "S", "stealth", "T", "init", "light", "mental"]
        self.sizelist = {"perception": (12, 15), "S": (6, 9), "stealth": (18, 8), "T": (6, 9), "init": (15, 10),
                         "light": (12, 15), "mental": (12, 12)}
        self.images = {}
        self.labels = []

        for key in self.secondlist:
            self.images[key] = QSvgWidget("./Images/symb-"+key+".svg")
            self.images[key].setFixedSize(self.sizelist[key][0], self.sizelist[key][1])
            self.labels.append(QLabel("= "))

        self.progressBars = {}
        i = 0
        for key in ["Perception", "Furtivité", "Réflexes", "Intelligence", "Résistance mentale"]:
            self.grid.addWidget(QLabel(self.tr(key)), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

            bar.setStyleSheet("QProgressBar::chunk { background-color: blue;}"
                              "QProgressBar {margin-right: 20px; text-align : right; color: black; }")
            self.progressBars[self.baselist[i]] = bar
            self.grid.addWidget(bar, 2 * i + 1, 0)

            if i < 2:
                self.grid.addWidget(self.images[self.secondlist[2 * i]], 2 * i, 1)
                self.grid.addWidget(self.labels[2*i], 2 * i, 2)
                self.grid.addWidget(self.images[self.secondlist[2 * i + 1]], 2 * i + 1, 1)
                self.grid.addWidget(self.labels[2*i+1], 2 * i + 1, 2)
            else:
                self.grid.addWidget(self.images[self.secondlist[i + 2]], 2 * i, 1)
                self.grid.addWidget(self.labels[i+2], 2 * i, 2)
            i += 1

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def mousePressEvent(self, event: QMouseEvent):
        """
        Method called when a mouse button is pressed on while above the frame. Calls the method to modify the travelling
        statistics of the character

        :return: None
        """
        self.parent().modify_abi()

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
        selectedchar = self.get_selectedchar()
        basestats = selectedchar.get_basestats()
        secondstats = selectedchar.get_secondstats()
        i = 0
        for key in self.baselist:
            self.progressBars[key].setValue(basestats[key][0])
            i += 1

        i = 0
        for key in self.secondlist:
            self.labels[i].setText(f'= {secondstats["symb-" + key]}')
            i += 1
