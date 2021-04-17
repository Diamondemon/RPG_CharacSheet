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
        """
        Method called when the Game Master wants to give points into specific stats

        :return: None
        """
        self.selectedchar.GM_gain(self.baseFrame.get_gmwheel_text(), self.baseFrame.get_new_gm())
        self.baseFrame.refresh(self.selectedchar)
        self.parent().save_characlist()

    @Slot()
    def add_xp(self):
        """
        Method called to give experience points to the character

        :return: None
        """
        self.selectedchar.upxp(self.baseFrame.get_new_xp())
        self.baseFrame.refresh(self.selectedchar)
        self.save_character()

    def get_selectedchar(self):
        """
        Method called to get the character to be displayed

        :return: the reference to the character
        """
        return self.selectedchar

    def GM_reinit_char(self):
        """
        Method called to reset all the stats given to the character by the Game Master in specific stats.

        :return: None
        """
        self.selectedchar.GM_clearstats()
        self.save_character()
        self.baseFrame.refresh(self.selectedchar)
        self.NBK.refresh()

    def legal_onMove(self, value: int):
        """
        Method called when the value of the legal stat is changed through the QSlider

        :param value: new value to register
        :return: None
        """
        self.selectedchar.change_passive("legal", value)
        self.save_character()
        self.baseFrame.set_legal_display(value)

    def parent(self) -> MW.UIWindow:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def refresh(self):
        """
        Method called to refresh all the widgets displaying the stats of the character

        :return: None
        """

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
        """
        Method called to reset all the statistics of the displayed character

        :return: None
        """
        self.selectedchar.clearstats()
        self.save_character()
        self.baseFrame.refresh(self.selectedchar)
        self.NBK.refresh()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_characlist()

    def set_selectedchar(self, character: Pc.player):
        """
        Method called to select the character to load and edit

        :param character: character to load
        :return: None
        """
        self.selectedchar = character
