from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)
from PySide6.QtSvgWidgets import QSvgWidget


class CharDefFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QGroupBox.__init__(self, " Armure ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["armor"]
        self.images = {
            "armor": QSvgWidget("./Images/symb-armor.svg")}
        self.images["armor"].setFixedSize(12, 20)

        self.grid.addWidget(QLabel("Armure"), 0, 0)
        bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)
        bar.setStyleSheet("QProgressBar::chunk "
                          "{ background-color: pink;}"
                          "QProgressBar {text-align : right; color: black; }")
        self.grid.addWidget(bar, 1, 0)
        self.grid.addWidget(self.images["armor"], 0, 1)
        self.grid.addWidget(QLabel("= "), 0, 2)
        self.grid.addWidget(QLabel("Palier d'armure"), 2, 0)

        """self.bind("<Button-1>", func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>", func=self.modifychar)"""

    def refresh(self):
        for i in self.grid_slaves(column=2):
            i["text"] = self.master.master.master.master.selectedchar.secondstats["symb-armor"]

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
        self.grid_slaves(row=2, column=1)[0]["text"] = str(
            self.master.master.master.master.selectedchar.secondstats["armor-level"])
        # Label(self,text=str(self.master.master.master.selectedchar.secondstats["armor-level"])).grid(row=i-1,column=1)

    def modifychar(self, event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.master.master.grid_slaves(column=3):
            i.grid_forget()
        self.master.master.MDEF.grid(row=0, column=3)

    def get_selectedchar(self):
        return self.master.get_selectedchar()
