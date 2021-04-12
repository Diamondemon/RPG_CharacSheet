from PySide6.QtCore import Slot, SIGNAL, Qt
from PySide6.QtWidgets import (QGridLayout, QWidget, QLabel, QComboBox, QLineEdit, QPlainTextEdit, QPushButton,
                               QTreeWidget, QTreeWidgetItem)
import MW


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
        self.Categ_entry.setEditable(False)
        self.Categ_entry.addItems(self.categlist)
        self.Categ_entry.setCurrentIndex(0)
        self.Subcateg_entry = QComboBox()
        self.Subcateg_entry.setEditable(False)
        self.Subcateg_entry.setDisabled(True)
        self.Name_entry = QLineEdit()
        self.Effect_entry = QPlainTextEdit()

        self.Register_choice = QPushButton(self.tr("Enregistrer"))
        self.suppr_choice = QPushButton(self.tr("Supprimer"))
        self.suppr_choice.setDisabled(True)

        self.grid.addWidget(self.Categ_entry, 2, 0)
        self.grid.addWidget(self.Subcateg_entry, 2, 1)
        self.grid.addWidget(self.Name_entry, 2, 2)
        self.grid.addWidget(self.Effect_entry, 2, 3)
        self.grid.addWidget(self.Register_choice, 1, 4, 2, 1)
        self.grid.addWidget(self.suppr_choice, 3, 5)

        self.connect(self.Categ_entry, SIGNAL("currentIndexChanged(int)"), self.subcateg_roll)
        self.connect(self.Register_choice, SIGNAL("clicked()"), self.register)
        self.connect(self.suppr_choice, SIGNAL("clicked()"), self.suppr)

        # les compétences qui existent déjà
        self.Compet_view = QTreeWidget()
        self.Compet_view.setHeaderLabels(["Catégorie", "Nom", "Effet", "Id"])
        self.Compet_view.hideColumn(3)
        self.grid.addWidget(self.Compet_view, 3, 0, 1, 5)

        self.connect(self.Compet_view, SIGNAL("itemSelectionChanged()"), self.select_compet)

    def parent(self) -> MW.UIWindow:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def refresh(self):
        """
        Méthode qui rafraîchit la liste des compétences

        :return: None
        """

        self.Compet_view.clear()
        itemlist = []
        for key in self.categlist:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", ""]))

        for key in ["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"]:
            itemlist[1].addChild(QTreeWidgetItem([self.tr(key), "", ""]))

        for key in ["Lancer", "Arc", "Arbalète"]:
            itemlist[2].addChild(QTreeWidgetItem([self.tr(key), "", ""]))

        self.Compet_view.addTopLevelItems(itemlist)

        competlist = self.parent().get_competlist()
        if competlist:
            i = 0
            for key in competlist:
                super_tree_item = self.Compet_view.findItems(key.categ, Qt.MatchExactly, 0)[0]
                if key.subcateg:
                    if key.categ == "Mélée":
                        tree_item = super_tree_item.child(["Mains nues", "Une main", "Doubles", "Deux mains",
                                                           "Bouclier"].index(key.subcateg))
                    else:
                        tree_item = super_tree_item.child(["Lancer", "Arc", "Arbalète"].index(key.subcateg))

                    tree_item.addChild(QTreeWidgetItem(["", key.name, key.effect, str(i)]))
                else:
                    super_tree_item.addChild(QTreeWidgetItem(["", key.name, key.effect, str(i)]))
                i += 1
        self.Compet_view.expandAll()

    @Slot()
    def register(self):
        """
        Méthode qui crée la nouvelle compétence

        :return: None
        """
        if self.Name_entry.text() and self.Effect_entry.toPlainText():
            if self.Effect_entry.toPlainText().endswith("\n"):
                text = self.Effect_entry.toPlainText()[:-1]
            else:
                text = self.Effect_entry.toPlainText()
            self.parent().generate_competence(self.Categ_entry.currentText(), self.Subcateg_entry.currentText(),
                                              self.Name_entry.text(), text)

            key = self.parent().get_competlist()[-1]
            i = len(self.parent().get_competlist()) - 1
            super_tree_item = self.Compet_view.findItems(key.categ, Qt.MatchExactly, 0)[0]
            if key.subcateg:
                if key.categ == "Mélée":
                    tree_item = super_tree_item.child(["Mains nues", "Une main", "Doubles", "Deux mains",
                                                       "Bouclier"].index(key.subcateg))
                else:
                    tree_item = super_tree_item.child(["Lancer", "Arc", "Arbalète"].index(key.subcateg))

                tree_item.addChild(QTreeWidgetItem(["", key.name, key.effect, str(i)]))
            else:
                super_tree_item.addChild(QTreeWidgetItem(["", key.name, key.effect, str(i)]))

    @Slot()
    def select_compet(self):
        """
        Méthode qui est appelée quand on sélectionne une compétence, pour ensuite la supprimer si besoin

        :return: None
        """
        selected_items = self.Compet_view.selectedItems()
        if len(selected_items) == 1:
            item = selected_items[0]
            if item.text(3):
                try:
                    self.selected_item = int(item.text(3))
                    self.suppr_choice.setDisabled(False)

                except ValueError:
                    self.selected_item = None
                    self.suppr_choice.setDisabled(True)

            else:
                self.selected_item = None
                self.suppr_choice.setDisabled(True)

    @Slot()
    def subcateg_roll(self):
        """
        Slot called to change proposed subcategories according to the selected category

        :return: None
        """
        val = self.Categ_entry.currentText()

        if val == "Mélée":
            self.Subcateg_entry.clear()
            self.Subcateg_entry.addItems(["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"])
            self.Subcateg_entry.setCurrentIndex(0)
            self.Subcateg_entry.setDisabled(False)

        elif val == "Jet":
            self.Subcateg_entry.clear()
            self.Subcateg_entry.addItems(["Lancer", "Arc", "Arbalète"])
            self.Subcateg_entry.setCurrentIndex(0)
            self.Subcateg_entry.setDisabled(False)

        elif val == "Armure":
            self.Subcateg_entry.clear()
            self.Subcateg_entry.setDisabled(True)

        else:
            self.Subcateg_entry.clear()
            self.Subcateg_entry.setDisabled(True)

    @Slot()
    def suppr(self):
        """
        Slot called to delete the selected spell

        :return: None
        """
        if type(self.selected_item) == int:
            self.parent().pop_compet(self.selected_item)
            self.selected_item = None
            self.suppr_choice.setDisabled(True)
            self.refresh()
