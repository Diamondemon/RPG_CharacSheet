from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import (QMouseEvent)

import CBF


class CharPhyFrame(QGroupBox):
    """ Widget to display the physical abilities of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Physique ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.setCursor(Qt.PointingHandCursor)

        self.baselist = ["training", "dexterity", "mobility"]
        self.secondlist = ["ability", "mobility"]
        self.thirdlist = ["phys-res"]
        self.images = {}
        self.labels = []

        i = 0
        for key in self.secondlist:
            if key == "ability":
                self.images["ability"] = QSvgWidget("./Images/symb-ability.svg")
                self.images["ability"].setFixedSize(15, 15)
            else:
                self.images["mobility"] = QSvgWidget("./Images/symb-mobility.svg")
                self.images["mobility"].setFixedSize(15, 10)
            self.grid.addWidget(self.images[key], 2 * i + 2, 1)
            self.labels.append(QLabel("= "))
            self.grid.addWidget(self.labels[i], 2 * i + 2, 3)
            i += 1

        self.progressBars = {}
        i = 0
        for key in ["Entrainement physique", "Dextérité/Habileté", "Mobilité", "Résistance physique"]:
            self.grid.addWidget(QLabel(self.tr(key)), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

            bar.setStyleSheet("QProgressBar::chunk { background-color: yellow;}"
                              "QProgressBar {margin-right: 20px; text-align : right; color: black; }")
            if i < 3:
                self.progressBars[self.baselist[i]] = bar
            else:
                self.progressBars[self.thirdlist[0]] = bar
            self.grid.addWidget(bar, 2 * i + 1, 0)
            i += 1

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def mousePressEvent(self, event: QMouseEvent):
        """
        Method called when a mouse button is pressed on while above the frame. Calls the method to modify the physical
        statistics of the character

        :return: None
        """
        self.parent().modify_phy()

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
        thirdstats = selectedchar.get_thirdstats()
        i = 0
        for key in self.secondlist:
            self.labels[i].setText(f'= {secondstats["symb-"+key]}')
            i += 1

        for key in self.baselist:
            self.progressBars[key].setValue(basestats[key][0])
        for key in self.thirdlist:
            self.progressBars[key].setValue(thirdstats[key][0])
