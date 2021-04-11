from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)


class CharSocFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QGroupBox.__init__(self, " Social ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["charisma", "trading", "luck"]
        self.secondlist = ["charisma", "trading", "luck"]
        self.sizelist = {"charisma": (12, 12), "trading": (15, 13), "luck": (12, 18)}
        self.images = {}
        for key in self.secondlist:
            self.images[key] = QPixmap("./Images/symb-" + key + ".png")
            self.images[key] = self.images[key].scaled(self.sizelist[key][0], self.sizelist[key][1])

        i = 0
        for key in ["Charisme", "Commerce", "Chance"]:
            self.grid.addWidget(QLabel(key), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)
            bar.setStyleSheet("QProgressBar::chunk "
                              "{ background-color: orange;}"
                              "QProgressBar {text-align : right; color: black; }")
            self.grid.addWidget(bar, 2 * i + 1, 0)
            self.grid.addWidget(QLabel(pixmap=self.images[self.secondlist[i]]), 2 * i, 1)
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
        self.master.master.MSOC.grid(row=0, column=3)

    def get_selectedchar(self):
        return self.master.get_selectedchar()
