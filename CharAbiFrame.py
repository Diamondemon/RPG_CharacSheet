from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)
from PySide6.QtSvgWidgets import QSvgWidget


class CharAbiFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QGroupBox.__init__(self, " Habileté ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["perception", "stealth", "reflex", "wit", "mental-res"]
        self.secondlist = ["perception", "S", "stealth", "T", "init", "light", "mental"]
        self.sizelist = {"perception": (12, 15), "S": (6, 9), "stealth": (18, 8), "T": (6, 9), "init": (15, 10),
                         "light": (12, 15), "mental": (12, 12)}
        self.images = {}
        for key in self.secondlist:
            if key == "perception":
                self.images[key] = QSvgWidget("./Images/symb-perception.svg")
                self.images[key].setFixedSize(self.sizelist[key][0], self.sizelist[key][1])
            else:
                self.images[key] = QPixmap("./Images/symb-" + key + ".png")

                self.images[key] = self.images[key].scaled(self.sizelist[key][0], self.sizelist[key][1])

        i = 0
        for key in ["Perception", "Furtivité", "Réflexes", "Intelligence", "Résistance mentale"]:
            self.grid.addWidget(QLabel(key), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)
            bar.setStyleSheet("QProgressBar::chunk "
                              "{ background-color: blue;}"
                              "QProgressBar {text-align : right; color: black; }")
            self.grid.addWidget(bar, 2 * i + 1, 0)
            if i < 2:
                if key == "Perception":
                    self.grid.addWidget(self.images[key.lower()], 2*i, 1)
                    self.grid.addWidget(QLabel("= "), 2 * i, 2)
                else:
                    self.grid.addWidget(QLabel(pixmap=self.images[self.secondlist[2 * i]]), 2 * i, 1)
                    self.grid.addWidget(QLabel("= "), 2 * i, 2)
                self.grid.addWidget(QLabel(pixmap=self.images[self.secondlist[2 * i + 1]]), 2 * i + 1, 1)
                self.grid.addWidget(QLabel("= "), 2 * i + 1, 2)
            else:
                self.grid.addWidget(QLabel(pixmap=self.images[self.secondlist[i + 2]]), 2 * i, 1)
                self.grid.addWidget(QLabel("= "), 2 * i, 2)
            i += 1

        """self.bind("<Button-1>", func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>", func=self.modifychar)"""

    def refresh(self):
        i = 1
        for key in self.grid_slaves(column=2):
            key["text"] = self.master.master.master.master.selectedchar.secondstats[
                "symb-" + self.secondlist[len(self.secondlist) - i]]
            i += 1
        i = 1
        for key in self.baselist:
            self.grid_slaves(row=i, column=0)[0].delete("all")
            self.grid_slaves(row=i, column=0)[0].create_rectangle(0, 0,
                                                                  self.master.master.master.master.selectedchar.basestats[
                                                                      key][0] // 2, 16, fill="black", tag="jauge")
            if self.master.master.master.master.selectedchar.basestats[key][0] <= 100:
                self.grid_slaves(row=i, column=0)[0].create_text(
                    self.master.master.master.master.selectedchar.basestats[key][0] // 2 + 10, 8,
                    text=str(self.master.master.master.master.selectedchar.basestats[key][0]), tag="stat")
            elif self.master.master.master.master.selectedchar.basestats[key][0] > 100:
                self.grid_slaves(row=i, column=0)[0].create_text(
                    self.master.master.master.master.selectedchar.basestats[key][0] // 2 - 10, 8,
                    text=str(self.master.master.master.master.selectedchar.basestats[key][0]), fill="white", tag="stat")
            i += 2

    def modifychar(self, event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MABI.grid(row=0, column=3)

    def get_selectedchar(self):
        return self.master.get_selectedchar()
