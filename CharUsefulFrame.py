from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QFrame, QLabel, QGridLayout, QPlainTextEdit, QComboBox, QPushButton,
                               QTreeWidget, QTreeWidgetItem)
from CharFirstSymbFrame import CharFirstSymbFrame
from CharPercepFrame import CharPercepFrame
from CharStealthFrame import CharStealthFrame
from CharHiddenFrame import CharHiddenFrame
from CharUseCompetFrame import CharUseCompetFrame
from CharMelFrame import CharMelFrame


class CharUsefulFrame(QWidget):
    """ Fiche personnage résumée """

    def __init__(self, parent):
        QWidget.__init__(self, parent)
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
        self.grid.addWidget(self.CharUCompF, 0, 4, 2, 1)

        """self.CharThrF = CharThrFrame(self, text=" Jet ")
        self.CharThrF.grid(row=2, column=4, sticky="we", padx="4p", ipadx='2p', ipady='2p')

        self.CharArmF = CharArmFrame(self, text=" Armure ")
        self.CharArmF.grid(row=3, column=4, sticky="we", padx="4p", ipadx='2p', ipady='2p', rowspan=3)

        self.PercFrame = CharPercFrame(self, text=" Pourcentages ", relief="groove")
        self.PercFrame.grid(row=6, column=4, padx="4p", pady="4p", sticky="we")

        self.bind("<Visibility>", func=self.refresh)"""

    def refresh(self, event=None):
        self.CharFSymF.refresh()
        self.CharPercepF.refresh()
        self.CharStealthF.refresh()
        self.CharHiddenF.refresh()
        self.CharUCompF.refresh()

        self.CharArmF.refresh()
        self.CharMelF.refresh()
        self.CharThrF.refresh()
        self.PercFrame.refresh()

    def get_selectedchar(self):
        return self.master.get_selectedchar()