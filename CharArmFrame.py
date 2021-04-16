from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QGroupBox, QGridLayout, QFrame, QTreeWidget, QTreeWidgetItem, QLabel)
from PySide6.QtGui import (QPixmap, QIcon)
import numpy as np


class CharArmFrame(QGroupBox):

    def __init__(self):
        QGroupBox.__init__(self, " Armure ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.threshold_types = ["Arm. Légère", "Arm. Moyenne", "Arm. Lourde"]
        self.Threshold_View = QTreeWidget()
        self.Threshold_View.setHeaderLabels(["Palier d'armure 3", "Val. d'Arm.", "Vit.", "Mobi."])
        self.grid.addWidget(self.Threshold_View, 0, 0, 1, 8)

        itemlist = []
        for key in self.threshold_types:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", "", ""]))
        self.Threshold_View.addTopLevelItems(itemlist)

        separator = QFrame(self)
        separator.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator, 1, 0, 1, 8)

        self.armor_attr = ["", "Nom", "Prot.", "Amort.", "Mobi.", "Vit.", "Sol.", "Casque"]

        self.armor_image = QSvgWidget("./Images/symb-armor.svg")
        self.armor_image.setFixedSize(12, 20)

        self.Armorlist = ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette",
                          "Cuissots", "Grèves", "Solerets"]

        self.Armor_View = QTreeWidget()
        self.Armor_View.setHeaderLabels(self.armor_attr)
        self.grid.addWidget(self.Armor_View, 2, 0, 1, 8)

        itemlist = []
        for key in self.Armorlist:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", "", "", "", "", "", ""]))
        self.Armor_View.addTopLevelItems(itemlist)

    def refresh(self):
        """palier = np.array([[[-10, -4, -8], [-8, -8, -10], [-4, -20, -12]], [[-8, -2, -6], [-4, -4, -6], [-2, -10, -10]],
                           [[-6, 0, -4], [-3, -4, -6], [-1, -8, -8]], [[-4, 0, -2], [-1, -4, -4], [0, -6, -6]],
                           [[-2, 0, 0], [0, -2, -2], [0, -4, -4]], [[0, 2, 0], [0, 0, -1], [0, -2, -2]],
                           [[0, 4, 0], [0, 2, -1], [2, 0, -2]], [[2, 6, 2], [4, 2, 1], [6, 0, 0]],
                           [[4, 8, 4], [6, 3, 2], [8, 0, 0]]])
        armor_level = self.parent().parent().parent().selectedchar.get_armor_level()
        self.Threshold_View.heading("#0", text="Palier d'armure " + str(armor_level))
        i = 0
        for item in self.Threshold_View.get_children():
            for j in range(3):
                self.Threshold_View.set(item, column=str(j), value=("+" * int(palier[armor_level, i, j] > 0)) + str(
                    palier[armor_level, i, j]))
            i += 1

        for item in self.Armor_View.get_children():
            self.Armor_View.set(item, "6", self.master.master.master.selectedchar.get_invested_armor(item))
            linked_equip = self.master.master.master.selectedchar.get_current_armor(item)
            if linked_equip:
                valuelist = linked_equip.get_stats_aslist(["name", "prot", "amort", "mobi", "vit", "solid"])
                for i in range(6):
                    self.Armor_View.set(item, str(i), value=valuelist[i])

            else:

                for i in range(6):
                    self.Armor_View.set(item, str(i), value="...")"""

    def get_selectedchar(self):
        return self.master.get_selectedchar()