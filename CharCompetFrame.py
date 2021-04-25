from PySide6.QtCore import SIGNAL, Slot, Qt
from PySide6.QtWidgets import (QWidget, QGridLayout, QLabel, QPushButton, QTreeWidget, QFrame, QLineEdit,
                               QPlainTextEdit, QTreeWidgetItem)

import Perso_class as Pc
import CNbk


class CharCompetFrame(QWidget):
    """ Widget to manage the competences of the character """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.selected_item = None
        self.selected_charitem = None
        self.modif_compet = None
        self.categlist = ["Lore", "Mélée", "Jet", "Combat vétéran", "Armure"]
        self.selected_compet: Pc.Competence = None

        # les compétences du personnage

        self.grid.addWidget(QLabel(self.tr("Compétences du personnage")), 0, 0)
        self.modify_choice = QPushButton(self.tr("Modifier"))
        self.modify_choice.setDisabled(True)
        self.connect(self.modify_choice, SIGNAL("clicked()"), self.modify_compet)
        self.suppr_choice = QPushButton(self.tr("Retirer"))
        self.suppr_choice.setDisabled(True)
        self.connect(self.suppr_choice, SIGNAL("clicked()"), self.suppr_compet)

        self.CharCompet_view = QTreeWidget()
        self.CharCompet_view.setMinimumHeight(300)
        self.CharCompet_view.setHeaderLabels([self.tr("Catégorie"), self.tr("Nom"), self.tr("Effet"), self.tr("Id")])
        self.CharCompet_view.hideColumn(3)

        self.grid.addWidget(self.CharCompet_view, 1, 0, 2, 5)
        self.grid.addWidget(self.modify_choice, 1, 5)
        self.grid.addWidget(self.suppr_choice, 2, 5)

        self.connect(self.CharCompet_view, SIGNAL("itemSelectionChanged()"), self.select_charcompet)

        # les compétences qui existent déjà

        self.grid.addWidget(QLabel(self.tr("Compétences disponibles")), 3, 0)
        self.transfer_choice = QPushButton(self.tr("Prendre"))
        self.transfer_choice.setDisabled(True)
        self.connect(self.transfer_choice, SIGNAL("clicked()"), self.transfer_compet)

        self.Compet_view = QTreeWidget()
        self.Compet_view.setHeaderLabels([self.tr("Catégorie"), self.tr("Nom"), self.tr("Effet"), "Id"])
        self.Compet_view.hideColumn(3)
        self.grid.addWidget(self.Compet_view, 4, 0, 1, 5)

        self.grid.addWidget(self.transfer_choice, 4, 5)

        self.connect(self.Compet_view, SIGNAL("itemSelectionChanged()"), self.select_compet)

        # widgets de modification
        separator = QFrame(self)
        separator.setFrameShape(QFrame.VLine)
        self.grid.addWidget(separator, 0, 6, 5, 1)
        self.modif_label = QLabel(self.tr("Modifications"))
        self.modif_name = QLineEdit()
        self.modif_name.setMaximumWidth(400)
        self.modif_effect = QPlainTextEdit()
        self.modif_effect.setMaximumWidth(400)
        self.modif_validate = QPushButton(self.tr("Valider"))
        self.connect(self.modif_validate, SIGNAL("clicked()"), self.modif_register)

        self.grid.addWidget(self.modif_label, 0, 7)
        self.grid.addWidget(self.modif_name, 1, 7)
        self.grid.addWidget(self.modif_effect, 2, 7)
        self.grid.addWidget(self.modif_validate, 3, 7)

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

    @Slot()
    def modify_compet(self):
        """
        Slot called when the user wants to edit a competence among those of the character

        :return: None
        """

        if self.selected_charitem is not None:
            self.modif_label.show()
            self.modif_effect.show()
            self.modif_validate.show()
            self.modif_name.show()
            self.selected_compet = self.get_selectedchar().get_competences()[self.selected_charitem]
            self.modif_name.setText(self.selected_compet.get_attr("name"))
            self.modif_effect.setPlainText(self.selected_compet.get_attr("effect"))

    @Slot()
    def modif_register(self):
        """
        Slot called to validate modifications done to the competence

        :return: None
        """
        self.selected_compet.modify(self.modif_name.text(), self.modif_effect.toPlainText())
        self.save_character()
        self.refresh_char()

    def refresh(self):
        """
        Method called to refresh everything on display

        :return: None
        """
        self.refresh_char()
        self.refresh_general()
        self.modif_label.hide()
        self.modif_effect.hide()
        self.modif_validate.hide()
        self.modif_name.hide()

    def refresh_char(self):
        """
        Method called to refresh the competences possessed by the character

        :return: None
        """

        meleelist = ["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"]
        throwlist = ["Lancer", "Arc", "Arbalète"]
        self.CharCompet_view.clear()
        itemlist = []
        for key in self.categlist:
            itemlist.append(QTreeWidgetItem([self.tr(key), "", ""]))

        for key in meleelist:
            itemlist[1].addChild(QTreeWidgetItem([self.tr(key), "", ""]))

        for key in throwlist:
            itemlist[2].addChild(QTreeWidgetItem([self.tr(key), "", ""]))

        self.CharCompet_view.addTopLevelItems(itemlist)

        competlist = self.get_selectedchar().get_competences()
        if competlist:
            i = 0
            for key in competlist:
                super_tree_item = self.CharCompet_view.findItems(self.tr(key.get_attr("categ")), Qt.MatchExactly, 0)[0]
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
        self.CharCompet_view.expandAll()

    def refresh_general(self):
        """
        Method called to refresh the TreeView displaying available competences

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

    @Slot()
    def select_charcompet(self):
        """
        Slot called when selecting a competence among the competences of the character

        :return: None
        """
        selected_items = self.CharCompet_view.selectedItems()
        if len(selected_items) == 1:
            item = selected_items[0]
            if item.text(3):
                try:
                    self.selected_charitem = int(item.text(3))
                    self.selected_compet = None
                    self.suppr_choice.setDisabled(False)
                    self.modify_choice.setDisabled(False)
                    self.modif_label.hide()
                    self.modif_effect.hide()
                    self.modif_validate.hide()
                    self.modif_name.hide()

                except ValueError:
                    self.selected_charitem = None
                    self.suppr_choice.setDisabled(True)
                    self.modify_choice.setDisabled(True)

            else:
                self.selected_charitem = None
                self.suppr_choice.setDisabled(True)
                self.modify_choice.setDisabled(True)

    @Slot()
    def select_compet(self):
        """
        Slot called when selecting a competence from the list of available competences

        :return: None
        """
        selected_items = self.Compet_view.selectedItems()
        if len(selected_items) == 1:
            item = selected_items[0]
            if item.text(3):
                try:
                    self.selected_item = int(item.text(3))
                    self.transfer_choice.setDisabled(False)

                except ValueError:
                    self.selected_item = None
                    self.transfer_choice.setDisabled(True)

            else:
                self.selected_item = None
                self.transfer_choice.setDisabled(True)

    @Slot()
    def suppr_compet(self):
        """
        Method called to remove the selected competence from the character's competences

        :return: None
        """
        if self.selected_charitem is not None:
            self.get_selectedchar().compet_suppr(self.selected_charitem)
            self.suppr_choice.setDisabled(True)
            self.modify_choice.setDisabled(True)
            self.save_character()
            self.refresh_char()

    @Slot()
    def transfer_compet(self):
        """
        Method called to give the selected competence to the selected character

        :return: None
        """
        meleelist = ["Mains nues", "Une main", "Doubles", "Deux mains", "Bouclier"]
        throwlist = ["Lancer", "Arc", "Arbalète"]

        if self.selected_item is not None:
            self.get_selectedchar().compet_add(self.get_competlist()[self.selected_item].copy())
            self.save_character()

            key = self.get_selectedchar().get_competences()[-1]
            i = len(self.get_selectedchar().get_competences()) - 1
            super_tree_item = self.CharCompet_view.findItems(self.tr(key.get_attr("categ")), Qt.MatchExactly, 0)[0]
            if key.get_attr("subcateg"):
                if key.get_attr("categ") == "Mélée":
                    tree_item = super_tree_item.child(meleelist.index(key.get_attr("subcateg")))
                else:
                    tree_item = super_tree_item.child(throwlist.index(key.get_attr("subcateg")))

                tree_item.addChild(QTreeWidgetItem(["", key.get_attr("name"), key.get_attr("effect"), str(i)]))
            else:
                super_tree_item.addChild(QTreeWidgetItem(["", key.get_attr("name"), key.get_attr("effect"), str(i)]))
