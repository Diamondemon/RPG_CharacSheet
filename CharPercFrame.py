from PySide6.QtWidgets import (QGroupBox, QGridLayout, QFrame, QTreeWidget, QTreeWidgetItem, QLabel)
from PySide6.QtGui import (QPixmap, QIcon)
import numpy as np


class CharPercFrame(QGroupBox):
    """ cadre d'affichage des pourcentages du personnage """

    def __init__(self, parent):
        QGroupBox.__init__(self, " Pourcentages ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.perclist = ["Mains nues", "Armes légères", "Armes moyennes", "Armes lourdes", "Armes de jet", "Bouclier",
                         "Résistance physique", "Dextérité", "Mobilité", "Perception", "Furtivité",
                         "Résistance mentale", "Charisme", "Commerce", "Sorts", "Perception magique"]



    def refresh(self):
        """ fonction qui réaffiche les statistiques de pourcentages du personnage """

        """for key in self.grid_slaves():
            key.destroy()
        i=0
        j=0
        k=0
        for key in self.master.master.master.selectedchar.percentages.keys():
            if self.master.master.master.selectedchar.percentages[key]!=0:
                Label(self,text=self.perclist[j]+" : "+str(self.master.master.master.selectedchar.percentages[key])+"%").grid(row=i,column=2*k)
                i+=1

                if i==4:
                    k+=1
                    i=0
                if i==0:
                    ttk.Separator(self,orient="vertical").grid(row=0,column=2*k-1,rowspan=4,sticky="ns",pady="2p")
            j+=1"""

    def get_selectedchar(self):
        return self.master.get_selectedchar()
