from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton)


class CharAtkMFrame(QWidget):
    """ Widget de modification des caractéristiques d'attaque du personnage"""

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.grid = QGridLayout(self)

        self.baselist = ["hands", "light", "medium", "heavy", "throw", "shield"]

        self.grid.addWidget(QLabel(self.tr("Utiliser l'XP")), 0, 0)

        self.statlist = QComboBox()
        self.statlist.addItems(["Mains nues", "Armes légères", "Armes moyennes", "Armes lourdes",
                               "Armes de jet", "Bouclier"])
        self.statlist.setEditable(False)
        self.statlist.setCurrentIndex(0)
        self.add_stat = QLineEdit()
        self.add_stat.setText("0")
        self.Register_new = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_new, SIGNAL("clicked()"), self.register)

        self.grid.addWidget(self.statlist, 1, 0)
        self.grid.addWidget(self.add_stat, 1, 1)
        self.grid.addWidget(self.Register_new, 2, 0, 1, 2)

    def register(self, event=None):
        """ Transforme l'expérience en points de la caractéristique sélectionnée avec statlist,
        et enregistre la nouvelle configuration du personnage"""
        self.get_selectedchar().upstats(self.baselist[self.statlist.current()], int(self.add_stat.text()))
        self.add_stat.setText("0")
        self.parent().parent().parent().reload()
        self.parent().BNDL.ATK.refresh()
        # with open("characters","wb") as fichier:
        #     pk.Pickler(fichier).dump(self.master.master.master.master.characlist)

    def get_selectedchar(self):
        return self.parent().get_selectedchar()
