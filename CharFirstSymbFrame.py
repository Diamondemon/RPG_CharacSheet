from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout)
from PySide6.QtGui import (QPixmap)


class CharFirstSymbFrame(QWidget):

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.grid = QGridLayout(self)
        self.SymbList = ["strength", "mobility", "init"]
        self.sizelist = {"strength": (24, 40), "mobility": (30, 20), "init": (30, 20)}

        self.images = {}
        i = 0
        for key in self.SymbList:
            self.images[key] = QPixmap("./Images/symb-" + key + ".png")
            self.images[key] = self.images[key].scaled(self.sizelist[key][0], self.sizelist[key][1])
            self.grid.addWidget(QLabel(pixmap=self.images[key]), 0, 2 * i)
            i += 1

        """for i in range(6):
            self.columnconfigure(i, weight=1)"""


    def refresh(self):
        """for i in self.grid_slaves():
            if i.grid_info()["column"]%2==1:
                i.destroy()

        i=0
        for key in self.SymbList:
            if key=="strength":
                Label(self,text=self.master.master.master.selectedchar.secondstats["symb-"+key][0]).grid(row=0,column=2*i+1,sticky="w")
            else:
                Label(self,text=self.master.master.master.selectedchar.secondstats["symb-"+key]).grid(row=0,column=2*i+1,sticky="w")
            i+=1"""

    def get_selectedchar(self):
        return self.master.get_selectedchar()