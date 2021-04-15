from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QFrame, QLabel, QGridLayout, QPlainTextEdit, QComboBox, QPushButton,
                               QTreeWidget, QTreeWidgetItem)

import CNbk
from CharFirstSymbFrame import CharFirstSymbFrame
from CharPercepFrame import CharPercepFrame
from CharStealthFrame import CharStealthFrame
from CharHiddenFrame import CharHiddenFrame
from CharUseCompetFrame import CharUseCompetFrame
from CharMelFrame import CharMelFrame
from CharThrFrame import CharThrFrame
from CharArmFrame import CharArmFrame
from CharPercFrame import CharPercFrame


class CharUsefulFrame(QWidget):
    """ Fiche personnage résumée """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)

        self.CharFSymF = CharFirstSymbFrame(self)
        self.grid.addWidget(self.CharFSymF, 0, 0)

        self.CharPercepF = CharPercepFrame(self)
        self.grid.addWidget(self.CharPercepF, 1, 0, 2, 1)

        self.CharStealthF = CharStealthFrame(self)
        self.grid.addWidget(self.CharStealthF, 3, 0, 2, 1)

        self.CharHiddenF = CharHiddenFrame(self)
        self.grid.addWidget(self.CharHiddenF, 5, 0, 2, 1)

        self.CharUCompF = CharUseCompetFrame(self)
        self.grid.addWidget(self.CharUCompF, 7, 0, 2, 1)

        separator = QFrame(self)
        separator.setFrameShape(QFrame.VLine)
        separator.setLineWidth(3)
        self.grid.addWidget(separator, 0, 3, 9, 1)

        self.CharMelF = CharMelFrame(self)
        self.grid.addWidget(self.CharMelF, 0, 4, 2, 1)

        self.CharThrF = CharThrFrame(self)
        self.grid.addWidget(self.CharThrF, 2, 4, 2, 1)

        self.CharArmF = CharArmFrame(self)
        self.grid.addWidget(self.CharArmF, 4, 4, 2, 1)

        self.PercFrame = CharPercFrame(self)
        self.grid.addWidget(self.PercFrame, 6, 4, 2, 1)

        """self.bind("<Visibility>", func=self.refresh)"""

    def refresh(self, event=None):
        print(self.parentWidget())
        """
        self.CharFSymF.refresh()
        self.CharPercepF.refresh()
        self.CharStealthF.refresh()
        self.CharHiddenF.refresh()
        self.CharUCompF.refresh()

        self.CharArmF.refresh()
        self.CharMelF.refresh()
        self.CharThrF.refresh()
        self.PercFrame.refresh()"""

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the Notebook)

        :return: the reference to the parent
        """
        return self.parentWidget().parent()
