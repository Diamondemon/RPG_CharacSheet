from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton)
from CharAtkFrame import CharAtkFrame
from CharDefFrame import CharDefFrame
from CharPhyFrame import CharPhyFrame
from CharAbiFrame import CharAbiFrame
from CharSocFrame import CharSocFrame
from CharEthFrame import CharEthFrame
from CharSymbFrame import CharSymbFrame
import CCaF


class CharBundleFrame(QWidget):
    """ Widget d'affichage de toutes les caractéristiques """

    def __init__(self):
        QWidget.__init__(self)
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
        self.ATK.refresh()
        self.SOC.refresh()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        return QWidget.parent(self)
