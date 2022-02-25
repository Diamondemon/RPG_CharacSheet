from PySide6.QtCore import Slot, SIGNAL, Qt, QObject
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
        for key in self.categlist:
            self.Categ_entry.addItem(self.tr(key))
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
        self.Compet_view.setHeaderLabels([self.tr("Catégorie"), self.tr("Nom"), self.tr("Effet"), "Id"])
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
        Method called to refresh the TreeView

        :return: None
        """
        meleelist = ["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"]
        throwlist = ["Lancer", "Arc", "Arbalète"]
        self.Compet_view.clear()
        itemlist = []
        for key in self.categlist:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", ""]))

        for key in meleelist:
            itemlist[1].addChild(QTreeWidgetItem([self.tr(key), "", ""]))

        for key in throwlist:
            itemlist[2].addChild(QTreeWidgetItem([self.tr(key), "", ""]))

        self.Compet_view.addTopLevelItems(itemlist)

        competlist = self.parent().get_competlist()
        if competlist:
            i = 0
            for key in competlist:
                super_tree_item = self.Compet_view.findItems(self.tr(key.get_attr("categ")), Qt.MatchExactly, 0)[0]
                if key.get_attr("subcateg"):
                    if key.get_attr("categ") == "Mélée":
                        tree_item = super_tree_item.child(meleelist.index(key.get_attr("subcateg")))
                    else:
                        tree_item = super_tree_item.child(throwlist.index(key.get_attr("subcateg")))

                    tree_item.addChild(QTreeWidgetItem(["", key.get_attr("name"), key.get_attr("effect"), str(i)]))
                else:
                    super_tree_item.addChild(QTreeWidgetItem(["", key.get_attr("name"), key.get_attr("effect"),
                                                              str(i)]))
                i += 1
        self.Compet_view.expandAll()

    @Slot()
    def register(self):
        """
        Slot called to create a new competence based on what the user entered

        :return: None
        """
        meleelist = ["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"]
        throwlist = ["Lancer", "Arc", "Arbalète"]
        if self.Name_entry.text() and self.Effect_entry.toPlainText():
            if self.Effect_entry.toPlainText().endswith("\n"):
                text = self.Effect_entry.toPlainText()[:-1]
            else:
                text = self.Effect_entry.toPlainText()
            categ = self.categlist[self.Categ_entry.currentIndex()]
            subcateg = self.categlist[self.Subcateg_entry.currentIndex()]
            self.parent().generate_competence(categ, subcateg, self.Name_entry.text(), text)

            key = self.parent().get_competlist()[-1]
            i = len(self.parent().get_competlist()) - 1
            super_tree_item = self.Compet_view.findItems(self.tr(key.get_attr("categ")), Qt.MatchExactly, 0)[0]
            if key.get_attr("subcateg"):
                if key.get_attr("categ") == "Mélée":
                    tree_item = super_tree_item.child(meleelist.index(key.get_attr("subcateg")))
                else:
                    tree_item = super_tree_item.child(throwlist.index(key.get_attr("subcateg")))

                tree_item.addChild(QTreeWidgetItem(["", key.get_attr("name"), key.get_attr("effect"), str(i)]))
            else:
                super_tree_item.addChild(QTreeWidgetItem(["", key.get_attr("name"), key.get_attr("effect"), str(i)]))

    @Slot()
    def select_compet(self):
        """
        Slot called when selecting a competence in the TreeWidget

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
        val = self.Categ_entry.currentIndex()

        if val == 1:
            self.Subcateg_entry.clear()
            self.Subcateg_entry.addItems(["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"])
            self.Subcateg_entry.setCurrentIndex(0)
            self.Subcateg_entry.setDisabled(False)

        elif val == 2:
            self.Subcateg_entry.clear()
            self.Subcateg_entry.addItems(["Lancer", "Arc", "Arbalète"])
            self.Subcateg_entry.setCurrentIndex(0)
            self.Subcateg_entry.setDisabled(False)

        elif val == 4:
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
