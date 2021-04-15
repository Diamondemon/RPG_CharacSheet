from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)
from PySide6.QtSvgWidgets import QSvgWidget
import CBF


class CharSocFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QGroupBox.__init__(self, " Social ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["charisma", "trading", "luck"]
        self.sizelist = {"charisma": (12, 12), "trading": (15, 13), "luck": (12, 18)}
        self.images = {}
        for key in self.baselist:
            self.images[key] = QSvgWidget("./Images/symb-"+key+".svg")
            self.images[key].setFixedSize(self.sizelist[key][0], self.sizelist[key][1])

        self.progressBars = {}
        i = 0
        for key in ["Charisme", "Commerce", "Chance"]:
            self.grid.addWidget(QLabel(self.tr(key)), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)

            bar.setStyleSheet("QProgressBar::chunk { background-color: orange;}"
                              "QProgressBar {margin-right: 20px; text-align : right; color: black; }")

            self.progressBars[self.baselist[i]] = bar
            self.grid.addWidget(bar, 2 * i + 1, 0)
            self.grid.addWidget(self.images[self.baselist[i]], 2*i, 1)
            self.grid.addWidget(QLabel("= "), 2 * i, 2)
            i += 1

        """self.bind("<Button-1>", func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>", func=self.modifychar)"""

    def refresh(self):
        """
        i = 1
        for key in self.grid_slaves(column=2):
            key["text"] = self.master.master.master.master.selectedchar.secondstats[
                "symb-" + self.baselist[len(self.baselist) - i]]
            i += 1
        i = 1
        """
        for key in self.baselist:
            self.progressBars[key].setValue(self.get_selectedchar().get_basestats()[key][0])

    def modifychar(self, event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MSOC.grid(row=0, column=3)

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CBF.CharBundleFrame:
        """
        Method called to get the parent widget (the charBundleFrame)

        :return: the reference to the parent
        """
        return QGroupBox.parent(self)
