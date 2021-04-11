from PySide6.QtWidgets import (QGroupBox, QGridLayout)


class CharUseCompetFrame(QGroupBox):

    def __init__(self, parent):
        QGroupBox.__init__(self, " Compétences ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

    def refresh(self):
        """for i in self.grid_slaves():
            i.destroy()

        i=0
        for compet in self.master.master.master.selectedchar.competences:
            Message(self,text=compet.name+" : "+compet.effect,width=500).grid(row=i,column=0)
            i+=1"""

    def get_selectedchar(self):
        return self.master.get_selectedchar()
