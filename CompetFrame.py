from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QGridLayout, QWidget, QLabel, QComboBox, QLineEdit, QTextEdit, QPushButton, QTreeWidget, QTreeWidgetItem)
import Perso_class as Pc


class CompetCreatorFrame(QWidget):
    """ Widget de création des compétences """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.grid.addWidget(QLabel(self.tr("Créer une compétence")), 0, 0, 1, 2)
        self.categlist = ["Lore", "Mélée", "Jet", "Combat vétéran", "Armure"]
        self.selected_item = None

        self.grid.addWidget(QLabel(self.tr("Catégorie")), 1, 0)
        self.grid.addWidget(QLabel(self.tr("Sous-catégorie")), 1, 1)
        self.grid.addWidget(QLabel(self.tr("Intitulé")), 1, 2)
        self.grid.addWidget(QLabel(self.tr("Effets")), 1, 3)

        self.Categ_entry = QComboBox()
        self.Categ_entry.addItems(self.categlist)
        self.Categ_entry.setCurrentIndex(0)
        self.Subcateg_entry = QComboBox()
        self.Subcateg_entry.setDisabled(True)
        self.Name_entry = QLineEdit()
        self.Effect_entry = QTextEdit()

        self.Register_choice = QPushButton(self.tr("Enregistrer"))
        self.suppr_choice = QPushButton(self.tr("Supprimer"))
        self.suppr_choice.setDisabled(True)

        self.grid.addWidget(self.Categ_entry, 2, 0)
        self.grid.addWidget(self.Subcateg_entry, 2, 1)
        self.grid.addWidget(self.Name_entry, 2, 2)
        self.grid.addWidget(self.Effect_entry, 2, 3)
        self.grid.addWidget(self.Register_choice, 1, 4, 2, 1)
        self.grid.addWidget(self.suppr_choice, 3, 5)

        self.connect(self.Categ_entry, SIGNAL("activated()"), self.subcateg_roll)
        self.connect(self.Register_choice, SIGNAL("clicked()"), self.register)
        self.connect(self.suppr_choice, SIGNAL("clicked()"), self.suppr)

        # les compétences qui existent déjà
        self.Compet_view = QTreeWidget()
        self.Compet_view.setHeaderLabels(["Catégorie", "Nom", "Effet"])
        self.grid.addWidget(self.Compet_view, 3, 0, 1, 5)

        a = []
        for key in self.categlist:
            a.append(QTreeWidgetItem([key, "", ""]))

        for key in ["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"]:
            a[1].addChild(QTreeWidgetItem([key, "", ""]))

        for key in ["Lancer", "Arc", "Arbalète"]:
            a[2].addChild(QTreeWidgetItem([key, "", ""]))

        self.Compet_view.addTopLevelItems(a)
        """self.Compet_view.grid(row=3, column=0, columnspan=5, pady="8p", sticky="w")
        self.Compet_view.bind("<Button-1>", func=self.select_compet)"""

    @Slot()
    def subcateg_roll(self, event=None):
        """ Méthode pour faire changer les sous-catégories proposées en fonction de la catégorie choisie """
        val = self.Categ_entry.get()

        if val == "Mélée":
            self.Subcateg_entry["values"] = ["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"]
            self.Subcateg_entry.current(0)
            self.Subcateg_entry["state"] = "readonly"

        elif val == "Jet":
            self.Subcateg_entry["values"] = ["Lancer", "Arc", "Arbalète"]
            self.Subcateg_entry["state"] = "readonly"
            self.Subcateg_entry.current(0)

        elif val == "Armure":
            self.Subcateg_entry.set("")
            self.Subcateg_entry["values"] = []
            self.Subcateg_entry["state"] = "disabled"

        else:
            self.Subcateg_entry.set("")
            self.Subcateg_entry["values"] = []
            self.Subcateg_entry["state"] = "disabled"

    @Slot()
    def register(self):
        """ Méthode qui crée la nouvelle compétence """
        new_compet = Pc.Competence(self.Categ_entry.get(), self.Subcateg_entry.get(), self.Name_entry.text(),
                                   self.Effect_entry.get(0.0, "end"))

        self.parent().competlist.append(new_compet)
        """if new_compet.subcateg:
            self.Compet_view.insert(new_compet.subcateg, "end", (len(self.master.competlist)), values=[new_compet.name, new_compet.effect])
        else:
            self.Compet_view.insert(new_compet.categ, "end", (len(self.master.competlist)), values=[new_compet.name, new_compet.effect])"""

    @Slot()
    def refresh(self):
        """ Méthode qui rafraîchit la liste des compétences """

        """for key in ["Lore", "Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier", "Lancer", "Arc", "Arbalète", "Combat vétéran", "Armure"]:
            for i in self.Compet_view.get_children(key):
                self.Compet_view.delete(i)

        if self.parent().competlist:
            i = 1
            for key in self.parent().competlist:
                if key.subcateg:
                    self.Compet_view.insert(key.subcateg, "end", i, values=[key.name, key.effect])
                else:
                    self.Compet_view.insert(key.categ, "end", i, values=[key.name, key.effect])

                i += 1"""

    def select_compet(self, event):
        """ Méthode qui est appelée quand on sélectionne une compétence, pour ensuite la supprimer si besoin """
        """if self.Compet_view.identify_row(event.y):

            try:
                self.selected_item = int(self.Compet_view.identify_row(event.y))
                self.suppr_choice["state"] = "normal"

            except:
                self.selected_item = None
                self.suppr_choice["state"] = "disabled"

        else:
            self.selected_item = None
            self.suppr_choice["state"] = "disabled"""""

    def suppr(self):
        """ Méthode qui supprime la compétence sélectionnée """
        if type(self.selected_item) == int:
            self.parent().competlist.pop(self.selected_item-1)
            self.refresh()
            self.selected_item = None
            self.suppr_choice["state"] = "disabled"
