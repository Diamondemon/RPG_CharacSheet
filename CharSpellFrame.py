from PySide6.QtCore import SIGNAL, Qt, Slot
from PySide6.QtGui import QIntValidator, QIcon
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QTreeWidget, QFrame, QComboBox, QLineEdit, \
    QPlainTextEdit, QTreeWidgetItem
from functools import partial
import CNbk
import Perso_class as Pc


class CharSpellFrame(QWidget):
    """ Widget to display and manage the spells of a mage character"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.selected_item = None
        self.selected_charitem = None
        self.spells_list = []

        self.elemlist = ["Foudre"]
        self.subcateglist = ["Emprise", "Appel", "Altération", "Transfert", "Divination", "Lien"]

        self.lightning_image = QIcon("./Images/symb-lightning.svg")

        self.grid.addWidget(QLabel(self.tr("Sorts du personnage")), 0, 0)
        self.plus_lightning = QPushButton(self.tr("+"))
        self.plus_lightning.setDisabled(True)
        self.plus_lightning.setIcon(self.lightning_image)
        self.connect(self.plus_lightning, SIGNAL("clicked()"), partial(self.modif_lightning, 1))
        self.grid.addWidget(self.plus_lightning, 1, 6)
        self.min_lightning = QPushButton(self.tr("-"))
        self.min_lightning.setDisabled(True)
        self.min_lightning.setIcon(self.lightning_image)
        self.connect(self.min_lightning, SIGNAL("clicked()"), partial(self.modif_lightning, -1))
        self.grid.addWidget(self.min_lightning, 1, 7)
        self.remove_choice = QPushButton(self.tr("Retirer"))
        self.remove_choice.setDisabled(True)
        self.connect(self.remove_choice, SIGNAL("clicked()"), self.remove_charspell)
        self.grid.addWidget(self.remove_choice, 2, 6, 1, 2)

        # les sorts que le personnage a déjà
        self.CharSpell_view = QTreeWidget()
        self.CharSpell_view.setHeaderLabels(["", self.tr("Effet"), self.tr("Description"), self.tr("Coût"), "", "Id"])
        self.CharSpell_view.headerItem().setIcon(4, self.lightning_image)
        self.CharSpell_view.hideColumn(5)
        self.connect(self.CharSpell_view, SIGNAL("itemSelectionChanged()"), self.select_charspell)

        self.grid.addWidget(self.CharSpell_view, 1, 0, 3, 5)

        self.grid.addWidget(QLabel(self.tr("Sorts disponibles")), 4, 0)
        self.transfer_choice = QPushButton(self.tr("Prendre"))
        self.transfer_choice.setDisabled(True)
        self.connect(self.transfer_choice, SIGNAL("clicked()"), self.transfer_spell)
        self.grid.addWidget(self.transfer_choice, 5, 6, 1, 2)

        # les sorts qui existent
        self.Spell_view = QTreeWidget()
        self.Spell_view.setHeaderLabels(["", self.tr("Effet"), self.tr("Description"), self.tr("Coût"), "Id"])
        self.Spell_view.hideColumn(4)
        self.connect(self.Spell_view, SIGNAL("itemSelectionChanged()"), self.select_spell)

        self.grid.addWidget(self.Spell_view, 5, 0, 1, 5)

        # la FUUUU-SIOOOON de sorts

        separator = QFrame(self)
        separator.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator, 6, 0, 1, 8)

        self.grid.addWidget(QLabel(self.tr("Sort spécial")), 7, 0)
        self.grid.addWidget(QLabel(self.tr("Elément")), 8, 0)
        self.grid.addWidget(QLabel(self.tr("Sous-catégorie")), 8, 1)
        self.grid.addWidget(QLabel(self.tr("Nom")), 8, 2)
        self.grid.addWidget(QLabel(self.tr("Coût")), 8, 3)
        self.grid.addWidget(QLabel(self.tr("Effets")), 10, 0)
        self.grid.addWidget(QLabel(self.tr("Description")), 10, 2)

        self.Elem_entry = QComboBox()
        for elem in self.elemlist:
            self.Elem_entry.addItem(self.tr(elem))
        self.Elem_entry.setEditable(False)
        self.Elem_entry.setCurrentIndex(0)
        self.Subcateg_entry = QComboBox()
        for subcateg in self.subcateglist:
            self.Subcateg_entry.addItem(self.tr(subcateg))
        self.Subcateg_entry.setEditable(False)
        self.Subcateg_entry.setCurrentIndex(0)

        self.Name_entry = QLineEdit()
        self.Cost_entry = QLineEdit()
        self.Cost_entry.setValidator(QIntValidator(0, 9999, self))
        self.Effect_entry = QPlainTextEdit()
        self.Description_entry = QPlainTextEdit()

        self.Special_register = QPushButton(self.tr("Enregistrer"))
        self.Special_register.setDisabled(True)
        self.connect(self.Special_register, SIGNAL("clicked()"), self.special_create)

        self.grid.addWidget(self.Elem_entry, 9, 0)
        self.grid.addWidget(self.Subcateg_entry, 9, 1)
        self.grid.addWidget(self.Name_entry, 9, 2)
        self.grid.addWidget(self.Cost_entry, 9, 3)
        self.grid.addWidget(self.Effect_entry, 11, 0, 1, 2)
        self.grid.addWidget(self.Description_entry, 11, 2, 1, 2)
        self.grid.addWidget(self.Special_register, 9, 4)

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.Player)
        """
        return self.parent().get_selectedchar()

    def get_spelllist(self):
        """
        Method called to get the available spells

        :return: Reference to the list of spells
        """
        return self.parent().get_spelllist()

    @Slot()
    def modif_lightning(self, number):
        """
        Method called to consume lightnings

        :param number: change to apply
        :return: None
        """
        if self.selected_charitem is not None:
            print(self.spells_list)
            print(self.selected_charitem)
            selected_spell = self.spells_list[self.selected_charitem]
            self.get_selectedchar().use_lightning(selected_spell, number)
            self.save_character()
            self.refresh_char()

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        return self.parentWidget().parent()

    def refresh(self):
        """
        Method called to refresh everything

        :return: None
        """
        self.refresh_general()
        self.refresh_char()
        self.remove_choice.setDisabled(True)
        self.transfer_choice.setDisabled(True)
        self.plus_lightning.setDisabled(True)
        self.min_lightning.setDisabled(True)

    def refresh_char(self):
        """
        Method called to refresh the list of spells of the character

        :return: None
        """
        self.CharSpell_view.clear()
        itemlist = []
        for key in self.elemlist:
            itemlist.append(QTreeWidgetItem([self.tr(key)]))

        for key in self.subcateglist:
            for i in enumerate(itemlist):
                i[1].addChild(QTreeWidgetItem([self.tr(key)]))

        self.CharSpell_view.addTopLevelItems(itemlist)

        self.spells_list = list(self.get_selectedchar().get_spelllist())
        selectedchar = self.get_selectedchar()
        if self.spells_list:
            i = 0
            for key in self.spells_list:
                super_tree_item = self.CharSpell_view.findItems(self.tr(key.get_stat("elem")), Qt.MatchExactly, 0)[0]
                tree_item = super_tree_item.child(self.subcateglist.index(key.get_stat("subcateg")))
                tree_item.addChild(QTreeWidgetItem(key.get_stats_aslist(["name", "effect", "description"]) +
                                                   [str(key.get_stat("cost")), str(selectedchar.get_lightnings(key)),
                                                   str(i)]))
                i += 1

        self.CharSpell_view.expandAll()

    def refresh_general(self):
        """
        Method called to refresh the list of available spells displayed

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
                tree_item.addChild(QTreeWidgetItem(key.get_stats_aslist(["name", "effect", "description"]) +
                                                   [str(key.get_stat("cost")), str(i)]))
                i += 1

        self.Spell_view.expandAll()

    @Slot()
    def remove_charspell(self):
        """
        Method called to remove the selected spell from the character's spells

        :return: None
        """
        if self.selected_charitem is not None:
            self.get_selectedchar().spell_pop(self.spells_list[self.selected_charitem])
            self.save_character()
            self.refresh_char()
            self.selected_charitem = None
            self.remove_choice.setDisabled(True)

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()

    @Slot()
    def select_charspell(self):
        """
        Slot called when a spell of the character is selected, to delete it if needed

        :return: None
        """
        selected_items = self.CharSpell_view.selectedItems()
        if len(selected_items) == 1:
            item = selected_items[0]
            if item.text(5):
                try:
                    self.selected_charitem = int(item.text(5))
                    self.remove_choice.setDisabled(False)
                    self.plus_lightning.setDisabled(False)
                    self.min_lightning.setDisabled(False)

                except ValueError:
                    self.selected_charitem = None
                    self.remove_choice.setDisabled(True)
                    self.plus_lightning.setDisabled(True)
                    self.min_lightning.setDisabled(True)

            else:
                self.selected_charitem = None
                self.remove_choice.setDisabled(True)
                self.plus_lightning.setDisabled(True)
                self.min_lightning.setDisabled(True)

    @Slot()
    def select_spell(self):
        """
        Slot called when a spell is selected, to delete it if needed

        :return: None
        """
        selected_items = self.Spell_view.selectedItems()
        if len(selected_items) == 1:
            item = selected_items[0]
            if item.text(4):
                try:
                    self.selected_item = int(item.text(4))
                    self.transfer_choice.setDisabled(False)

                except ValueError:
                    self.selected_item = None
                    self.transfer_choice.setDisabled(True)

            else:
                self.selected_item = None
                self.transfer_choice.setDisabled(True)

    @Slot()
    def special_create(self):
        """
        Method called to create a spell specific to the character

        :return: None
        """
        if self.Name_entry.text() and self.Cost_entry.text():
            elem = self.elemlist[self.Elem_entry.currentIndex()]
            subcateg = self.subcateglist[self.Subcateg_entry.currentIndex()]
            new_spell = Pc.Spell(elem, subcateg, self.Name_entry.text(),
                                 self.Effect_entry.toPlainText(), self.Description_entry.toPlainText(),
                                 int(self.Cost_entry.text()))
            self.get_selectedchar().spell_add(new_spell)

            self.spells_list.append(new_spell)
            i = len(self.spells_list) - 1
            super_tree_item = self.CharSpell_view.findItems(self.tr(new_spell.get_stat("elem")), Qt.MatchExactly, 0)[0]
            tree_item = super_tree_item.child(self.subcateglist.index(new_spell.get_stat("subcateg")))
            tree_item.addChild(QTreeWidgetItem(new_spell.get_stats_aslist(["name", "effect", "description"]) +
                                               [str(new_spell.get_stat("cost")),
                                                str(self.get_selectedchar().get_lightnings(new_spell)), str(i)]))

    @Slot()
    def transfer_spell(self):
        """
        Method called to give the selected spell to the character

        :return: None
        """
        if self.selected_item is not None:
            new_spell = self.get_spelllist()[self.selected_item].copy()
            self.get_selectedchar().spell_add(new_spell)
            self.save_character()
            self.spells_list.append(new_spell)
            i = len(self.spells_list) - 1
            super_tree_item = self.CharSpell_view.findItems(self.tr(new_spell.get_stat("elem")), Qt.MatchExactly, 0)[0]
            tree_item = super_tree_item.child(self.subcateglist.index(new_spell.get_stat("subcateg")))
            tree_item.addChild(QTreeWidgetItem(new_spell.get_stats_aslist(["name", "effect", "description"]) +
                                               [str(new_spell.get_stat("cost")),
                                                str(self.get_selectedchar().get_lightnings(new_spell)), str(i)]))
