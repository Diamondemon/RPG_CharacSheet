from PySide6.QtWidgets import (QWidget, QGridLayout)
from CharAtkMFrame import CharAtkMFrame
from CharBundleFrame import CharBundleFrame
from CharDefMFrame import CharDefMFrame
from CharPhyMFrame import CharPhyMFrame
from CharAbiMFrame import CharAbiMFrame
from CharSocMFrame import CharSocMFrame
from CharEthMFrame import CharEthMFrame
import CNbk


class CharCaracFrame(QWidget):
    """Affichage des statistiques d'un personnage"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.BNDL = CharBundleFrame()
        self.grid.addWidget(self.BNDL, 0, 0)
        self.MATK = CharAtkMFrame()
        self.grid.addWidget(self.MATK, 0, 1)
        self.MDEF = CharDefMFrame()
        self.grid.addWidget(self.MDEF, 0, 1)
        self.MPHY = CharPhyMFrame()
        self.grid.addWidget(self.MPHY, 0, 1)
        self.MABI = CharAbiMFrame()
        self.grid.addWidget(self.MABI, 0, 1)
        self.MSOC = CharSocMFrame()
        self.grid.addWidget(self.MSOC, 0, 1)
        self.METH = CharEthMFrame()
        self.grid.addWidget(self.METH, 0, 1)

        self.clear()

    def clear(self):
        self.MATK.hide()
        self.MDEF.hide()
        self.MPHY.hide()
        self.MABI.hide()
        self.MSOC.hide()
        self.METH.hide()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def modify_abi(self):
        """
        Method called to modify the travelling statistics of the character

        :return: None
        """
        self.clear()
        self.MABI.show()

    def modify_atk(self):
        """
        Method called to modify the offensive statistics of the character

        :return: None
        """
        self.clear()
        self.MATK.show()

    def modify_def(self):
        """
        Method called to modify the defensive statistics of the character

        :return: None
        """
        self.clear()
        self.MDEF.show()

    def modify_eth(self):
        """
        Method called to modify the magical statistics of the character

        :return: None
        """
        self.clear()
        self.METH.show()

    def modify_phy(self):
        """
        Method called to modify the physical statistics of the character

        :return: None
        """
        self.clear()
        self.MPHY.show()

    def modify_soc(self):
        """
        Method called to modify the social statistics of the character

        :return: None
        """
        self.clear()
        self.MSOC.show()

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the Notebook)

        :return: the reference to the parent
        """
        return self.parentWidget().parent()

    def refresh(self):
        self.BNDL.refresh()
