from PySide6.QtCore import SIGNAL
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QComboBox, QPushButton, QFrame)
from functools import partial
import CCaF
import numpy as np


class CharAbiMFrame(QWidget):
    """ Widget to modify the travelling abilities of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setMaximumHeight(500)
        self.setMaximumWidth(350)
        self.baselist = ["perception", "stealth", "reflex", "wit", "mental-res"]
        self.addlist = {}
        self.perceplist = [["intention", "thing-info", "bestiary"], ["trap", "find", "tracking"],
                           ["ennemies", "threat", "curse"]]
        self.furtiflist = [["ground", "moving", "assassination"], ["shadow", "not-moving", "identity"],
                           ["smell", "disguise", "nature-field"]]
        self.labels = np.zeros((8, 3), dtype=QLabel)
        for i in range(8):
            for j in range(3):
                self.labels[i, j] = QLabel("0")

        self.grid.addWidget(QLabel(self.tr("Utiliser l'XP")), 0, 0, 1, 12)

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

        separator = QFrame(self)
        separator.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator, 3, 0, 1, 12)

        # sense
        self.grid.addWidget(QLabel(self.tr("Améliorer ses sens")), 4, 0, 1, 12)

        i = 5
        for key in ["Vue : ", "Ouïe : ", "Odorat : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 0, 1, 3)
            i += 1

        self.add_sight = QPushButton(self.tr("+"))
        self.add_sight.setDisabled(True)
        self.connect(self.add_sight, SIGNAL("clicked()"), partial(self.add_sense, "sight"))
        self.add_hearing = QPushButton(self.tr("+"))
        self.add_hearing.setDisabled(True)
        self.connect(self.add_hearing, SIGNAL("clicked()"), partial(self.add_sense, "hearing"))
        self.add_smell = QPushButton(self.tr("+"))
        self.add_smell.setDisabled(True)
        self.connect(self.add_smell, SIGNAL("clicked()"), partial(self.add_sense, "smell"))

        self.grid.addWidget(self.add_sight, 5, 3, 1, 1)
        self.grid.addWidget(self.add_hearing, 6, 3, 1, 1)
        self.grid.addWidget(self.add_smell, 7, 3, 1, 1)

        separator1 = QFrame(self)
        separator1.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator1, 8, 0, 1, 12)

        # perception
        self.grid.addWidget(QLabel(self.tr("Perception")), 9, 0, 1, 12)

        i = 0
        for key in ["Indice : ", "Terrain : ", "Embuscade : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 10, 4 * i, 1, 4)
            i += 1

        i = 11
        for key in ["Intention : ", "Objet-info : ", "Bestiaire : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 0, 1, 3)
            i += 1

        i = 11
        for key in ["Piège : ", "Trouver Objets : ", "Pistage : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 4, 1, 3)
            i += 1

        i = 11
        for key in ["Adversaires : ", "Menace : ", "Malédiction : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 8, 1, 3)
            i += 1

        for j in range(3):
            i = 11
            for stat in self.perceplist[j]:
                self.addlist[stat] = QPushButton(self.tr("+"))
                self.addlist[stat].setDisabled(True)
                self.connect(self.addlist[stat], SIGNAL("clicked()"), partial(self.invest_furtif, stat))
                self.grid.addWidget(self.addlist[stat], i, 4 * j + 3, 1, 1)
                i += 1

        separator2 = QFrame(self)
        separator2.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator2, 14, 0, 1, 12)

        # stealth
        self.grid.addWidget(QLabel(self.tr("Furtivité")), 15, 0, 1, 12)

        i = 0
        for key in ["Silence : ", "Dissimulation : ", "Camouflage : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 16, 4 * i, 1, 4)
            i += 1

        i = 17
        for key in ["Sol : ", "Déplacement : ", "Assassinat : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 0, 1, 3)
            i += 1

        i = 17
        for key in ["Ombre : ", "Immobilité : ", "Identité : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 4, 1, 3)
            i += 1

        i = 17
        for key in ["Odeur : ", "Déguisement : ", "Nature/Terrain : "]:
            self.grid.addWidget(QLabel(self.tr(key)), i, 8, 1, 3)
            i += 1

        for j in range(3):
            i = 17
            for stat in self.furtiflist[j]:
                self.addlist[stat] = QPushButton(self.tr("+"))
                self.addlist[stat].setDisabled(True)
                self.connect(self.addlist[stat], SIGNAL("clicked()"), partial(self.invest_furtif, stat))
                self.grid.addWidget(self.addlist[stat], i, 4 * j + 3, 1, 1)
                i += 1

        separator3 = QFrame(self)
        separator3.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator3, 20, 0, 1, 12)

        # action dissimulée
        self.grid.addWidget(QLabel(self.tr("Action dissimulée")), 21, 0, 1, 12)

        i = 0
        for key in ["Vol à la tire : ", "Embuscade : ", "Fuite : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 22, 4 * i, 1, 4)
            i += 1

        j = 0
        for stat in ["thievery", "ambush", "escape"]:
            self.addlist[stat] = QPushButton(self.tr("+"))
            self.addlist[stat].setDisabled(True)
            self.connect(self.addlist[stat], SIGNAL("clicked()"), partial(self.invest_furtif, stat))
            self.grid.addWidget(self.addlist[stat], 22, 4 * j + 3, 1, 1)
            j += 1

    def add_sense(self, stat):
        """
        Method called to add points to the senses of the character

        :param stat: sense to invest points into
        :return: None
        """
        self.get_selectedchar().upstats(stat, 1)
        self.refresh()
        self.parent().refresh_abi()

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def invest_furtif(self, stat):
        """
        Method called to consume stealth points

        :param stat: the target stat to put the points into
        :return: None
        """
        self.get_selectedchar().upstats(stat, 1)
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
        ""Fonction qui rafraichit toutes les zones de tier 3 ""
        for i in self.senseFrame.grid_slaves():
            info=i.grid_info()
            if info["row"]>=1 and info["column"]==1:
                i.destroy()
            elif info["row"]==0 and info["column"]==3:
                i.destroy()

        for i in self.stealthFrame.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,7]:
                i.destroy()
            elif info["row"]==0 and info["column"]==9:
                i.destroy()

        for i in self.percepFrame.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,7]:
                i.destroy()
            elif info["row"]==0 and info["column"]==9:
                i.destroy()

        # sens
        if self.master.master.master.selectedchar.secondstats["symb-S"]:
            Label(self.senseFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-S"])).grid(row=0,column=3,sticky="w")
            self.add_sight["state"]="normal"
            self.add_hearing["state"]="normal"
            self.add_smell["state"]="normal"
        else:
            self.add_sight["state"]="disabled"
            self.add_hearing["state"]="disabled"
            self.add_smell["state"]="disabled"

        i=1
        for key in ["sight","hearing","smell"]:
            Label(self.senseFrame,text=self.master.master.master.selectedchar.thirdstats[key]).grid(row=i,column=1)
            i+=1

        # furtivité
        if self.master.master.master.selectedchar.secondstats["symb-T"]+self.master.master.master.selectedchar.secondstats["symb-stealth"][0]+self.master.master.master.selectedchar.secondstats["symb-stealth"][1]:
            Label(self.stealthFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-T"]+self.master.master.master.selectedchar.secondstats["symb-stealth"][0]+self.master.master.master.selectedchar.secondstats["symb-stealth"][1])).grid(row=0,column=9,sticky="w")
            for j in range(3):
                for key in self.furtiflist[j]:
                    self.addlist[key]["state"]="normal"
        else:
            for j in range(3):
                for key in self.furtiflist[j]:
                    self.addlist[key]["state"]="disabled"

        j=0
        for key in ["silence","hiding","camo"]:
            i=2
            for stat in self.furtiflist[j]:
                Label(self.stealthFrame,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=3*j+1)
                i+=1

            j+=1

        # perception
        if self.master.master.master.selectedchar.secondstats["symb-perception"]:
            Label(self.percepFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-perception"])).grid(row=0,column=9,sticky="w")
            for j in range(3):
                for key in self.perceplist[j]:
                    self.addlist[key]["state"]="normal"
        else:
            for j in range(3):
                for key in self.perceplist[j]:
                    self.addlist[key]["state"]="disabled"

        j=0
        for key in ["clue","field","ambush"]:
            i=2
            for stat in self.perceplist[j]:
                Label(self.percepFrame,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=3*j+1)
                i+=1

            j+=1

        # action dissimulée
        if self.master.master.master.selectedchar.secondstats["symb-ability"][0]+self.master.master.master.selectedchar.secondstats["symb-ps_T"][0]+self.master.master.master.selectedchar.secondstats["symb-T"]:
            Label(self.hiddenFrame,text="Points restants : "+str(self.master.master.master.selectedchar.secondstats["symb-ability"][0]+self.master.master.master.selectedchar.secondstats["symb-ps_T"][0]+self.master.master.master.selectedchar.secondstats["symb-T"])).grid(row=0,column=9,sticky="w")
            for key in ["thievery","ambush","escape"]:
                self.addlist[key]["state"]="normal"
        else:
            for key in ["thievery","ambush","escape"]:
                self.addlist[key]["state"]="disabled"

        j=0
        for stat in ["thievery","ambush","escape"]:
            Label(self.hiddenFrame,text=self.master.master.master.selectedchar.thirdstats["hidden_action"][stat]).grid(row=1,column=3*j+1)
            j+=1"""

    def register(self):
        """
        Method that turns experience points into the selected caracteristic and registers the new stats

        :return: None
        """
        self.get_selectedchar().upstats(self.baselist[self.statlist.currentIndex()], int(self.add_stat.text()))
        self.parent().refresh_abi()
        self.parent().refresh_base()
        self.refresh()
