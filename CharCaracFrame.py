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
    """ Widget to display and modify the caracteristics of the selected character """

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
        """
        Method called to hide all the modifying frames

        :return:
        """
        self.MATK.hide()
        self.MDEF.hide()
        self.MPHY.hide()
        self.MABI.hide()
        self.MSOC.hide()
        self.METH.hide()

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def modify_abi(self):
        """
        Method called to modify the travelling statistics of the character

        :return: None
        """
        self.clear()
        self.MABI.show()
        self.MABI.refresh()

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
        """
        Method called to refresh all the information displayed on the subframes

        :return: None
        """
        self.BNDL.refresh()
        self.MABI.refresh()

    def refresh_abi(self):
        """
        Method called to refresh only the ability frame

        :return: None
        """
        self.BNDL.refresh_abi()

    def refresh_atk(self):
        """
        Method called to refresh only the attack frame

        :return: None
        """
        self.BNDL.refresh_atk()

    def refresh_base(self):
        """
        Method called to refresh the base frame of the CharDisplay

        :return: None
        """
        self.parent().refresh_base()

    def refresh_def(self):
        """
        Method called to refresh only the defense frame

        :return: None
        """
        self.BNDL.refresh_def()

    def refresh_eth(self):
        """
        Method called to refresh only the magic frame

        :return: None
        """
        self.BNDL.refresh_eth()

    def refresh_phy(self):
        """
        Method called to refresh only the physical frame

        :return: None
        """
        self.BNDL.refresh_phy()

    def refresh_soc(self):
        """
        Method called to refresh only the social frame

        :return: None
        """
        self.BNDL.refresh_soc()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()
