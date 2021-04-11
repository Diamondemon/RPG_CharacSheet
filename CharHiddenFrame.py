from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout, QSplitter, QFrame)
from PySide6.QtGui import (QPixmap, Qt)


class CharHiddenFrame(QWidget):
    """ Widget qui affiche ce qui a été investi dans action dissimulée """

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.grid = QGridLayout(self)

        self.grid.addWidget(QLabel("Action dissimulée"), 0, 0)

        i = 0
        for key in ["Vol à la tire : ", "Embuscade : ", "Fuite : "]:
            self.grid.addWidget(QLabel(key), 1, 3 * i)
            i += 1

        """for i in range(2):
            self.columnconfigure(3*i+2,weight=1)"""



    def refresh(self):

       """for i in self.grid_slaves():
            info=i.grid_info()
            if info["row"]==1 and info["column"] in [1,4,7]:
                i.destroy()

        j=0
        for stat in ["thievery","ambush","escape"]:
            Label(self,text=self.master.master.master.selectedchar.thirdstats["hidden_action"][stat]).grid(row=1,column=3*j+1)
            j+=1"""

    def get_selectedchar(self):
        return self.master.get_selectedchar()