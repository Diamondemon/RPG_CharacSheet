from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QMouseEvent
import CBF


class CharSocFrame(QGroupBox):
    """ Widget to display the social abilities of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Social ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["charisma", "trading", "luck"]
        self.sizelist = {"charisma": (12, 12), "trading": (15, 13), "luck": (12, 18)}
        self.images = {}
        self.labels = []

        i = 0
        for key in self.baselist:
            self.images[key] = QSvgWidget("./Images/symb-"+key+".svg")
            self.images[key].setFixedSize(self.sizelist[key][0], self.sizelist[key][1])
            self.grid.addWidget(self.images[self.baselist[i]], 2*i, 1)
            self.labels.append(QLabel("= "))
            self.grid.addWidget(self.labels[i], 2 * i, 2)
            i += 1

        self.progressBars = {}
        i = 0
        for key in ["Charisme", "Commerce", "Chance"]:
            self.grid.addWidget(QLabel(self.tr(key)), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

            bar.setStyleSheet("QProgressBar::chunk { background-color: orange;}"
                              "QProgressBar {margin-right: 20px; text-align : right; color: black; }")

            self.progressBars[self.baselist[i]] = bar
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
        Method called when a mouse button is pressed on while above the frame. Calls the method to modify the social
        statistics of the character

        :return: None
        """
        self.parent().modify_soc()

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
            self.labels[i].setText("= " + str(secondstats["symb-"+key]))
            self.progressBars[key].setValue(basestats[key][0])
            i += 1
