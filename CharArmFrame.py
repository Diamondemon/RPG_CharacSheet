from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QGroupBox, QGridLayout, QFrame, QTreeWidget, QTreeWidgetItem)
from PySide6.QtGui import (QIcon)
import numpy as np
import CUF


class CharArmFrame(QGroupBox):
    """ Widget to display the armor equipment equipped on the character """

    def __init__(self):
        QGroupBox.__init__(self, " Armure ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.setMinimumWidth(840)

        threshold_types = ["Arm. Légère", "Arm. Moyenne", "Arm. Lourde"]
        self.Threshold_View = QTreeWidget()
        self.Threshold_View.header().setDefaultAlignment(Qt.AlignCenter)
        self.Threshold_View.setHeaderLabels([self.tr("Palier d'armure %n", "", 0), self.tr("Val. d'Arm."),
                                             self.tr("Vit."), self.tr("Mobi.")])
        self.grid.addWidget(self.Threshold_View, 0, 0, 1, 8)

        itemlist = []
        for key in threshold_types:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", "", ""]))
            for j in range(1, 4):
                itemlist[-1].setTextAlignment(j, Qt.AlignCenter)
        self.Threshold_View.addTopLevelItems(itemlist)

        separator = QFrame(self)
        separator.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator, 1, 0, 1, 8)

        self.armor_attr = ["", "Nom", "Prot.", "Amort.", "Mobi.", "Vit.", "Sol.", ""]

        self.Armorlist = ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette",
                          "Cuissots", "Grèves", "Solerets"]

        self.Armor_View = QTreeWidget()
        self.Armor_View.setHeaderLabels(self.armor_attr)
        self.Armor_View.headerItem().setIcon(7, QIcon("./Images/symb-armor.png"))
        self.grid.addWidget(self.Armor_View, 2, 0, 1, 8)

        itemlist = []
        for key in self.Armorlist:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", "", "", "", "", "", ""]))
        self.Armor_View.addTopLevelItems(itemlist)

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CUF.CharUsefulFrame:
        """
        Method called to get the parent widget (the Useful frame)

        :return: the reference to the parent
        """
        return QGroupBox.parent(self)

    def refresh(self):
        """
        Method called to refresh the armor equipments of the character along with its compatibility with them

        :return: None
        """
        palier = np.array([[[-10, -4, -8], [-8, -8, -10], [-4, -20, -12]], [[-8, -2, -6], [-4, -4, -6], [-2, -10, -10]],
                           [[-6, 0, -4], [-3, -4, -6], [-1, -8, -8]], [[-4, 0, -2], [-1, -4, -4], [0, -6, -6]],
                           [[-2, 0, 0], [0, -2, -2], [0, -4, -4]], [[0, 2, 0], [0, 0, -1], [0, -2, -2]],
                           [[0, 4, 0], [0, 2, -1], [2, 0, -2]], [[2, 6, 2], [4, 2, 1], [6, 0, 0]],
                           [[4, 8, 4], [6, 3, 2], [8, 0, 0]]])

        selectedchar = self.get_selectedchar()
        armor_level = selectedchar.get_armor_level()

        header = self.Threshold_View.headerItem()
        header.setText(0, self.tr("Palier d'armure %n", "", armor_level))
        i = 0
        for trio in palier[armor_level]:
            item = self.Threshold_View.topLevelItem(i)
            for j in range(1, 4):
                item.setText(j, str(trio[j-1]))
            i += 1

        self.Armor_View.clear()
        for item in self.Armorlist:
            invested_armor = str(selectedchar.get_invested_armor(item))
            linked_equip = selectedchar.get_current_armor(item)
            if linked_equip:
                stats = linked_equip.get_stats_aslist(["name", "prot", "amort", "mobi", "vit", "solid"])
                for i in range(1, 6):
                    stats[i] = str(stats[i])
            else:
                stats = ["..."]*6
            self.Armor_View.addTopLevelItem(QTreeWidgetItem([self.tr(item)]+stats+[invested_armor]))
