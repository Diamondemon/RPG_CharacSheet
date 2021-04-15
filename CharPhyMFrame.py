from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton)
import CCaF


class CharPhyMFrame(QWidget):
    """ Widget to modify the physical abilities of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setMaximumHeight(250)
        self.setMaximumWidth(400)
        self.baselist = ["training", "dexterity", "mobility"]
        self.thirdlist = ["phys-res"]

        self.grid.addWidget(QLabel(self.tr("Utiliser l'XP")), 0, 0, 1, 2)

        self.statlist = QComboBox()
        for key in ["Entrainement physique", "Dextérité/Habileté", "Mobilité"]:
            self.statlist.addItem(self.tr(key))
        self.statlist.setEditable(False)
        self.statlist.setCurrentIndex(0)
        self.add_stat = QLineEdit()
        self.add_stat.setText("0")
        self.Register_new = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_new, SIGNAL("clicked()"), self.register)

        self.grid.addWidget(QLabel(self.tr("Utiliser la force")), 3, 0, 1, 2)
        self.statthird = QComboBox()
        self.statthird.addItem(self.tr("Résistance Physique"))
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

        self.grid.addWidget(QLabel(self.tr("Convertir l'initiative en habileté")), 6, 0)
        self.convert = QPushButton(self.tr("Ajouter"))
        self.connect(self.convert, SIGNAL("clicked()"), self.launch_convert)
        self.grid.addWidget(self.convert, 7, 0)

    def register(self, event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist,
        et enregistre la nouvelle configuration du personnage"""
        self.get_selectedchar().upstats(self.baselist[self.statlist.current()], self.New_carac.get())
        self.New_carac.set(0)
        self.master.master.master.reload()
        self.master.BNDL.PHY.refresh()

    def register_third(self, event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist,
        et enregistre la nouvelle configuration du personnage"""
        self.get_selectedchar().upstats(self.thirdlist[self.statthird.current()], self.New_third.get())
        self.New_third.set(0)
        self.master.master.master.reload()
        self.master.BNDL.PHY.refresh()

    def launch_convert(self):
        self.master.master.master.selectedchar.convert_init(1)
        self.master.BNDL.PHY.refresh()
        self.master.BNDL.ABI.refresh()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the carac frame)

        :return: the reference to the parent
        """
        return QWidget.parent(self)
