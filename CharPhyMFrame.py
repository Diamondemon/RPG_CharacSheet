from PySide6.QtCore import SIGNAL, Qt
from PySide6.QtGui import QIntValidator
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

        self.hide_button = QPushButton("×")
        self.hide_button.setCursor(Qt.PointingHandCursor)
        self.hide_button.setStyleSheet("QPushButton {background: white; color: red; border: none;"
                                       "font-weight: bold; font-size: 25px;}")
        self.connect(self.hide_button, SIGNAL("clicked()"), self.hide)
        self.grid.addWidget(self.hide_button, 0, 2)

        self.statlist = QComboBox()
        for key in ["Entrainement physique", "Dextérité/Habileté", "Mobilité"]:
            self.statlist.addItem(self.tr(key))
        self.statlist.setEditable(False)
        self.statlist.setCurrentIndex(0)
        self.add_stat = QLineEdit()
        self.add_stat.setText("0")
        self.add_stat.setValidator(QIntValidator(0, 200, self))
        self.Register_new = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_new, SIGNAL("clicked()"), self.register)

        self.grid.addWidget(QLabel(self.tr("Utiliser la force")), 3, 0, 1, 2)
        self.statthird = QComboBox()
        self.statthird.addItem(self.tr("Résistance Physique"))
        self.statthird.setEditable(False)
        self.statthird.setCurrentIndex(0)
        self.add_third = QLineEdit()
        self.add_third.setText("0")
        self.add_third.setValidator(QIntValidator(0, 50, self))
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

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.Player)
        """
        return self.parent().get_selectedchar()

    def launch_convert(self):
        """
        Method called to convert ability points into initiative

        :return: None
        """
        self.get_selectedchar().convert_init(1)
        self.save_character()
        self.parent().refresh_phy()
        self.parent().refresh_abi()

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
        self.parent().refresh_phy()
        self.parent().refresh_base()

    def register_third(self):
        """
        Method called to consume strength and enhance physical resistance

        :return: None
        """
        self.get_selectedchar().upstats(self.thirdlist[self.statthird.currentIndex()], int(self.add_third.text()))
        self.save_character()
        self.parent().refresh_phy()
        self.parent().refresh_base()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()
