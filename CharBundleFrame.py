from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton)
from CharAtkFrame import CharAtkFrame
from CharDefFrame import CharDefFrame
from CharPhyFrame import CharPhyFrame
from CharAbiFrame import CharAbiFrame
from CharSocFrame import CharSocFrame
from CharEthFrame import CharEthFrame
from CharSymbFrame import CharSymbFrame


class CharBundleFrame(QWidget):
    """ Widget d'affichage de toutes les caractéristiques """

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.grid = QGridLayout(self)

        self.ATK = CharAtkFrame(self)
        self.grid.addWidget(self.ATK, 0, 0, 2, 1)
        self.DEF = CharDefFrame(self)
        self.grid.addWidget(self.DEF, 0, 1)
        self.PHY = CharPhyFrame(self)
        self.grid.addWidget(self.PHY, 1, 1)
        self.ABI = CharAbiFrame(self)
        self.grid.addWidget(self.ABI, 2, 0, 2, 1)
        self.SOC = CharSocFrame(self)
        self.grid.addWidget(self.SOC, 2, 1)
        self.ETH = CharEthFrame(self)
        self.grid.addWidget(self.ETH, 3, 1)
        self.SYM = CharSymbFrame(self)
        self.grid.addWidget(self.SYM, 0, 2, 4, 1)

    def refresh(self):
        for i in self.grid_slaves():
            i.refresh()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def grid(self,**kwargs):

        for i in self.grid_slaves():
            i.grid_forget()
        self.ATK.grid(row=0,column=0,rowspan=2,padx="4p",sticky="NEW",pady="2p",ipadx="4p",ipady="4p")
        self.DEF.grid(row=0,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        self.PHY.grid(row=1,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        if self.master.master.master.selectedchar.mage:
            self.ABI.grid(row=2,column=0,rowspan=2,sticky="NEW",padx="4p",pady="2p",ipadx="4p",ipady="4p")
            self.SOC.grid(row=2,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
            self.ETH.grid(row=3,column=1,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        else:
            self.ABI.grid(row=2,column=0,sticky="NEW",padx="4p",pady="2p",ipadx="4p",ipady="4p")
            self.SOC.grid(row=2,column=1,padx="4p",sticky="NEW",pady="2p",ipadx="4p",ipady="4p")
        self.SYM.grid(row=0,column=2,rowspan=4,padx="4p",sticky="NSEW",pady="2p",ipadx="4p",ipady="4p")
        self.refresh()
        # Frame.grid(self, kwargs)