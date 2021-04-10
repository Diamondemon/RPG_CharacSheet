from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QPlainTextEdit, QComboBox, QPushButton,
                               QTreeWidget, QTreeWidgetItem)
import Perso_class as Pc


class SpellCreatorFrame(QWidget):
    """ Widget de création des sorts """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)

        self.grid.addWidget(QLabel(self.tr("Créer un sort")), 0, 0, 1, 2)
        self.selected_item = None
        self.elemlist = ["Foudre"]
        self.subcateglist = ["Emprise", "Appel", "Altération", "Transfert", "Divination", "Lien"]

        self.grid.addWidget(QLabel(self.tr("Elément")), 1, 0)
        self.grid.addWidget(QLabel(self.tr("Sous-catégorie")), 1, 1)
        self.grid.addWidget(QLabel(self.tr("Nom")), 1, 2)
        self.grid.addWidget(QLabel(self.tr("Effets")), 3, 0)
        self.grid.addWidget(QLabel(self.tr("Description")), 3, 2)
        self.grid.addWidget(QLabel(self.tr("Coût")), 1, 3)

        self.Elem_entry = QComboBox()
        self.Elem_entry.setEditable(False)
        self.Elem_entry.addItems(self.elemlist)
        self.Elem_entry.setCurrentIndex(0)
        self.Subcateg_entry = QComboBox()
        self.Subcateg_entry.setEditable(False)
        self.Subcateg_entry.addItems(self.subcateglist)
        self.Subcateg_entry.setCurrentIndex(0)

        self.Name_entry = QLineEdit()
        self.Effect_entry = QPlainTextEdit()
        self.Description_entry = QPlainTextEdit()
        self.Cost_entry = QLineEdit()
        self.Cost_entry.setText("0")

        self.Register_choice = QPushButton(self.tr("Enregistrer"))
        self.Suppr_choice = QPushButton(self.tr("Supprimer"))
        self.Suppr_choice.setDisabled(True)

        self.grid.addWidget(self.Elem_entry, 2, 0)
        self.grid.addWidget(self.Subcateg_entry, 2, 1)
        self.grid.addWidget(self.Name_entry, 2, 2)
        self.grid.addWidget(self.Effect_entry, 4, 0, 1, 2)
        self.grid.addWidget(self.Cost_entry, 2, 3)
        self.grid.addWidget(self.Description_entry, 4, 2, 1, 2)
        self.grid.addWidget(self.Register_choice, 2, 4, 3, 1)
        self.grid.addWidget(self.Suppr_choice, 5, 4)

        self.connect(self.Register_choice, SIGNAL("clicked()"), self.register)
        self.connect(self.Suppr_choice, SIGNAL("clicked()"), self.suppr)

        self.Spell_view = QTreeWidget()
        self.Spell_view.setHeaderLabels(["Elément", "Effet", "Description", "Coût"])
        self.grid.addWidget(self.Spell_view, 5, 0, 1, 4)

        itemlist = []
        for key in self.elemlist:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", "", ""]))

        for key in self.subcateglist:
            itemlist[0].addChild(QTreeWidgetItem([self.tr(key), "", "", ""]))

        self.Spell_view.addTopLevelItems(itemlist)

        """self.Spell_view.bind("<Button-1>", func=self.select_spell)"""


    def register(self):
        """ Méthode qui crée le nouveau sort """
        new_spell = Pc.Spell(self.Elem_entry.get(), self.Subcateg_entry.get(), self.Name_entry.text(), self.Effect_entry.get(0.0, "end"), self.Description_entry.get(0.0, "end"), self.Cost_entry.text())

        self.parent().spelllist.append(new_spell)
        self.Spell_view.insert(new_spell.elem+new_spell.subcateg, "end", (len(self.master.spelllist)), text=new_spell.name, values=[new_spell.effect, new_spell.description, new_spell.cost])

    def refresh(self):
        """ Méthode qui rafraîchit la liste des sorts """

        for key in self.elemlist:
            for kkey in self.subcateglist:
                for i in self.Spell_view.get_children(key+kkey):
                    self.Spell_view.delete(i)

        if self.parent().spelllist:
            i = 1
            for key in self.parent().spelllist:
                self.Spell_view.insert(key.elem+key.subcateg, "end", i, text=key.name, values=[key.effect,key.description,key.cost])

                i += 1

    def select_spell(self,event):
        """ Méthode qui est appelée quand on sélectionne une compétence, pour ensuite la supprimer si besoin """
        if self.Spell_view.identify_row(event.y):

            try:
                self.selected_item = int(self.Spell_view.identify_row(event.y))
                self.suppr_choice["state"] = "normal"

            except:
                self.selected_item = None
                self.suppr_choice["state"] = "disabled"

        else:
            self.selected_item = None
            self.suppr_choice["state"] = "disabled"

    def suppr(self):
        """ Méthode qui supprime la compétence sélectionnée """
        if type(self.selected_item) == int:
            self.parent().spelllist.pop(self.selected_item-1)
            self.refresh()
            self.selected_item = None
            self.suppr_choice["state"] = "disabled"
