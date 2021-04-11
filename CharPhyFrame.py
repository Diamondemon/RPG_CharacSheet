from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)


class CharPhyFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QGroupBox.__init__(self, " Physique ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["training", "dexterity", "mobility"]
        self.secondlist = ["ability", "mobility"]
        self.thirdlist = ["phys-res"]
        self.images = {"ability": QPixmap("./Images/symb-ability.png"),
                       "mobility": QPixmap("./Images/symb-mobility.png")}
        self.images["ability"] = self.images["ability"].scaled(15, 15)
        self.images["mobility"] = self.images["mobility"].scaled(15, 10)

        i = 1
        for key in self.secondlist:
            self.grid.addWidget(QLabel(pixmap=self.images[key]), 2 * i, 1)
            self.grid.addWidget(QLabel("= "), 2 * i, 2)
            i += 1
        i = 0
        for key in ["Entrainement physique", "Dextérité/Habileté", "Mobilité", "Résistance physique"]:
            self.grid.addWidget(QLabel(key), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)
            bar.setStyleSheet("QProgressBar::chunk "
                              "{ background-color: yellow;}"
                              "QProgressBar {text-align : right; color: black; }")
            self.grid.addWidget(bar, 2 * i + 1, 0)
            i += 1

        """self.bind("<Button-1>", func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>", func=self.modifychar)"""

    def refresh(self):
        i = 1
        for key in self.grid_slaves(column=2):
            if i == 2:
                key["text"] = self.master.master.master.master.selectedchar.secondstats["symb-ability"]
            else:
                key["text"] = self.master.master.master.master.selectedchar.secondstats["symb-mobility"]
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
        for key in self.thirdlist:
            self.grid_slaves(row=i, column=0)[0].delete("all")
            self.grid_slaves(row=i, column=0)[0].create_rectangle(0, 0,
                                                                  self.master.master.master.master.selectedchar.thirdstats[
                                                                      key][0] // 2, 16, fill="black", tag="jauge")
            if self.master.master.master.master.selectedchar.thirdstats[key][0] <= 100:
                self.grid_slaves(row=i, column=0)[0].create_text(
                    self.master.master.master.master.selectedchar.thirdstats[key][0] // 2 + 10, 8,
                    text=str(self.master.master.master.master.selectedchar.thirdstats[key][0]), tag="stat")
            elif self.master.master.master.master.selectedchar.thirdstats[key][0] > 100:
                self.grid_slaves(row=i, column=0)[0].create_text(
                    self.master.master.master.master.selectedchar.thirdstats[key][0] // 2 - 10, 8,
                    text=str(self.master.master.master.master.selectedchar.thirdstats[key][0]), fill="white",
                    tag="stat")
            i += 2

    def modifychar(self, event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MPHY.grid(row=0, column=3)

    def get_selectedchar(self):
        return self.master.get_selectedchar()