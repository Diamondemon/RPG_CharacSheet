from PySide6.QtCore import SIGNAL
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton)
import CCaF


class CharAtkMFrame(QWidget):
    """ Widget to modify the offensive abilities of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setMaximumHeight(150)
        self.setMaximumWidth(300)
        self.baselist = ["hands", "light", "medium", "heavy", "throw", "shield"]

        self.grid.addWidget(QLabel(self.tr("Utiliser l'XP")), 0, 0)

        self.statlist = QComboBox()
        for key in ["Mains nues", "Armes légères", "Armes moyennes", "Armes lourdes", "Armes de jet", "Bouclier"]:
            self.statlist.addItem(self.tr(key))
        self.statlist.setEditable(False)
        self.statlist.setCurrentIndex(0)
        self.add_stat = QLineEdit()
        self.add_stat.setText("0")
        self.add_stat.setValidator(QIntValidator(0, 200, self))
        self.Register_new = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_new, SIGNAL("clicked()"), self.register)

        self.grid.addWidget(self.statlist, 1, 0)
        self.grid.addWidget(self.add_stat, 1, 1)
        self.grid.addWidget(self.Register_new, 2, 0, 1, 2)

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
        self.parent().refresh_atk()
        self.parent().refresh_base()
