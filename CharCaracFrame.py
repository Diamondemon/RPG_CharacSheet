from PySide6.QtWidgets import (QWidget, QGridLayout)
from CharAtkMFrame import CharAtkMFrame
from CharBundleFrame import CharBundleFrame
import CNbk


class CharCaracFrame(QWidget):
    """Affichage des statistiques d'un personnage"""

    def __init__(self, parent):
        QWidget.__init__(self, parent=parent)
        self.grid = QGridLayout(self)
        self.parent1 = parent
        self.BNDL = CharBundleFrame()
        self.grid.addWidget(self.BNDL, 0, 0)
        self.MATK = CharAtkMFrame()
        print(self.parent1)

        """self.MDEF = CharDefMFrame(self)

        self.MPHY = CharPhyMFrame(self)

        self.MABI = CharAbiMFrame(self)

        self.MSOC = CharSocMFrame(self)

        self.METH = CharEthMFrame(self)"""

    def refresh(self):
        self.BNDL.refresh()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CNbk.CharNotebook:
        return
