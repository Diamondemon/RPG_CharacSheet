from PySide6.QtWidgets import (QGroupBox, QLabel, QGridLayout, QProgressBar)
from PySide6.QtGui import (QPixmap)


class CharAtkFrame(QGroupBox):
    """ Widget d'affichage des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QGroupBox.__init__(self, " Combat ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.baselist = ["hands", "light", "medium", "heavy", "throw", "shield"]
        self.images = {
            "mastery": QPixmap("./Images/symb-mastery.png"),
            "parry": QPixmap("./Images/symb-parry.png")}
        i = 0
        for key in self.baselist[:-1]:
            self.grid.addWidget(QLabel(pixmap=self.images["mastery"].scaled(10, 10)), 2 * i, 2)
            self.grid.addWidget(QLabel("= "), 2 * i, 3)
            i += 1
        self.grid.addWidget(QLabel(pixmap=self.images["parry"].scaled(12, 15)), 2 * i, 2)
        self.grid.addWidget(QLabel("= "), 2 * i, 3)

        i = 0
        for key in ["Mains nues", "Armes légères", "Armes moyennes", "Armes lourdes", "Armes de jet", "Bouclier"]:
            self.grid.addWidget(QLabel(key), 2 * i, 0)
            bar = QProgressBar(format="%v", minimum=0, maximum=200, value=90)
            bar.setStyleSheet("QProgressBar::chunk "
                              "{ background-color: red;}"
                              "QProgressBar {text-align : right; color: black; }")
            self.grid.addWidget(bar, 2 * i + 1, 0)
            i += 1

        """self.bind("<Button-1>", func=self.modifychar)
        for i in self.grid_slaves():
            i.bind("<Button-1>", func=self.modifychar)"""

    def refresh(self):
        i=0
        for key in self.grid_slaves(column=3):
            if i > 0:
                key["text"]=(str(self.master.master.master.master.selectedchar.secondstats["symb-mastery"][self.baselist[5-i]]))
            else:
                key["text"]=(str(self.master.master.master.master.selectedchar.secondstats["symb-parry"]))
            i+=1

        i=1
        for key in self.baselist:
            self.grid_slaves(row=i,column=0)[0].delete("all")
            self.grid_slaves(row=i,column=0)[0].create_rectangle(0,0,self.master.master.master.master.selectedchar.basestats[key][0]//2,16,fill="black",tag="jauge")
            if self.parent().parent().parent().parent().selectedchar.basestats[key][0]<=100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2+10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),tag="stat")
            elif self.parent().parent().parent().parent().selectedchar.basestats[key][0]>100:
                self.grid_slaves(row=i,column=0)[0].create_text(self.master.master.master.master.selectedchar.basestats[key][0]//2-10,8,text=str(self.master.master.master.master.selectedchar.basestats[key][0]),fill="white",tag="stat")
            i+=2


    def modifychar(self,event=None):
        """ Affiche la fenêtre de modification du personnage """
        for i in self.parent.parent().grid_slaves(column=3):
            i.grid_forget()
        self.parent.parent().MATK.grid(row=0,column=3)

    def get_selectedchar(self):
        return self.parent().get_selectedchar()
