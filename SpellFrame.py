from PySide6.QtCore import SIGNAL, Qt, Slot
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QPlainTextEdit, QComboBox, QPushButton,
                               QTreeWidget, QTreeWidgetItem)
import MW


class SpellCreatorFrame(QWidget):
    """ Widget to create and delete spells """

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
        self.Cost_entry.setValidator(QIntValidator(0, 9999, self))

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
        self.Spell_view.setHeaderLabels([self.tr("Elément"), self.tr("Nom"), self.tr("Effet"), self.tr("Description"),
                                         self.tr("Coût"), self.tr("Id")])
        self.Spell_view.hideColumn(5)
        self.grid.addWidget(self.Spell_view, 5, 0, 1, 4)

        self.connect(self.Spell_view, SIGNAL("itemSelectionChanged()"), self.select_spell)

    def parent(self) -> MW.UIWindow:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    @Slot()
    def register(self):
        """
        Slot called to create a new spell

        :return: None
        """
        if self.Name_entry.text() and self.Effect_entry.toPlainText() and self.Cost_entry.text():
            if self.Effect_entry.toPlainText().endswith("\n"):
                effect_text = self.Effect_entry.toPlainText()[:-1]
            else:
                effect_text = self.Effect_entry.toPlainText()

            if self.Description_entry.toPlainText().endswith("\n"):
                descr_text = self.Description_entry.toPlainText()[:-1]
            else:
                descr_text = self.Description_entry.toPlainText()

            elem = self.elemlist[self.Elem_entry.currentIndex()]
            subcateg = self.subcateglist[self.Subcateg_entry.currentIndex()]
            self.parent().generate_spell(elem, subcateg,
                                         self.Name_entry.text(), effect_text,
                                         descr_text, int(self.Cost_entry.text()))

            key = self.parent().get_spelllist()[-1]
            i = len(self.parent().get_spelllist()) - 1
            super_tree_item = self.Spell_view.findItems(self.tr(key.get_stat("elem")), Qt.MatchExactly, 0)[0]
            tree_item = super_tree_item.child(self.subcateglist.index(key.get_stat("subcateg")))
            tree_item.addChild(QTreeWidgetItem([""] + key.get_stats_aslist(["name", "effect", "description", "cost"]) +
                                               [str(i)]))

    def refresh(self):
        """
        Method called to refresh the list of spells displayed

        :return: None
        """
        self.Spell_view.clear()
        itemlist = []
        for key in self.elemlist:
            itemlist.append(QTreeWidgetItem([self.tr(key)]))

        for key in self.subcateglist:
            for i in enumerate(itemlist):
                i[1].addChild(QTreeWidgetItem([self.tr(key)]))

        self.Spell_view.addTopLevelItems(itemlist)

        spelllist = self.parent().get_spelllist()
        if spelllist:
            i = 0
            for key in spelllist:
                super_tree_item = self.Spell_view.findItems(self.tr(key.get_stat("elem")), Qt.MatchExactly, 0)[0]
                tree_item = super_tree_item.child(self.subcateglist.index(key.get_stat("subcateg")))
                tree_item.addChild(QTreeWidgetItem([""] + key.get_stats_aslist(["name", "effect",
                                                                                "description", "cost"]) + [str(i)]))
                i += 1

        self.Spell_view.expandAll()

    @Slot()
    def select_spell(self):
        """
        Slot called when a spell is selected, to delete it if needed

        :return: None
        """
        selected_items = self.Spell_view.selectedItems()
        if len(selected_items) == 1:
            item = selected_items[0]
            if item.text(5):
                try:
                    self.selected_item = int(item.text(5))
                    self.Suppr_choice.setDisabled(False)

                except ValueError:
                    self.selected_item = None
                    self.Suppr_choice.setDisabled(True)

            else:
                self.selected_item = None
                self.Suppr_choice.setDisabled(True)

    @Slot()
    def suppr(self):
        """
        Method called to delete the selected spell

        :return: None
        """
        if type(self.selected_item) == int:
            self.parent().pop_spell(self.selected_item)
            self.selected_item = None
            self.Suppr_choice.setDisabled(True)
            self.refresh()
