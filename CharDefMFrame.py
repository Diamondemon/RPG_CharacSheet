from PySide6.QtCore import SIGNAL
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

        self.grid.addWidget(QLabel(self.tr("Utiliser l'XP")), 0, 0, 1, 2)
        self.grid.addWidget(QLabel(self.tr("Utiliser l'Armure")), 3, 0, 1, 2)

        self.statlist = QComboBox()
        self.statlist.addItem(self.tr("Armure"))
        self.statlist.setEditable(False)
        self.statlist.setCurrentIndex(0)
        self.add_stat = QLineEdit()
        self.add_stat.setText("0")
        self.Register_new = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_new, SIGNAL("clicked()"), self.register)

        self.statthird = QComboBox()
        for key in ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette",
                    "Cuissots", "Grèves", "Solerets"]:
            self.statthird.addItem(self.tr(key))
        self.statthird.setEditable(False)
        self.statthird.setCurrentIndex(0)

        self.add_third = QLineEdit()
        self.add_third.setText("0")
        self.Register_third = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_third, SIGNAL("clicked()"), self.register_third)

        self.grid.addWidget(self.statlist, 1, 0)
        self.grid.addWidget(self.add_stat, 1, 1)
        self.grid.addWidget(self.Register_new, 2, 0, 1, 2)

        self.grid.addWidget(self.statthird, 4, 0)
        self.grid.addWidget(self.add_third, 4, 1)
        self.grid.addWidget(self.Register_third, 5, 0, 1, 2)

    def register(self, event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist,
        et enregistre la nouvelle configuration du personnage"""
        self.get_selectedchar().upstats(self.baselist[self.statlist.current()], self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.DEF.refresh()

    def register_third(self, event=None):
        """ Consomme un symbole d'armure pour l'assigner à une pièce d'équipement """
        self.get_selectedchar().upstats("invested_armor", self.New_third.get(), self.statthird.get())
        self.New_third.set(0)
        self.master.BNDL.DEF.refresh()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the carac frame)

        :return: the reference to the parent
        """
        return QWidget.parent(self)
