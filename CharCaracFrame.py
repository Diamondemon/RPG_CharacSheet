from PySide6.QtWidgets import (QWidget, QGridLayout)
from CharAtkMFrame import CharAtkMFrame
from CharBundleFrame import CharBundleFrame
import CNbk


class CharCaracFrame(QWidget):
    """Affichage des statistiques d'un personnage"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.BNDL = CharBundleFrame(self)
        self.grid.addWidget(self.BNDL, 0, 0)
        self.MATK = CharAtkMFrame()

        """self.MDEF = CharDefMFrame(self)

        self.MPHY = CharPhyMFrame(self)

        self.MABI = CharAbiMFrame(self)

        self.MSOC = CharSocMFrame(self)

        self.METH = CharEthMFrame(self)"""

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def modify_abi(self):
        """
        Method called to modify the travelling statistics of the character

        :return: None
        """
        print("abi")

    def modify_atk(self):
        """
        Method called to modify the offensive statistics of the character

        :return: None
        """
        self.grid.addWidget(self.MATK, 0, 1)

    def modify_def(self):
        """
        Method called to modify the defensive statistics of the character

        :return: None
        """
        print("def")

    def modify_eth(self):
        """
        Method called to modify the magical statistics of the character

        :return: None
        """
        print("eth")

    def modify_phy(self):
        """
        Method called to modify the physical statistics of the character

        :return: None
        """
        print("phy")

    def modify_soc(self):
        """
        Method called to modify the social statistics of the character

        :return: None
        """
        print("soc")

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the Notebook)

        :return: the reference to the parent
        """
        return self.parentWidget().parent()

    def refresh(self):
        self.BNDL.refresh()
