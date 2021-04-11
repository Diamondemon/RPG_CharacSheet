from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout, QSplitter, QFrame)
from PySide6.QtGui import (QPixmap, Qt)


class CharPercepFrame(QWidget):
    """ Widget qui affiche les investissements dans les sens et l'analyse sur la fiche résumé """

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.grid = QGridLayout(self)

        self.perceplist = [["intention", "thing-info", "bestiary"], ["trap", "find", "tracking"],
                           ["ennemies", "threat", "curse"]]

        self.percep_image = QPixmap("./Images/symb-perception.png")
        self.percep_image = self.percep_image.scaled(12, 15)
        self.grid.addWidget(QLabel("Analyse/Perception "), 0, 0, 1, 2)
        self.grid.addWidget(QLabel(pixmap=self.percep_image), 0, 2)

        i = 2
        for key in ["Vue :", "Ouïe :", "Odorat :"]:
            self.grid.addWidget(QLabel(key), i, 0)
            i += 1

        separator = QFrame(self)
        separator.setFrameShape(QFrame.VLine)
        self.grid.addWidget(separator, 1, 2, 4, 1)

        i = 0
        for key in ["Indice : ", "Terrain : ", "Embuscade : "]:
            self.grid.addWidget(QLabel(key), 1, 2 * i + 3)
            i += 1

        i = 2
        for key in ["Intention : ", "Objet-info : ", "Bestiaire : "]:
            self.grid.addWidget(QLabel(key), i, 3)
            i += 1

        i = 2
        for key in ["Piège : ", "Trouver Objets : ", "Pistage : "]:
            self.grid.addWidget(QLabel(key), i, 5)
            i += 1

        i = 2
        for key in ["Adversaires : ", "Menace : ", "Malédiction : "]:
            self.grid.addWidget(QLabel(key), i, 7)
            i += 1

    def refresh(self):
        """
        for i in self.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,6,8]:
                i.destroy()

        i=2
        for key in ["sight","hearing","smell"]:
            Label(self,text=self.master.master.master.selectedchar.thirdstats[key]).grid(row=i,column=1)
            i+=1

        j=0
        for key in ["clue","field","ambush"]:
            i=2
            for stat in self.perceplist[j]:
                Label(self,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=2*j+4)
                i+=1

            j+=1"""

    def get_selectedchar(self):
        return self.parent().get_selectedchar()