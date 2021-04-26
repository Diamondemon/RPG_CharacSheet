from PySide6.QtCore import SIGNAL, Qt
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton, QFrame)
from functools import partial
import CCaF


class CharAbiMFrame(QWidget):
    """ Widget to modify the travelling abilities of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setMaximumHeight(500)
        self.setMaximumWidth(460)
        self.baselist = ["perception", "stealth", "reflex", "wit", "mental-res"]
        self.addlist = {}
        self.labels = {}
        self.perceplist = [["intention", "thing-info", "bestiary"], ["trap", "find", "tracking"],
                           ["ennemies", "threat", "curse"]]
        self.furtiflist = [["ground", "moving", "assassination"], ["shadow", "not-moving", "identity"],
                           ["smell", "disguise", "nature-field"]]
        self.point_labels = []
        for i in range(4):
            self.point_labels.append(QLabel(self.tr("Points restants : %n", "", 0)))

        self.grid.addWidget(QLabel(self.tr("Utiliser l'XP")), 0, 0, 1, 12)

        self.hide_button = QPushButton("×")
        self.hide_button.setCursor(Qt.PointingHandCursor)
        self.hide_button.setStyleSheet("QPushButton {background: white; color: red; border: none;"
                                       "font-weight: bold; font-size: 25px;}")
        self.connect(self.hide_button, SIGNAL("clicked()"), self.hide)
        self.grid.addWidget(self.hide_button, 0, 13)

        self.statlist = QComboBox()
        for key in ["Perception", "Furtivité", "Réflexes", "Intelligence", "Résistance mentale"]:
            self.statlist.addItem(self.tr(key))
        self.statlist.setEditable(False)
        self.statlist.setCurrentIndex(0)
        self.add_stat = QLineEdit()
        self.add_stat.setText("0")
        self.add_stat.setValidator(QIntValidator(0, 200, self))
        self.Register_new = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register_new, SIGNAL("clicked()"), self.register)

        self.grid.addWidget(self.statlist, 1, 0, 1, 6)
        self.grid.addWidget(self.add_stat, 1, 6, 1, 6)
        self.grid.addWidget(self.Register_new, 2, 0, 1, 12)

        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator, 3, 0, 1, 12)

        # sense
        self.grid.addWidget(QLabel(self.tr("Améliorer ses sens")), 4, 0, 1, 7)
        self.grid.addWidget(self.point_labels[0], 4, 7, 1, 5)

        i = 0
        for key in ["Vue : ", "Ouïe : ", "Odorat : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 5, 4*i, 1, 2)
            i += 1

        i = 0
        for stat in ["sight", "hearing", "smelling"]:
            self.addlist[stat] = QPushButton(self.tr("+"))
            self.addlist[stat].setDisabled(True)
            self.connect(self.addlist[stat], SIGNAL("clicked()"), partial(self.add_sense, stat))
            self.grid.addWidget(self.addlist[stat], 5, 3+4*i)
            self.labels[stat] = QLabel("0")
            self.grid.addWidget(self.labels[stat], 5, 2+4*i)
            i += 1

        separator1 = QFrame()
        separator1.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator1, 6, 0, 1, 12)

        # perception
        self.grid.addWidget(QLabel(self.tr("Perception")), 7, 0, 1, 7)
        self.grid.addWidget(self.point_labels[1], 7, 7, 1, 5)

        i = 0
        for key in ["Indice : ", "Terrain : ", "Embuscade : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 8, 4 * i, 1, 4)
            i += 1

        i = 9
        for key in ["Intention : ", "Objet-info : ", "Bestiaire : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 0, 1, 2)
            i += 1

        i = 9
        for key in ["Piège : ", "Trouver Objets : ", "Pistage : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 4, 1, 2)
            i += 1

        i = 9
        for key in ["Adversaires : ", "Menace : ", "Malédiction : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 8, 1, 2)
            i += 1

        for j in range(3):
            i = 9
            for stat in self.perceplist[j]:
                self.addlist[stat] = QPushButton(self.tr("+"))
                self.addlist[stat].setDisabled(True)
                self.connect(self.addlist[stat], SIGNAL("clicked()"), partial(self.invest_furtif, stat))
                self.grid.addWidget(self.addlist[stat], i, 4 * j + 3)
                self.labels[stat] = QLabel("0")
                self.grid.addWidget(self.labels[stat], i, 4*j+2)
                i += 1

        separator2 = QFrame()
        separator2.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator2, 12, 0, 1, 12)

        # stealth
        self.grid.addWidget(QLabel(self.tr("Furtivité")), 13, 0, 1, 7)
        self.grid.addWidget(self.point_labels[2], 13, 7, 1, 5)

        i = 0
        for key in ["Silence : ", "Dissimulation : ", "Camouflage : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 14, 4 * i, 1, 4)
            i += 1

        i = 15
        for key in ["Sol : ", "Déplacement : ", "Assassinat : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 0, 1, 2)
            i += 1

        i = 15
        for key in ["Ombre : ", "Immobilité : ", "Identité : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 4, 1, 2)
            i += 1

        i = 15
        for key in ["Odeur : ", "Déguisement : ", "Nature/Terrain : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 8, 1, 2)
            i += 1

        for j in range(3):
            i = 15
            for stat in self.furtiflist[j]:
                self.addlist[stat] = QPushButton(self.tr("+"))
                self.addlist[stat].setDisabled(True)
                self.connect(self.addlist[stat], SIGNAL("clicked()"), partial(self.invest_furtif, stat))
                self.grid.addWidget(self.addlist[stat], i, 4 * j + 3)
                self.labels[stat] = QLabel("0")
                self.grid.addWidget(self.labels[stat], i, 4*j+2)
                i += 1

        separator3 = QFrame()
        separator3.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator3, 18, 0, 1, 12)

        # action dissimulée
        self.grid.addWidget(QLabel(self.tr("Action dissimulée")), 19, 0, 1, 7)
        self.grid.addWidget(self.point_labels[3], 19, 7, 1, 5)

        i = 0
        for key in ["Vol à la tire : ", "Embuscade : ", "Fuite : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 20, 4 * i, 1, 2)
            i += 1

        j = 0
        for stat in ["thievery", "ambush", "escape"]:
            self.addlist[stat] = QPushButton(self.tr("+"))
            self.addlist[stat].setDisabled(True)
            self.connect(self.addlist[stat], SIGNAL("clicked()"), partial(self.invest_furtif, stat))
            self.grid.addWidget(self.addlist[stat], 20, 4 * j + 3, 1, 1)
            self.labels[stat] = QLabel("0")
            self.grid.addWidget(self.labels[stat], 20, 4*j+2)
            j += 1

    def add_sense(self, stat):
        """
        Method called to add points to the senses of the character

        :param stat: sense to invest points into
        :return: None
        """
        self.get_selectedchar().upstats(stat, 1)
        self.save_character()
        self.refresh()
        self.parent().refresh_abi()

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.Player)
        """
        return self.parent().get_selectedchar()

    def invest_furtif(self, stat):
        """
        Method called to consume stealth points

        :param stat: the target stat to put the points into
        :return: None
        """
        self.get_selectedchar().upstats(stat, 1)
        self.save_character()
        self.refresh()
        self.parent().refresh_abi()

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the carac frame)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def refresh(self):
        """
        Method called to refresh all the statistics and numbers displayed on screen

        :return: None
        """

        selectedchar = self.get_selectedchar()
        secondstats = selectedchar.get_secondstats()
        thirdstats = selectedchar.get_thirdstats()

        self.point_labels[0].setText(self.tr("Points restants : %n", "", secondstats["symb-S"]))
        self.point_labels[1].setText(self.tr("Points restants : %n", "", secondstats["symb-perception"]))
        self.point_labels[2].setText(self.tr("Points restants : %n", "", secondstats["symb-T"] +
                                             secondstats["symb-stealth"][0] + secondstats["symb-stealth"][1]))
        self.point_labels[3].setText(self.tr("Points restants : %n", "", secondstats["symb-ability"][0] +
                                             secondstats["symb-ps_T"][0] + secondstats["symb-T"]))

        # senses
        if secondstats["symb-S"]:
            for key in ["sight", "hearing", "smelling"]:
                self.addlist[key].setDisabled(False)
        else:
            for key in ["sight", "hearing", "smelling"]:
                self.addlist[key].setDisabled(True)

        i = 0
        for key in ["sight", "hearing", "smelling"]:
            self.labels[key].setText(str(thirdstats[key]))
            i += 1

        # stealth
        if secondstats["symb-T"] + secondstats["symb-stealth"][0] + secondstats["symb-stealth"][1]:
            for i in range(3):
                for key in self.furtiflist[i]:
                    self.addlist[key].setDisabled(False)
        else:
            for i in range(3):
                for key in self.furtiflist[i]:
                    self.addlist[key].setDisabled(True)

        j = 0
        for key in ["silence", "hiding", "camo"]:
            i = 1
            for stat in self.furtiflist[j]:
                self.labels[stat].setText(str(thirdstats[key][stat]))
                i += 1
            j += 1

        # perception
        if secondstats["symb-perception"]:
            for j in range(3):
                for key in self.perceplist[j]:
                    self.addlist[key].setDisabled(False)
        else:
            for j in range(3):
                for key in self.perceplist[j]:
                    self.addlist[key].setDisabled(True)

        j = 0
        for key in ["clue", "field", "ambush"]:
            i = 4
            for stat in self.perceplist[j]:
                self.labels[stat].setText(str(thirdstats[key][stat]))
                i += 1
            j += 1

        # action dissimulée
        if secondstats["symb-ability"][0] + secondstats["symb-ps_T"][0] + secondstats["symb-T"]:
            for key in ["thievery", "ambush", "escape"]:
                self.addlist[key].setDisabled(False)
        else:
            for key in ["thievery", "ambush", "escape"]:
                self.addlist[key].setDisabled(True)

        j = 0
        for stat in ["thievery", "ambush", "escape"]:
            self.labels[stat].setText(str(thirdstats["hidden_action"][stat]))
            j += 1

    def register(self):
        """
        Method that turns experience points into the selected caracteristic and registers the new stats

        :return: None
        """
        self.get_selectedchar().upstats(self.baselist[self.statlist.currentIndex()], int(self.add_stat.text()))
        self.parent().refresh_abi()
        self.parent().refresh_base()
        self.save_character()
        self.refresh()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()
