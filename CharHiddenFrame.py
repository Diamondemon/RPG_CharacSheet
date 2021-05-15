from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout)

import CUF


class CharHiddenFrame(QWidget):
    """ Widget displaying what has been invested in hidden actions """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.setMaximumHeight(60)

        self.labels = []

        self.grid.addWidget(QLabel("Action dissimulée"), 0, 0)

        i = 0
        for key in ["Vol à la tire : ", "Embuscade : ", "Fuite : "]:
            self.grid.addWidget(QLabel(self.tr(key)), 1, 2 * i)
            self.labels.append(QLabel(""))
            self.grid.addWidget(self.labels[i], 1, 2 * i + 1)
            i += 1

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
        return self.parentWidget()

    def refresh(self):
        """
        Method called to refresh the invested points

        :return: None
        """
        thirdstats = self.get_selectedchar().get_thirdstats()

        i = 0
        for key in ["thievery", "ambush", "escape"]:
            self.labels[i].setText(str(thirdstats["hidden_action"][key]))
            i += 1
