from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtSvgWidgets import QSvgWidget
import CBF


class CharAtkFrame(QGroupBox):
    """ Widget to display the offensive abilities of the character """

    def __init__(self, parent):
        QGroupBox.__init__(self, " Combat ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["hands", "light", "medium", "heavy", "throw", "shield"]

        self.images = {"parry": QSvgWidget("./Images/symb-parry.svg")}
        self.images["parry"].setFixedSize(12, 15)
        for key in self.baselist[:-1]:
            self.images["mastery-"+key] = QSvgWidget("./Images/symb-mastery.svg")
            self.images["mastery-"+key].setFixedSize(10, 10)

        self.progressBars = {}
        i = 0
        for key in self.baselist[:-1]:
            self.grid.addWidget(self.images["mastery-"+key], 2 * i, 2)
            self.grid.addWidget(QLabel("= "), 2 * i, 3)
            i += 1
        self.grid.addWidget(self.images["parry"], 2 * i, 2)
        self.grid.addWidget(QLabel("= "), 2 * i, 3)

        i = 0
        for key in ["Mains nues", "Armes légères", "Armes moyennes", "Armes lourdes", "Armes de jet", "Bouclier"]:
            self.grid.addWidget(QLabel(self.tr(key)), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

            bar.setStyleSheet("QProgressBar::chunk "
                              "{ background-color: red;}"
                              "QProgressBar {margin-right: 20px; text-align : right; color: black; }")
            self.progressBars[self.baselist[i]] = bar
            self.grid.addWidget(bar, 2 * i + 1, 0)
            i += 1

    def refresh(self):
        """
        i = 0
        for key in self.grid_slaves(column=3):
            if i > 0:
                key["text"]=(str(self.master.master.master.master.selectedchar.secondstats["symb-mastery"][self.baselist[5-i]]))
            else:
                key["text"]=(str(self.master.master.master.master.selectedchar.secondstats["symb-parry"]))
            i += 1
        """

        for key in self.baselist:
            self.progressBars[key].setValue(self.get_selectedchar().get_basestats()[key][0])

    def modifychar(self):
        """ Affiche la fenêtre de modification du personnage """
        pass

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CBF.CharBundleFrame:
        """
        Method called to get the parent widget (the charBundleFrame)

        :return: the reference to the parent
        """
        return QGroupBox.parent(self)
