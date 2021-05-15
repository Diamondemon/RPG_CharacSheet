from PySide6.QtWidgets import (QGroupBox, QGridLayout, QTableWidget, QTableWidgetItem)
from PySide6.QtCore import Qt

import CUF


class CharPercFrame(QGroupBox):
    """ Widget to display the percentages of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Pourcentages ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.setMinimumHeight(185)

        self.perclist = ["Mains nues", "Armes légères", "Armes moyennes", "Armes lourdes", "Armes de jet", "Bouclier",
                         "Résistance physique", "Dextérité", "Mobilité", "Perception", "Furtivité",
                         "Résistance mentale", "Charisme", "Commerce", "Sorts", "Perception magique"]

        self.table = QTableWidget()
        self.table.setShowGrid(False)
        self.table.horizontalHeader().hide()
        self.table.verticalHeader().hide()
        self.grid.addWidget(self.table, 0, 0)

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CUF.CharUsefulFrame:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        return QGroupBox.parent(self)

    def refresh(self):
        """
        Method called to refresh the percentages of the character

        :return: None
        """
        selectedchar = self.get_selectedchar()
        percentages = selectedchar.get_percentages()
        self.table.clear()
        i = 0
        j = 0
        k = 0
        self.table.setRowCount(4)
        self.table.setColumnCount(len([elem for elem in percentages.values() if elem != 0]) // 4 + 1)
        for key in percentages.keys():
            if percentages[key] != 0:
                newitem = QTableWidgetItem(self.tr(self.perclist[j] + " : %n%", "", percentages[key]))
                newitem.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, k, newitem)
                i += 1

                if i == 4:
                    k += 1
                    i = 0
            j += 1
        if i != 0:
            for row in range(i, 4):
                newitem = QTableWidgetItem()
                newitem.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(row, k, newitem)



