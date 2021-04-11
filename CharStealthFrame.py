from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLabel, QGridLayout, QSplitter, QFrame)
from PySide6.QtGui import (QPixmap, Qt)


class CharStealthFrame(QWidget):
    """ Widget qui affiche l'investissement de la furtivité dans la fiche résumé """

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.grid = QGridLayout(self)

        self.furtiflist = [["ground", "moving", "assassination"], ["shadow", "not-moving", "identity"],
                           ["smell", "disguise", "nature-field"]]
        self.stealth_image = QPixmap("./Images/symb-stealth.png")
        self.stealth_image = self.stealth_image.scaled(18, 8)
        self.grid.addWidget(QLabel("Furtivité "), 0, 0)
        self.grid.addWidget(QLabel(pixmap=self.stealth_image), 0, 1)

        i = 0
        for key in ["Silence : ", "Dissimulation : ", "Camouflage : "]:
            self.grid.addWidget(QLabel(key), 1, 3 * i)
            i += 1

        i = 2
        for key in ["Sol : ", "Déplacement : ", "Assassinat : "]:
            self.grid.addWidget(QLabel(key), i, 0)
            i += 1

        i = 2
        for key in ["Ombre : ", "Immobilité : ", "Identité : "]:
            self.grid.addWidget(QLabel(key), i, 3)
            i += 1

        i = 2
        for key in ["Odeur : ", "Déguisement : ", "Nature/Terrain : "]:
            self.grid.addWidget(QLabel(key), i, 6)
            i += 1

        """for i in range(2):
            self.columnconfigure(3*i+2,weight=1)"""



    def refresh(self):

        """for i in self.grid_slaves():
            info=i.grid_info()
            if info["row"]>=2 and info["column"] in [1,4,7]:
                i.destroy()

        j=0
        for key in ["silence","hiding","camo"]:
            i=2
            for stat in self.furtiflist[j]:
                Label(self,text=self.master.master.master.selectedchar.thirdstats[key][stat]).grid(row=i,column=3*j+1)
                i+=1

            j+=1"""
