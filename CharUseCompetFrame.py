from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, QTextCursor
from PySide6.QtWidgets import (QGroupBox, QGridLayout, QPlainTextEdit, QTextEdit)

import CUF


class CharUseCompetFrame(QGroupBox):
    """ Widget used to display the character's competences """

    def __init__(self):
        QGroupBox.__init__(self, " Compétences ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.textedit = QTextEdit()
        self.textedit.setReadOnly(True)
        self.grid.addWidget(self.textedit, 0, 0)

    def refresh(self):
        competences = self.get_selectedchar().get_competences()
        text = ""
        i = 0
        for compet in competences:
            text += compet.name + " : " + compet.effect + "\n"
            i += 1
        self.textedit.setText(text)

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
