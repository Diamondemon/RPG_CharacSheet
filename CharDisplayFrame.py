from PySide6.QtCore import SIGNAL, Slot
from PySide6.QtWidgets import (QWidget, QGridLayout, QPushButton)
import Perso_class as Pc
from CharNotebook import CharNotebook
from CharBaseFrame import CharBaseFrame
import MW


class CharDisplayFrame(QWidget):
    """Affichage des statistiques d'un personnage"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)

        self.selectedchar: Pc.player = None
        self.selected = ""  # Partie des caractéristiques sélectionnée

        self.baseFrame = CharBaseFrame()

        self.connect(self.baseFrame.get_plus_xp(), SIGNAL("clicked()"), self.add_xp)
        self.connect(self.baseFrame.get_plus_gm(), SIGNAL("clicked()"), self.add_GM)
        self.connect(self.baseFrame.get_slider(), SIGNAL("valueChanged(int)"), self.legal_onMove)

        self.grid.addWidget(self.baseFrame, 0, 0, 1, 1)

        self.restat_choice = QPushButton(self.tr("Restat"))
        self.connect(self.restat_choice, SIGNAL("clicked()"), self.reinit_char)
        self.grid.addWidget(self.restat_choice, 1, 0)

        self.GM_restat_choice = QPushButton(self.tr("Restat MJ"))
        self.connect(self.GM_restat_choice, SIGNAL("clicked()"), self.GM_reinit_char)
        self.grid.addWidget(self.GM_restat_choice, 2, 0)

        self.NBK = CharNotebook(self)
        self.grid.addWidget(self.NBK, 0, 1, 3, 1)

    @Slot()
    def add_GM(self):
        self.selectedchar.GM_gain(self.baseFrame.get_gmwheel_text(), self.baseFrame.get_new_gm())
        self.baseFrame.refresh(self.selectedchar)
        self.parent().save_characlist()

    @Slot()
    def add_xp(self):
        self.selectedchar.upxp(self.baseFrame.get_new_xp())
        self.baseFrame.refresh(self.selectedchar)
        self.parent().save_characlist()

    def get_selectedchar(self):
        return self.selectedchar

    def GM_reinit_char(self):
        self.selectedchar.GM_clearstats()
        self.parent().save_characlist()
        self.NBK.refresh()

    def legal_onMove(self, value: int):
        self.selectedchar.change_passive("legal", value)
        self.parent().save_characlist()
        self.baseFrame.set_legal_display(value)

    def parent(self) -> MW.UIWindow:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def refresh(self):

        if self.selectedchar:
            self.baseFrame.refresh(self.selectedchar)
            self.NBK.refresh()
            """self.legal_scale.set(self.selectedchar.passivestats["legal"][0])
            self.legal_scale.grid(row=10, column=0, columnspan=2)
            self.NBK.CharCF.BNDL.SYM.refresh()"""

    def refresh_base(self):
        """
        Method called to refresh only the base frame

        :return: None
        """
        self.baseFrame.refresh(self.selectedchar)

    def reinit_char(self):
        self.selectedchar.clearstats()
        self.parent().save_characlist()
        # self.NBK.refresh()

    def set_selectedchar(self, character: Pc.player):
        self.selectedchar = character
