from PySide6.QtWidgets import (QWidget, QGridLayout)
from CharAtkFrame import CharAtkFrame
from CharDefFrame import CharDefFrame
from CharPhyFrame import CharPhyFrame
from CharAbiFrame import CharAbiFrame
from CharSocFrame import CharSocFrame
from CharEthFrame import CharEthFrame
from CharSymbFrame import CharSymbFrame
import CCaF


class CharBundleFrame(QWidget):
    """ Widget to display all the caracteristics of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)

        self.ATK = CharAtkFrame()
        self.grid.addWidget(self.ATK, 0, 0, 2, 1)
        self.DEF = CharDefFrame()
        self.grid.addWidget(self.DEF, 0, 1)
        self.PHY = CharPhyFrame()
        self.grid.addWidget(self.PHY, 1, 1)
        self.ABI = CharAbiFrame()
        self.grid.addWidget(self.ABI, 2, 0, 2, 1)
        self.SOC = CharSocFrame()
        self.grid.addWidget(self.SOC, 2, 1)
        self.ETH = CharEthFrame()
        self.grid.addWidget(self.ETH, 3, 1)
        self.ETH.hide()
        self.SYM = CharSymbFrame()
        self.grid.addWidget(self.SYM, 0, 2, 4, 1)

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
        self.parent().modify_abi()

    def modify_atk(self):
        """
        Method called to modify the offensive statistics of the character

        :return: None
        """
        self.parent().modify_atk()

    def modify_def(self):
        """
        Method called to modify the defensive statistics of the character

        :return: None
        """
        self.parent().modify_def()

    def modify_eth(self):
        """
        Method called to modify the magical statistics of the character

        :return: None
        """
        self.parent().modify_eth()

    def modify_phy(self):
        """
        Method called to modify the physical statistics of the character

        :return: None
        """
        self.parent().modify_phy()

    def modify_soc(self):
        """
        Method called to modify the social statistics of the character

        :return: None
        """
        self.parent().modify_soc()

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the carac frame)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def refresh(self):
        """
        Method called to refresh all the information displayed on the subframes

        :return: None
        """
        self.ABI.refresh()
        self.ATK.refresh()
        self.DEF.refresh()
        self.PHY.refresh()
        self.SOC.refresh()
        if self.get_selectedchar().ismage():
            self.ETH.show()
            self.ETH.refresh()
        else:
            self.ETH.hide()
        self.SYM.refresh()

    def refresh_abi(self):
        """
        Method called to refresh only the ability frame

        :return: None
        """
        self.ABI.refresh()
        self.SYM.refresh()

    def refresh_atk(self):
        """
        Method called to refresh only the attack frame

        :return: None
        """
        self.ATK.refresh()
        self.SYM.refresh()

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
        self.DEF.refresh()
        self.SYM.refresh()

    def refresh_eth(self):
        """
        Method called to refresh only the magic frame

        :return: None
        """
        self.ETH.refresh()
        self.SYM.refresh()

    def refresh_phy(self):
        """
        Method called to refresh only the physical frame

        :return: None
        """
        self.PHY.refresh()
        self.SYM.refresh()

    def refresh_soc(self):
        """
        Method called to refresh only the social frame

        :return: None
        """
        self.SOC.refresh()
        self.SYM.refresh()
