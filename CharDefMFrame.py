from PySide6.QtCore import SIGNAL
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton)
import CCaF


class CharDefMFrame(QWidget):
    """ Widget to modify the defensive abilities of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setMaximumHeight(200)
        self.setMaximumWidth(300)
        self.baselist = ["armor"]
        self.thirdlist = ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette",
                          "Cuissots", "Grèves", "Solerets"]

        self.grid.addWidget(QLabel(self.tr("Utiliser l'XP")), 0, 0, 1, 2)
        self.grid.addWidget(QLabel(self.tr("Utiliser l'Armure")), 3, 0, 1, 2)

        self.statlist = QComboBox()
        self.statlist.addItem(self.tr("Armure"))
        self.statlist.setEditable(False)
        self.statlist.setCurrentIndex(0)
        self.add_stat = QLineEdit()
        self.add_stat.setText("0")
        self.add_stat.setValidator(QIntValidator(0, 200, self))
        self.Register_new = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_new, SIGNAL("clicked()"), self.register)

        self.statthird = QComboBox()
        for key in self.thirdlist:
            self.statthird.addItem(self.tr(key))
        self.statthird.setEditable(False)
        self.statthird.setCurrentIndex(0)

        self.add_third = QLineEdit()
        self.add_third.setText("0")
        self.add_third.setValidator(QIntValidator(0, 10, self))
        self.Register_third = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_third, SIGNAL("clicked()"), self.register_third)

        self.grid.addWidget(self.statlist, 1, 0)
        self.grid.addWidget(self.add_stat, 1, 1)
        self.grid.addWidget(self.Register_new, 2, 0, 1, 2)

        self.grid.addWidget(self.statthird, 4, 0)
        self.grid.addWidget(self.add_third, 4, 1)
        self.grid.addWidget(self.Register_third, 5, 0, 1, 2)

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the carac frame)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def register(self):
        """
        Method that turns experience points into the selected caracteristic and registers the new stats

        :return: None
        """
        self.get_selectedchar().upstats(self.baselist[self.statlist.currentIndex()], int(self.add_stat.text()))
        self.save_character()
        self.parent().refresh_def()
        self.parent().refresh_base()

    def register_third(self):
        """
        Consumes an armor symbol to give it to a piece of equipment

        :return: None
        """
        self.get_selectedchar().upstats("invested_armor", int(self.add_third.text()),
                                        self.thirdlist[self.statthird.currentIndex()])
        self.save_character()
        self.parent().refresh_def()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()
