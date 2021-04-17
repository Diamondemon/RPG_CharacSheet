from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtCore import Qt
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QMouseEvent
import CBF


class CharAtkFrame(QGroupBox):
    """ Widget to display the offensive abilities of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Combat ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.setCursor(Qt.PointingHandCursor)

        self.baselist = ["hands", "light", "medium", "heavy", "throw", "shield"]
        self.images = {}
        self.labels = []

        i = 0
        for key in self.baselist:
            if key != "shield":
                self.images["mastery-"+key] = QSvgWidget("./Images/symb-mastery.svg")
                self.images["mastery-"+key].setFixedSize(10, 10)
            else:
                self.images["mastery-" + key] = QSvgWidget("./Images/symb-parry.svg")
                self.images["mastery-" + key].setFixedSize(12, 15)
            self.grid.addWidget(self.images["mastery-" + key], 2 * i, 1)
            self.labels.append(QLabel("= "))
            self.grid.addWidget(self.labels[i], 2 * i, 2)
            i += 1

        self.progressBars = {}
        i = 0
        for key in ["Mains nues", "Armes légères", "Armes moyennes", "Armes lourdes", "Armes de jet", "Bouclier"]:
            self.grid.addWidget(QLabel(self.tr(key)), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

            bar.setStyleSheet("QProgressBar::chunk { background-color: red;}"
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
        Method called when a mouse button is pressed on while above the frame. Calls the method to modify the offensive
        statistics of the character

        :return: None
        """
        self.parent().modify_atk()

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
            if key != "shield":
                self.labels[i].setText(f'= {secondstats["symb-mastery"][key]}')

            else:
                self.labels[i].setText(f'= {secondstats["symb-parry"]}')

            self.progressBars[key].setValue(basestats[key][0])

            i += 1
