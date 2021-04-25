from PySide6.QtCore import SIGNAL, Slot
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QTreeWidget, QFrame, QLineEdit, QPlainTextEdit

import CNbk


class CharCompetFrame(QWidget):
    """ Widget pour attribuer des compétences au personnage """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.selected_item = None
        self.selected_charitem = None
        self.modif_compet = None
        self.categlist = ["Lore", "Mélée", "Jet", "Combat vétéran", "Armure"]

        # les compétences du personnage

        self.grid.addWidget(QLabel(self.tr("Compétences du personnage")), 0, 0)
        self.modify_choice = QPushButton(self.tr("Modifier"))
        self.modify_choice.setDisabled(True)
        self.connect(self.modify_choice, SIGNAL("clicked()"), self.modify_compet)
        self.suppr_choice = QPushButton(self.tr("Retirer"))
        self.suppr_choice.setDisabled(True)
        self.connect(self.suppr_choice, SIGNAL("clicked()"), self.suppr_compet)

        self.CharCompet_view = QTreeWidget()
        self.CharCompet_view.setHeaderLabels(["Catégorie", "Nom", "Effet", "Id"])
        self.CharCompet_view.hideColumn(3)
        self.grid.addWidget(self.CharCompet_view, 3, 0, 1, 5)

        self.grid.addWidget(self.CharCompet_view, 1, 0, 2, 5)
        self.grid.addWidget(self.modify_choice, 1, 5)
        self.grid.addWidget(self.suppr_choice, 2, 5)

        self.connect(self.CharCompet_view, SIGNAL("itemSelectionChanged()"), self.select_compet)

        # les compétences qui existent déjà

        self.grid.addWidget(QLabel(self.tr("Compétences disponibles")), 3, 0)
        self.transfer_choice = QPushButton(self.tr("Prendre"))
        self.transfer_choice.setDisabled(True)
        self.connect(self.transfer_choice, SIGNAL("clicked()"), self.transfer_compet)

        self.Compet_view = QTreeWidget()
        self.Compet_view.setHeaderLabels(["Catégorie", "Nom", "Effet", "Id"])
        self.Compet_view.hideColumn(3)
        self.grid.addWidget(self.Compet_view, 4, 0, 1, 5)

        self.grid.addWidget(self.transfer_choice, 4, 5)

        self.connect(self.Compet_view, SIGNAL("itemSelectionChanged()"), self.select_compet)

        # widgets de modification
        separator = QFrame(self)
        separator.setFrameShape(QFrame.VLine)
        self.grid.addWidget(separator, 0, 6, 5, 1)
        self.modif_name = QLineEdit()
        self.modif_effect = QPlainTextEdit()
        self.modif_validate = QPushButton(self.tr("Retirer"))
        self.modif_validate.setDisabled(True)
        self.connect(self.modif_validate, SIGNAL("clicked()"), self.modif_register)

    def transfer_compet(self):
        """
        Method called to give the selected competence to the selected character

        :return: None
        """
        if self.selected_item:
            self.get_selectedchar().compet_add(self.get_competlist()[self.selected_item].copy())
            self.refresh_char()
            self.save_character()

    def refresh(self):
        """
        Method called to refresh everything on display

        :return: None
        """
        self.refresh_char()
        self.refresh_general()

    def refresh_char(self):
        """
        Method called to refresh the competences possessed by the character

        :return: None
        """

        """for key in ["Lore","Mains nues","Une main","Doubles","Deux mains","Bouclier","Lancer","Arc","Arbalète","Combat vétéran","Armure"]:
            for i in self.CharCompet_view.get_children(key):
                self.CharCompet_view.delete(i)

        for i in self.grid_slaves(column=7):
            i.grid_forget()

        if self.master.master.selectedchar.competences:
            i=1
            for key in self.master.master.selectedchar.competences:
                if key.subcateg:
                    self.CharCompet_view.insert(key.subcateg,"end",i,values=[key.name,key.effect])
                else:
                    self.CharCompet_view.insert(key.categ,"end",i,values=[key.name,key.effect])

                i+=1"""

    def refresh_general(self):
        """ Méthode qui rafraîchit la liste des compétences """

        """for key in ["Lore","Mains nues","Une main","Doubles","Deux mains","Bouclier","Lancer","Arc","Arbalète","Combat vétéran","Armure"]:
            for i in self.Compet_view.get_children(key):
                self.Compet_view.delete(i)

        if self.master.master.master.competlist:
            i=1
            for key in self.master.master.master.competlist:
                if key.subcateg:
                    self.Compet_view.insert(key.subcateg,"end",i,values=[key.name,key.effect])
                else:
                    self.Compet_view.insert(key.categ,"end",i,values=[key.name,key.effect])

                i+=1"""

    @Slot()
    def select_compet(self):
        """
        Slot called when selecting a competence from the list of available competences

        :return: None
        """

        """if self.Compet_view.identify_row(event.y):

            try:
                self.selected_item=int(self.Compet_view.identify_row(event.y))
                self.transfer_choice["state"]="normal"

            except:
                self.selected_item=None
                self.transfer_choice["state"]="disabled"

        else:
            self.selected_item=None
            self.transfer_choice["state"]="disabled"
        """

    def select_charcompet(self):
        """
        Slot called when selecting a competence among the competences of the character

        :return: None
        """
        """if self.CharCompet_view.identify_row(event.y):

            try:
                self.selected_charitem=int(self.CharCompet_view.identify_row(event.y))
                self.selected_compet=None
                self.suppr_choice["state"]="normal"
                self.modify_choice["state"]="normal"

            except:
                self.selected_charitem=None
                self.selected_compet=None
                self.suppr_choice["state"]="disabled"
                self.modify_choice["state"]="disabled"

        else:
            self.selected_charitem=None
            self.selected_compet=None
            self.suppr_choice["state"]="disabled"
            self.modify_choice["state"]="disabled" 
            """

    def modify_compet(self):
        """ Méthode qui permet d'éditer la compétence du personnage sélectionnée """
        """if self.selected_charitem:
            self.selected_compet=self.master.master.selectedchar.competences[self.selected_charitem-1]
            Label(self,text="Modifications").grid(row=0,column=7)
            self.modif_name.grid(row=1,column=7,sticky="w")
            self.modif_effect.grid(row=2,column=7,sticky="w")
            self.modif_validate.grid(row=3,column=7)
            self.modif_var.set(self.selected_compet.name)
            self.modif_effect.delete(0.0,"end")
            self.modif_effect.insert("end",self.selected_compet.effect)"""

    def suppr_compet(self):
        """
        Method called to remove the selected competence from the character's competences

        :return:
        """
        if self.selected_charitem:
            self.get_selectedchar().compet_suppr(self.selected_charitem)
            self.suppr_choice.setDisabled(True)
            self.modify_choice.setDisabled(True)
            self.refresh_char()

    def modif_register(self):
        """ Méthode qui permet d'enregistrer les modifications apportées """
        """self.selected_compet.name=self.modif_var.get()
        self.selected_compet.effect=self.modif_effect.get(0.0,"end")
        self.refresh_char()"""

    def get_competlist(self):
        """
        Method called to get the available competences

        :return: Reference to the list of competences
        """
        return self.parent().get_competlist()

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        return self.parentWidget().parent()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()
