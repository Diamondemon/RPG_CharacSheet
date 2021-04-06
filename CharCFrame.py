from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QCheckBox, QGridLayout, QPushButton)
from PySide6.QtGui import QIntValidator


class CharCFrame(QWidget):
    """ Widget to create a new character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.Name_lab = QLabel(self.tr("Nom du personnage"))
        self.xp_lab = QLabel(self.tr("Expérience de base"))
        self.Name_input = QLineEdit()
        self.xp_input = QLineEdit()
        self.xp_input.setValidator(QIntValidator(0, 9999, self))
        self.mage_input = QCheckBox(self.tr("Ce personnage est un mage"))
        self.Char_Gen = QPushButton(self.tr("Créer le personnage"))

        self.grid.addWidget(self.Name_lab, 0, 0)
        self.grid.addWidget(self.xp_lab, 1, 0)
        self.grid.addWidget(self.Name_input, 0, 1)
        self.grid.addWidget(self.xp_input, 1, 1)
        self.grid.addWidget(self.mage_input, 2, 1)
        self.grid.addWidget(self.Char_Gen, 3, 0, 1, 2)

        self.connect(self.Char_Gen, SIGNAL("clicked()"), self.generate)

    @Slot()
    def generate(self):
        """ Method called to create the new character """
        # Call the method of the mainwindow
        self.parent().generate(self.Name_input.text(), self.xp_input.text(), self.mage_input.isChecked())
