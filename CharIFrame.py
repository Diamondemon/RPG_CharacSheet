from PySide6.QtCore import SIGNAL, Slot
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QTreeWidget, QGridLayout, QFrame, QTreeWidgetItem,
                               QFileDialog)
from functools import partial
import Perso_class as Pc
from os import path
import pickle as pk

import CNbk
from ObjCreatorFrame import ObjCreatorFrame


class CharIFrame(QWidget):
    """Inventaire d'un personnage"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.Objlist = []
        self.Objitems = []
        self.Meleelist = []
        self.Meleeitems = []
        self.Throwlist = []
        self.Throwitems = []
        self.Shieldlist = []
        self.Shielditems = []
        self.Armorlist = []
        self.Armoritems = []
        self.id = None
        self.selected_item = None

        self.ObjCLabel = QLabel(self.tr("Créer un objet"))
        self.Import = QPushButton(self.tr("Importer"))
        self.connect(self.Import, SIGNAL("clicked()"), self.obj_import)
        self.ObjCF = ObjCreatorFrame()

        # tableaux d'affichage des objets --> _view
        # rester sur un objet déclenche l'affichage d'un popup d'information sur l'objet
        # un clic gauche sur une ligne d'objet permet de l'équiper/retirer/supprimer/changer son nombre

        self.Obj_view = QTreeWidget()
        self.Obj_view.setHeaderLabels([self.tr("Nom"), self.tr("Nombre"), self.tr("Id")])
        self.Obj_view.hideColumn(2)
        self.Obj_view.setColumnWidth(0, 170)
        self.Obj_view.setMinimumHeight(150)
        self.connect(self.Obj_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.options_obj)

        self.Melee_view = QTreeWidget()
        self.Melee_view.setHeaderLabels([self.tr("Nom"), self.tr("Type"), self.tr("Taille"), self.tr("Nombre"),
                                         self.tr("Id")])
        self.Melee_view.hideColumn(4)
        self.Melee_view.setColumnWidth(0, 170)
        self.Melee_view.setMinimumHeight(120)
        self.Melee_view.setMinimumWidth(500)
        self.connect(self.Melee_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.options_melee)

        self.Throw_view = QTreeWidget()
        self.Throw_view.setHeaderLabels([self.tr("Nom"), self.tr("Taille"), self.tr("Nombre"), self.tr("Id")])
        self.Throw_view.hideColumn(3)
        self.Throw_view.setColumnWidth(0, 170)
        self.Throw_view.setMinimumHeight(120)
        self.connect(self.Throw_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.options_throw)

        self.Shield_view = QTreeWidget()
        self.Shield_view.setHeaderLabels([self.tr("Nom"), self.tr("Taille"), self.tr("Nombre"), self.tr("Id")])
        self.Shield_view.hideColumn(3)
        self.Shield_view.setColumnWidth(0, 170)
        self.Shield_view.setMinimumHeight(120)
        self.connect(self.Shield_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.options_shield)

        self.Armor_view = QTreeWidget()
        self.Armor_view.setHeaderLabels([self.tr("Nom"), self.tr("Position"), self.tr("Nombre"), self.tr("Id")])
        self.Armor_view.hideColumn(3)
        self.Armor_view.setColumnWidth(0, 170)
        self.Armor_view.setMinimumHeight(120)
        self.connect(self.Armor_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.options_armor)

        # boutons pour équiper les objets, gauche/droite pour les armes; boutons pour changer les nombres/supprimer, etc

        self.Left_Cord = QPushButton(self.tr("Corder (gauche)"))
        self.Left_Cord.setDisabled(True)
        self.connect(self.Left_Cord, SIGNAL("clicked()"), partial(self.equip_cord, "left"))
        self.Right_Cord = QPushButton(self.tr("Corder (droite)"))
        self.Right_Cord.setDisabled(True)
        self.connect(self.Right_Cord, SIGNAL("clicked()"), partial(self.equip_cord, "right"))
        self.Left_Melee = QPushButton(self.tr("Equiper (gauche)"))
        self.Left_Melee.setDisabled(True)
        self.connect(self.Left_Melee, SIGNAL("clicked()"), partial(self.equip_item, "left"))
        self.Right_Melee = QPushButton(self.tr("Equiper (droite)"))
        self.Right_Melee.setDisabled(True)
        self.connect(self.Right_Melee, SIGNAL("clicked()"), partial(self.equip_item, "right"))
        self.Left_Throw = QPushButton(self.tr("Equiper (gauche)"))
        self.Left_Throw.setDisabled(True)
        self.connect(self.Left_Throw, SIGNAL("clicked()"), partial(self.equip_item, "left"))
        self.Right_Throw = QPushButton(self.tr("Equiper (droite)"))
        self.Right_Throw.setDisabled(True)
        self.connect(self.Right_Throw, SIGNAL("clicked()"), partial(self.equip_item, "right"))
        self.Left_Shield = QPushButton(self.tr("Equiper (gauche)"))
        self.Left_Shield.setDisabled(True)
        self.connect(self.Left_Shield, SIGNAL("clicked()"), partial(self.equip_item, "left"))
        self.Right_Shield = QPushButton(self.tr("Equiper (droite)"))
        self.Right_Shield.setDisabled(True)
        self.connect(self.Right_Shield, SIGNAL("clicked()"), partial(self.equip_item, "right"))
        self.Armor_Equip = QPushButton(self.tr("Equiper"))
        self.Armor_Equip.setDisabled(True)
        self.connect(self.Armor_Equip, SIGNAL("clicked()"), self.equip_item)
        self.Obj_suppr = QPushButton(self.tr("Supprimer"))
        self.Obj_suppr.setDisabled(True)
        self.connect(self.Obj_suppr, SIGNAL("clicked()"), self.suppr_obj)
        self.Obj_add = QPushButton(self.tr("+"))
        self.Obj_add.setDisabled(True)
        self.connect(self.Obj_add, SIGNAL("clicked()"), partial(self.change_number, 1))
        self.Obj_remove = QPushButton(self.tr("-"))
        self.Obj_remove.setDisabled(True)
        self.connect(self.Obj_remove, SIGNAL("clicked()"), partial(self.change_number, -1))
        self.Obj_transfer = QPushButton(self.tr("Exporter"))
        self.Obj_transfer.setDisabled(True)
        self.connect(self.Obj_transfer, SIGNAL("clicked()"), self.obj_export)
        self.Equip_remove = QPushButton(self.tr("Retirer"))
        self.Equip_remove.setDisabled(True)
        self.connect(self.Equip_remove, SIGNAL("clicked()"), self.unequip_item)
        self.Solid_add = QPushButton(self.tr("+ Sol."))
        self.Solid_add.setDisabled(True)
        self.connect(self.Solid_add, SIGNAL("clicked()"), partial(self.change_solid, 1))
        self.Solid_remove = QPushButton(self.tr("- Sol."))
        self.Solid_remove.setDisabled(True)
        self.connect(self.Solid_remove, SIGNAL("clicked()"), partial(self.change_solid, -1))

        self.grid.addWidget(self.Obj_view, 0, 0, 2, 3)
        self.grid.addWidget(self.Melee_view, 2, 0, 2, 3)
        self.grid.addWidget(self.Throw_view, 4, 0, 2, 3)
        self.grid.addWidget(self.Shield_view, 6, 0, 2, 3)
        self.grid.addWidget(self.Armor_view, 8, 0, 1, 3)

        self.grid.addWidget(self.Left_Cord, 0, 3, 1, 2)
        self.grid.addWidget(self.Right_Cord, 1, 3, 1, 2)
        self.grid.addWidget(self.Left_Melee, 2, 3, 1, 2)
        self.grid.addWidget(self.Right_Melee, 3, 3, 1, 2)
        self.grid.addWidget(self.Left_Throw, 4, 3, 1, 2)
        self.grid.addWidget(self.Right_Throw, 5, 3, 1, 2)
        self.grid.addWidget(self.Left_Shield, 6, 3, 1, 2)
        self.grid.addWidget(self.Right_Shield, 7, 3, 1, 2)
        self.grid.addWidget(self.Armor_Equip, 8, 3, 1, 2)

        self.grid.addWidget(self.Obj_suppr, 10, 2)
        self.grid.addWidget(self.Obj_add, 10, 1)
        self.grid.addWidget(self.Obj_remove, 10, 0)
        self.grid.addWidget(self.Obj_transfer, 11, 0, 1, 2)
        self.grid.addWidget(self.Equip_remove, 10, 3, 1, 2)
        self.grid.addWidget(self.Solid_add, 11, 3)
        self.grid.addWidget(self.Solid_remove, 11, 4)

        separator = QFrame(self)
        separator.setFrameShape(QFrame.VLine)
        self.grid.addWidget(separator, 0, 5, 11, 1)

        self.grid.addWidget(self.ObjCLabel, 0, 6)
        self.grid.addWidget(self.Import, 0, 7)
        self.grid.addWidget(self.ObjCF, 1, 6, 4, 2)

        self.grid.setRowStretch(8, 20)

    def change_number(self, number):
        """
        Method called to change the number of exemplaries of the selected item the character carries

        :param number: number to modify
        :return: None
        """
        selectedchar = self.get_selectedchar()
        selectedchar.change_invent_number(self.selected_item, number)
        self.refresh()
        inventory = selectedchar.get_inventory()

        # si l'objet n'est pas stackable, on change les boutons disponibles
        if inventory[self.selected_item] and not self.selected_item.get_stat("is_stackable"):
            self.Obj_add.setDisabled(True)
            self.Obj_remove.setDisabled(False)

        elif inventory[self.selected_item] and self.selected_item.is_stackable:
            self.Obj_remove.setDisabled(False)

        # si le nombre atteint 0, on enlève la posiibilité de retirer un objet
        if not inventory[self.selected_item]:
            self.Obj_remove.setDisabled(True)
            self.Obj_add.setDisabled(False)

            # si l'objet est équipé, on le déséquipe
            if self.selected_item in selectedchar.get_equipment().values():
                self.unequip_item()

        self.save_character()

    def change_solid(self, number):
        """
        Method called to manage the solidity of the selected item

        :param number: change to apply in the number
        :return: None
        """
        if self.selected_item:
            self.selected_item.upsolid(number)
            self.refresh()
            self.save_character()

    def equip_cord(self, where):
        """
        Method called to put a cord on a shooting weapon.

        :param where: side of the weapon to cord
        :return: None
        """
        selectedchar = self.get_selectedchar()
        inventory = selectedchar.get_inventory()

        left_throw = selectedchar.get_weapon("left", "throw")
        right_throw = selectedchar.get_weapon("right", "throw")

        if left_throw and left_throw.get_stat("cord"):

            # si l'arme est à 2 mains, on vérifier juste qu'on a assez de cordes pour en "corder" une de plus
            if left_throw.get_stat("hand") == 2:

                if inventory[self.selected_item] > left_throw.get_stat("cord")[0] or \
                        left_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):
                    selectedchar.get_weapon(where, "throw").load_cord(self.selected_item)

            # sinon, on vérifie si la deuxième arme existe, puis si elle a besoin d'une corde
            elif right_throw and right_throw.get_stat("cord"):

                if (left_throw.get_stat("cord")[1] ==
                    right_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc")) or (
                        left_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and
                        right_throw.get_stat("cord")[1] == 0) or (
                        right_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and
                        left_throw.get_stat("cord")[1] == 0) or (
                        left_throw.get_stat("cord")[1] == right_throw.get_stat("cord")[1] == 0):

                    if inventory[self.selected_item] > left_throw.get_stat("cord")[0] + right_throw.get_stat("cord")[0]:
                        selectedchar.get_weapon(where, "throw").load_cord(self.selected_item)

                elif (left_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and
                      right_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc")):

                    if inventory[self.selected_item] > left_throw.get_stat("cord")[0]:
                        selectedchar.get_weapon(where, "throw").load_cord(self.selected_item)

                elif right_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and \
                        left_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):

                    if inventory[self.selected_item] > right_throw.get_stat("cord")[0]:
                        selectedchar.get_weapon(where, "throw").load_cord(self.selected_item)

                else:
                    selectedchar.get_weapon(where, "throw").load_cord(self.selected_item)

            else:
                if inventory[self.selected_item] > left_throw.get_stat("cord")[0] or \
                        left_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):
                    if where == "left":
                        selectedchar.get_weapon(where, "throw").load_cord(self.selected_item)

            # sinon, on regarde pour la droite, qui est alors forcément à une main si elle existe
        elif right_throw and right_throw.get_stat("cord"):
            # si on a assez de corde pour corder à droite, on dévérouille le bouton
            if inventory[self.selected_item] > right_throw.get_stat("cord")[0] or \
                    right_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):
                if where == "right":
                    selectedchar.get_weapon(where, "throw").load_cord(self.selected_item)

        self.save_character()

    def equip_item(self, where=""):
        """
        Method called to equip the selected item

        :param where: if it is a weapon
        :return: None
        """
        # on équipe l'objet et on rafraichit le cadre qui affiche l'objet équipé.
        # Si c'est une arme, on dit de quel côté l'équiper

        if type(self.selected_item) == Pc.ArmorEquip:
            self.get_selectedchar().equip_obj(self.selected_item)
        elif type(self.selected_item) == Pc.ThrowEquip:
            self.get_selectedchar().equip_obj(self.selected_item, where)
        else:
            self.get_selectedchar().equip_obj(self.selected_item, where)

        # on peut alors déséquiper l'objet du personnage
        self.Equip_remove.setDisabled(False)
        self.save_character()

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.Player)
        """
        return self.parent().get_selectedchar()

    @Slot()
    def obj_export(self):
        """
        Slot called to export characters created to share them with other users

        :return: None
        """
        selected_item = self.selected_item.copy()

        filename = QFileDialog.getSaveFileName(self, self.tr("Sauvegarder un objet"),
                                               path.dirname(__file__) + "/Objets/" + selected_item.get_stat("name"),
                                               self.tr("Tous fichiers (*)"))

        if filename[0]:
            with open(filename[0], "wb") as fichier:
                pk.Pickler(fichier).dump(selected_item)

    @Slot()
    def obj_import(self):
        """
        Slot called to import objects created by other users

        :return: None
        """
        # on demande le fichier de personnage à importer
        filenames = QFileDialog.getOpenFileNames(self, self.tr("Choisissez des fichiers d'objets"),
                                                 path.dirname(__file__), self.tr("Tous fichiers (*)"))
        if filenames[0]:
            for filename in filenames[0]:
                with open(filename, "rb") as fichier:
                    # si le fichier importé est bien celui d'un objet, on le stocke dans l'inventaire
                    obj = pk.Unpickler(fichier).load()
                    if type(obj) in (Pc.Obj, Pc.MeleeEquip, Pc.ThrowEquip, Pc.ArmorEquip, Pc.ShieldEquip, Pc.Cord):
                        self.get_selectedchar().invent_add(obj)
            self.refresh()
            self.save_character()

    @Slot()
    def options_armor(self):
        """
        Method called to enable the adequate buttons for the selected piece of armor

        :return: None
        """
        self.unselect_previous()

        selected_items = self.Armor_view.selectedItems()
        selectedchar = self.get_selectedchar()
        if len(selected_items) == 1:
            item = selected_items[0]
            try:
                self.selected_item: Pc.ArmorEquip = self.Armorlist[int(item.text(3))]
                self.Armor_Equip.setDisabled(False)
                self.Obj_suppr.setDisabled(False)
                self.Obj_transfer.setDisabled(False)

                self.Solid_add.setDisabled(False)
                self.Solid_remove.setDisabled(False)

                if self.selected_item.get_stat("is_stackable"):
                    self.Obj_add.setDisabled(False)
                    self.Obj_remove.setDisabled(False)

                    if not selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(True)

                else:
                    if selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(False)
                    else:
                        self.Obj_add.setDisabled(False)

                if self.selected_item in selectedchar.get_equipment().values():
                    self.Equip_remove.setDisabled(False)

            except ValueError:
                self.selected_item = True
                self.unselect_previous()

    @Slot()
    def options_melee(self):
        """
        Method called to enable the adequate buttons for the selected melee weapon

        :return: None
        """
        self.unselect_previous()

        selected_items = self.Melee_view.selectedItems()
        selectedchar = self.get_selectedchar()
        if len(selected_items) == 1:
            item = selected_items[0]
            try:
                self.selected_item: Pc.MeleeEquip = self.Meleelist[int(item.text(4))]
                self.Obj_suppr.setDisabled(False)
                self.Left_Melee.setDisabled(False)
                self.Right_Melee.setDisabled(False)

                self.Obj_suppr.setDisabled(False)
                self.Obj_transfer.setDisabled(False)

                self.Solid_add.setDisabled(False)
                self.Solid_remove.setDisabled(False)

                if self.selected_item.get_stat("is_stackable"):
                    self.Obj_add.setDisabled(False)
                    self.Obj_remove.setDisabled(False)

                    if not selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(True)

                else:
                    if selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(False)
                    else:
                        self.Obj_add.setDisabled(False)

                if self.selected_item in selectedchar.get_equipment().values():
                    self.Equip_remove.setDisabled(False)

            except ValueError:
                self.selected_item = True
                self.unselect_previous()

    @Slot()
    def options_obj(self):
        """
        Method called to enable the adequate buttons for the selected item

        :return: None
        """
        self.unselect_previous()

        selected_items = self.Obj_view.selectedItems()
        selectedchar = self.get_selectedchar()
        inventory = selectedchar.get_inventory()
        if len(selected_items) == 1:
            item = selected_items[0]
            try:
                self.selected_item: Pc.Obj = self.Objlist[int(item.text(2))]
                self.Obj_suppr.setDisabled(False)
                self.Obj_transfer.setDisabled(False)

                if self.selected_item.get_stat("is_stackable"):
                    self.Obj_add.setDisabled(False)
                    self.Obj_remove.setDisabled(False)

                    if not inventory[self.selected_item]:
                        self.Obj_remove.setDisabled(True)

                else:
                    if inventory[self.selected_item]:
                        self.Obj_remove.setDisabled(False)
                    else:
                        self.Obj_add.setDisabled(False)

                # si l'objet est une corde, on dévérouille les boutons de cordage si les conditions les permettent
                if type(self.selected_item) == Pc.Cord:
                    # on commence par vérifier si l'arme de jet gauche existe, puis si elle nécessite une corde
                    left_throw: Pc.ThrowEquip = selectedchar.get_weapon("left", "throw")
                    right_throw: Pc.ThrowEquip = selectedchar.get_weapon("right", "throw")
                    if left_throw and left_throw.get_stat("cord"):
                        # si l'arme est à 2 mains, on vérifie juste qu'on a assez de cordes pour en "corder" une de plus
                        if left_throw.get_stat("hand") == 2:
                            if inventory[self.selected_item] > left_throw.get_stat("cord")[0] or \
                                    left_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):
                                self.Left_Cord.setDisabled(False)
                                self.Right_Cord.setDisabled(False)

                        # sinon, on vérifie si la deuxième arme existe, puis si elle a besoin d'une corde
                        elif right_throw and right_throw.get_stat("cord"):

                            if (left_throw.get_stat("cord")[1] == right_throw.get_stat("cord")[1] ==
                                self.selected_item.get_stat("perc")) or (
                                    left_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and
                                    right_throw.get_stat("cord")[1] == 0) or (
                                    right_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and
                                    left_throw.get_stat("cord")[1] == 0) or (
                                    left_throw.get_stat("cord")[1] == right_throw.get_stat("cord")[1] == 0):

                                if inventory[self.selected_item] > left_throw.get_stat("cord")[0] + \
                                        right_throw.get_stat("cord")[0]:
                                    self.Left_Cord.setDisabled(False)
                                    self.Right_Cord.setDisabled(False)

                            elif (left_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and
                                  right_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc")):
                                if inventory[self.selected_item] > left_throw.get_stat("cord")[0]:
                                    self.Left_Cord.setDisabled(False)
                                    self.Right_Cord.setDisabled(False)

                            elif right_throw.get_stat("cord")[1] == self.selected_item.get_stat("perc") and \
                                    left_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):
                                if inventory[self.selected_item] > right_throw.get_stat("cord")[0]:
                                    self.Left_Cord.setDisabled(False)
                                    self.Right_Cord.setDisabled(False)

                            else:
                                self.Left_Cord.setDisabled(False)
                                self.Right_Cord.setDisabled(False)

                        else:
                            if inventory[self.selected_item] > left_throw.get_stat("cord")[0] or \
                                    left_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):
                                self.Left_Cord.setDisabled(False)

                    # sinon, on regarde pour la droite, qui est alors forcément à une main si elle existe
                    elif right_throw and right_throw.get_stat("cord"):
                        # si on a assez de corde pour corder à droite, on dévérouille le bouton
                        if inventory[self.selected_item] > right_throw.get_stat("cord")[0] or \
                                right_throw.get_stat("cord")[1] != self.selected_item.get_stat("perc"):
                            self.Right_Cord.setDisabled(False)

            except ValueError:
                self.selected_item = True
                self.unselect_previous()

    @Slot()
    def options_shield(self):
        """
        Method called to enable the adequate buttons for the selected shield

        :return: None
        """
        self.unselect_previous()

        selected_items = self.Shield_view.selectedItems()
        selectedchar = self.get_selectedchar()
        if len(selected_items) == 1:
            item = selected_items[0]
            try:
                self.selected_item: Pc.ShieldEquip = self.Shieldlist[int(item.text(3))]
                self.Left_Shield.setDisabled(False)
                self.Right_Shield.setDisabled(False)
                self.Obj_suppr.setDisabled(False)
                self.Obj_transfer.setDisabled(False)

                self.Solid_add.setDisabled(False)
                self.Solid_remove.setDisabled(False)

                if self.selected_item.get_stat("is_stackable"):
                    self.Obj_add.setDisabled(False)
                    self.Obj_remove.setDisabled(False)

                    if not selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(True)

                else:
                    if selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(False)
                    else:
                        self.Obj_add.setDisabled(False)

                if self.selected_item in selectedchar.get_equipment().values():
                    self.Equip_remove.setDisabled(False)

            except ValueError:
                self.selected_item = True
                self.unselect_previous()

    @Slot()
    def options_throw(self):
        """
        Method called to enable the adequate buttons for the selected throwing weapon

        :return: None
        """
        self.unselect_previous()

        selected_items = self.Throw_view.selectedItems()
        selectedchar = self.get_selectedchar()
        if len(selected_items) == 1:
            item = selected_items[0]
            try:
                self.selected_item: Pc.ThrowEquip = self.Throwlist[int(item.text(3))]

                self.Left_Throw.setDisabled(False)
                self.Right_Throw.setDisabled(False)
                self.Obj_suppr.setDisabled(False)
                self.Obj_transfer.setDisabled(False)

                self.Solid_add.setDisabled(False)
                self.Solid_remove.setDisabled(False)

                if self.selected_item.get_stat("is_stackable"):
                    self.Obj_add.setDisabled(False)
                    self.Obj_remove.setDisabled(False)

                    if not selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(True)

                else:
                    if selectedchar.get_inventory()[self.selected_item]:
                        self.Obj_remove.setDisabled(False)
                    else:
                        self.Obj_add.setDisabled(False)

                if self.selected_item in selectedchar.get_equipment().values():
                    self.Equip_remove.setDisabled(False)

            except ValueError:
                self.selected_item = True
                self.unselect_previous()

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        return self.parentWidget().parent()

    def refresh(self):
        """
         Method called to refresh the content of the character's inventory

        :return: None
        """
        self.Obj_view.clear()
        self.Melee_view.clear()
        self.Armor_view.clear()
        self.Throw_view.clear()
        self.Shield_view.clear()
        self.Objlist = []
        self.Objitems = []
        self.Meleelist = []
        self.Meleeitems = []
        self.Throwlist = []
        self.Throwitems = []
        self.Shieldlist = []
        self.Shielditems = []
        self.Armorlist = []
        self.Armoritems = []

        selectedchar = self.get_selectedchar()
        inventory = selectedchar.get_inventory()
        for duo in enumerate(inventory.keys()):
            if type(duo[1]) == Pc.Obj or type(duo[1]) == Pc.Cord:
                index = str(len(self.Objlist))
                item: Pc.Obj = duo[1]
                self.Objlist.append(item)
                name = item.get_stat("name")
                number = str(inventory[item])
                infos_popup = item.get_stat("description")
                self.Objitems.append(QTreeWidgetItem([name, number, index]))
                self.Objitems[-1].setToolTip(0, infos_popup)
                self.Obj_view.addTopLevelItem(self.Objitems[-1])

            elif type(duo[1]) == Pc.MeleeEquip:
                index = str(len(self.Meleelist))
                item: Pc.MeleeEquip = duo[1]
                self.Meleelist.append(item)
                statlist = item.get_stats_aslist(["name", "weight", "hand"])
                number = str(inventory[item])

                labellist = {"Dgt tr": "dgt_tr", "Dgt ctd": "dgt_ctd", "Estoc": "estoc",
                             "hast": ["vit", "hast_bonus"], "Maîtr.": "mastery", "Qual.": "quality", "Sol.": "solid"}
                infos_popup = "<body><div><p>" + item.get_stat("description") + "</p>"
                infos_popup += "<p><table cellpadding='4'><tbody><tr>"

                for k in labellist:
                    if k != "hast":
                        infos_popup += '<th "align=center">' + k + "</th>"
                    else:
                        if not item.get_stat("hast"):
                            infos_popup += '<th "align=center">' + "Vit." + "</th>"
                        else:
                            infos_popup += '<th "align=center">' + "Bon.Hast" + "</th>"

                infos_popup += "</tr><tr>"

                for k, v in labellist.items():
                    if k != "hast":
                        infos_popup += '<th "align=center">' + str(item.get_stat(v)) + "</th>"
                    else:
                        if not item.get_stat("hast"):
                            infos_popup += '<th "align=center">' + str(item.get_stat(v[0])) + "</th>"
                        else:
                            infos_popup += '<th "align=center">' + str(item.get_stat(v[1])) + "</th>"

                infos_popup += "</tr></tbody></table></p></div></body>"

                self.Meleeitems.append(QTreeWidgetItem(statlist[:2]+[self.tr("%n Main(s)", "", statlist[-1]), number,
                                                                     index]))
                self.Meleeitems[-1].setToolTip(0, infos_popup)
                self.Melee_view.addTopLevelItem(self.Meleeitems[-1])

            elif type(duo[1]) == Pc.ThrowEquip:
                index = str(len(self.Throwlist))
                item: Pc.ThrowEquip = duo[1]
                self.Throwlist.append(item)
                statlist = item.get_stats_aslist(["name", "hand"])
                number = str(inventory[item])
                keylist = ["dgt", "pa", "mastery", "solid"]
                labellist = ["Dég.", "P.-Arm.", "Maîtr.", "Sol."]
                scope = item.get_stat("scope")
                infos_popup = "<body><div><p>" + item.get_stat("description") + "</p>"
                infos_popup += "<p><table cellpadding='4'><tbody><tr><th><table cellpadding='4'><tbody><tr>"

                for k in labellist:
                    infos_popup += '<th "align=center">' + k + "</th>"

                infos_popup += "</tr><tr>"

                for k in keylist:
                    infos_popup += '<th "align=center">' + str(item.get_stat(k)) + "</th>"

                infos_popup += "</tr></tbody></table></th><th><table cellpadding='4'><tbody><tr>"
                infos_popup += "<th></th><th>0</th>"
                for sublist in scope:
                    infos_popup += "<th></th><th>" + str(sublist[0]) + "</th>"
                infos_popup += "</tr><tr><th>Préc.</th><th>|</th>"
                for sublist in scope:
                    infos_popup += "<th>" + str(sublist[2]) + "</th><th>|</th>"
                infos_popup += "</tr><tr><th>Vit.</th><th>|</th>"
                for sublist in scope:
                    infos_popup += "<th>" + str(sublist[1]) + "</th><th>|</th>"
                infos_popup += "</tr></tbody></table></th></tr></tbody></table></p></div></body>"
                self.Throwitems.append(QTreeWidgetItem([statlist[0], self.tr("%n Main(s)", "", statlist[-1]),
                                                        number, index]))
                self.Throwitems[-1].setToolTip(0, infos_popup)
                self.Throw_view.addTopLevelItem(self.Throwitems[-1])
            elif type(duo[1]) == Pc.ShieldEquip:
                index = str(len(self.Shieldlist))
                item: Pc.ShieldEquip = duo[1]
                self.Shieldlist.append(item)
                statlist = item.get_stats_aslist(["name", "hand"])
                number = str(inventory[item])
                keylist = ["close", "dist", "mastery", "mobi", "vit", "quality", "solid"]
                labellist = ["Par. CàC", "Par. Dist.", "Maîtr.", "Mobi.", "Vit.", "Quali.", "Sol."]
                infos_popup = "<body><div><p>" + item.get_stat("description") + "</p>"
                infos_popup += "<p><table cellpadding='4'><tbody><tr>"

                for k in labellist:
                    infos_popup += '<th "align=center">' + k + "</th>"

                infos_popup += "</tr><tr>"

                for k in keylist:
                    infos_popup += '<th "align=center">' + str(item.get_stat(k)) + "</th>"

                infos_popup += "</tr></tbody></table></p></div></body>"
                self.Shielditems.append(QTreeWidgetItem([statlist[0], self.tr("%n Main(s)", "", statlist[-1]),
                                                        number, index]))
                self.Shielditems[-1].setToolTip(0, infos_popup)
                self.Shield_view.addTopLevelItem(self.Shielditems[-1])

            elif type(duo[1]) == Pc.ArmorEquip:
                index = str(len(self.Armorlist))
                item: Pc.ArmorEquip = duo[1]
                self.Armorlist.append(item)
                statlist = item.get_stats_aslist(["name", "location"])
                number = str(inventory[item])
                keylist = ["prot", "amort", "mobi", "vit", "solid"]
                labellist = ["Prot.", "Amort.", "Mobi.", "Vit.", "Sol."]
                infos_popup = "<body><div><p>" + item.get_stat("description") + "</p>"
                infos_popup += "<p><table cellpadding='4'><tbody><tr>"

                for k in labellist:
                    infos_popup += '<th "align=center">' + k + "</th>"

                infos_popup += "</tr><tr>"

                for k in keylist:
                    infos_popup += '<th "align=center">' + str(item.get_stat(k)) + "</th>"

                infos_popup += "</tr></tbody></table></p></div></body>"
                self.Armoritems.append(QTreeWidgetItem(statlist + [number, index]))
                self.Armoritems[-1].setToolTip(0, infos_popup)
                self.Armor_view.addTopLevelItem(self.Armoritems[-1])

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()

    def suppr_obj(self):
        """
        Method to remove the selected item from the character's inventory

        :return: None
        """
        # on retire l'objet de l'inventaire
        selectedchar = self.get_selectedchar()
        selectedchar.invent_suppr(self.selected_item)
        self.refresh()

        # si l'objet est équipé, on le déséquipe
        if self.selected_item in selectedchar.get_equipment().values():
            self.unequip_item()

        # on désélectionne l'objet, car il n'est plus censé exister
        self.unselect_previous()
        self.save_character()

    def unequip_item(self):
        """
        Method called to unequip the selected item.

        :return: None
        """
        self.get_selectedchar().unequip_obj(self.selected_item)
        self.Equip_remove.setDisabled(True)

        # on rafraîchit le cadre qui affichait l'objet déséquipé
        if type(self.selected_item) == Pc.ThrowEquip:
            self.selected_item.del_cord()
        self.save_character()

    def unselect_previous(self):
        """
        Method called to unselect any previously sleected item and disable all the buttons

        :return: None
        """
        # on désactive tous les boutons
        if self.selected_item:
            self.Obj_suppr.setDisabled(True)
            self.Obj_add.setDisabled(True)
            self.Obj_remove.setDisabled(True)
            self.Obj_transfer.setDisabled(True)
            self.Equip_remove.setDisabled(True)

            self.Solid_add.setDisabled(True)
            self.Solid_remove.setDisabled(True)

            if type(self.selected_item) == Pc.MeleeEquip:
                self.Left_Melee.setDisabled(True)
                self.Right_Melee.setDisabled(True)

            elif type(self.selected_item) == Pc.ThrowEquip:
                self.Left_Throw.setDisabled(True)
                self.Right_Throw.setDisabled(True)

            elif type(self.selected_item) == Pc.ShieldEquip:
                self.Left_Shield.setDisabled(True)
                self.Right_Shield.setDisabled(True)

            elif type(self.selected_item) == Pc.ArmorEquip:
                self.Armor_Equip.setDisabled(True)

            elif type(self.selected_item) == Pc.Cord:
                self.Left_Cord.setDisabled(True)
                self.Right_Cord.setDisabled(True)

            self.selected_item = None
