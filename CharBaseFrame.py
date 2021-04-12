from PySide6.QtCore import Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QSlider, QPushButton
import Perso_class as Pc


class CharBaseFrame(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.setMaximumWidth(250)
        self.setMaximumHeight(500)
        
        self.grid.addWidget(QLabel(self.tr("Personnage")), 0, 0)
        self.grid.addWidget(QLabel(self.tr("Xp totale")), 1, 0)
        self.grid.addWidget(QLabel(self.tr("Xp restante")), 2, 0)
        self.grid.addWidget(QLabel(self.tr("Force")), 3, 0)
        self.grid.addWidget(QLabel(self.tr("Gagner de l'xp")), 4, 0)

        self.nameLabel = QLabel()
        self.totalXpLabel = QLabel()
        self.xpLabel = QLabel()
        self.strengthLabel = QLabel()
        self.grid.addWidget(self.nameLabel, 0, 1)
        self.grid.addWidget(self.totalXpLabel, 1, 1)
        self.grid.addWidget(self.xpLabel, 2, 1)
        self.grid.addWidget(self.strengthLabel, 3, 1)

        self.New_xp = QLineEdit()
        self.New_xp.setText("0")
        self.New_xp.setValidator(QIntValidator(0, 9999, self))
        self.grid.addWidget(self.New_xp, 5, 0)

        self.plus_xp = QPushButton(self.tr("+"))
        self.grid.addWidget(self.plus_xp, 5, 1)
        
        self.grid.addWidget(QLabel(self.tr("Gain MJ")), 6, 0)
        self.GM_wheel = QComboBox()
        self.GM_wheel.setEditable(False)
        self.grid.addWidget(self.GM_wheel, 7, 0, 1, 2)
        
        self.New_GM = QLineEdit()
        self.New_GM.setText("0")
        self.New_GM.setValidator(QIntValidator(0, 9999, self))
        self.grid.addWidget(self.New_GM, 8, 0)

        self.plus_GM = QPushButton(self.tr("+"))
        self.grid.addWidget(self.plus_GM, 8, 1)

        self.grid.addWidget(QLabel(self.tr("Légal")), 9, 0)
        self.legal_scale = QSlider(Qt.Horizontal)
        self.legal_scale.setRange(-50, 50)
        self.legal_scale.setSingleStep(25)
        self.legal_scale.setValue(0)
        self.legal_scale.setTracking(True)
        self.grid.addWidget(self.legal_scale, 10, 0, 1, 2)

    def get_gmwheel_text(self):
        """
        Method called to get the statistic to boost with GM experience

        :return: statistic to boost
        """
        return self.GM_wheel.currentText()

    def get_new_gm(self):
        """
        Method called to get the GM experience number to give the character

        :return: GM experience
        """
        return int(self.New_GM.text())

    def get_new_xp(self):
        """
        Method called to get the experience number to give the character

        :return: experience to add
        """
        return int(self.New_xp.text())

    def get_plus_gm(self):
        """
        Method called to get the reference to the game-master button

        :return: reference to the button
        """
        return self.plus_GM

    def get_plus_xp(self):
        """
        Method called to get the reference to the experience button

        :return: reference to the button
        """
        return self.plus_xp
    
    def refresh(self, selectedchar: Pc.player):
        """
        Method called to refresh the name and basic characteristics of the character
        
        :return: None
        """

        self.nameLabel.setText(selectedchar.get_name())
        self.totalXpLabel.setText(str(selectedchar.totalxp))
        self.xpLabel.setText(str(selectedchar.xp))
        self.strengthLabel.setText(str(selectedchar.secondstats["symb-strength"][0]) + "/" + str(
            selectedchar.secondstats["symb-strength"][1]) + " (" + str(
            selectedchar.secondstats["symb-strength"][2]) + ")")

        self.GM_wheel.clear()
        self.GM_wheel.addItems(list(selectedchar.GMstats.keys()))
        self.GM_wheel.setCurrentIndex(0)

        self.legal_scale.setValue(selectedchar.passivestats["legal"][0])
