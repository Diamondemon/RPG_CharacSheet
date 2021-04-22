from PySide6.QtWidgets import (QTableWidget, QTableWidgetItem)
from PySide6.QtCore import Qt
import Perso_class as Pc


class ThrScopeTable(QTableWidget):
    """ Table Widget to display the scope of a shooting weapon """

    def __init__(self):
        QTableWidget.__init__(self)
        self.horizontalHeader().hide()
        self.setRowCount(3)
        self.setVerticalHeaderLabels([self.tr("Portée max"), self.tr("Vitesse"), self.tr("Mobilité")])
        self.setMinimumHeight(100)
        self.setMinimumWidth(200)
        self.verticalHeader().setMaximumWidth(70)
        self.setShowGrid(False)

    def refresh(self, equipment: Pc.ThrowEquip):
        """
        Method called to refresh the scope display of the specified shooting weapon

        :param equipment: shooting weapon to display the scope
        :return: None
        """
        scope = equipment.get_stat("scope")
        self.setColumnCount(len(scope))
        i = 0
        for trio in scope:
            self.setColumnWidth(i, 10)
            for value in enumerate(trio):
                item = QTableWidgetItem(str(value[1]))
                item.setTextAlignment(Qt.AlignCenter)
                item.setFlags(Qt.ItemIsEnabled)
                self.setItem(value[0], i, item)
            i += 1
