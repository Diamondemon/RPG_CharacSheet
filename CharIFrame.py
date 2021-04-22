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
        self.Meleelist = []
        self.Throwlist = []
        self.Shieldlist = []
        self.Armorlist = []
        self.id = None
        self.selected_item = None

        self.ObjCLabel = QLabel(self.tr("Créer un objet"))
        self.Import = QPushButton(self.tr("Importer"))
        self.connect(self.Import, SIGNAL("clicked()"), self.import_obj)
        self.ObjCF = ObjCreatorFrame()

        # tableaux d'affichage des objets --> _view
        # rester sur un objet déclenche l'affichage d'un popup d'information sur l'objet
        # un clic gauche sur une ligne d'objet permet de l'équiper/retirer/supprimer/changer son nombre

        self.Obj_view = QTreeWidget()
        self.Obj_view.setHeaderLabels([self.tr("Nom"), self.tr("Nombre"), self.tr("Id")])
        self.Obj_view.hideColumn(2)
        self.Obj_view.setColumnWidth(0, 170)
        self.Obj_view.setMinimumHeight(120)
        self.connect(self.Obj_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.obj_options)
        """self.Obj_pop = ObjPopup(self.Obj_view)
        self.Obj_firstindex=1
        self.Obj_view.bind("<Motion>",func=self.obj_schedule)
        self.Obj_view.bind("<Leave>",func=self.unschedule)
        self.Obj_view.bind("<Button-1>",func=self.obj_options)"""

        self.Melee_view = QTreeWidget()
        self.Melee_view.setHeaderLabels([self.tr("Nom"), self.tr("Type"), self.tr("Taille"), self.tr("Nombre"),
                                         self.tr("Id")])
        self.Melee_view.hideColumn(4)
        self.Melee_view.setColumnWidth(0, 170)
        self.Melee_view.setMinimumHeight(120)
        self.connect(self.Melee_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.melee_options)

        """self.Melee_pop=MeleePopup(self.Melee_view)
        self.Melee_firstindex=1
        self.Melee_view.bind("<Motion>",func=self.melee_schedule)
        self.Melee_view.bind("<Leave>",func=self.unschedule)
        self.Melee_view.bind("<Button-1>",func=self.melee_options)"""

        self.Throw_view = QTreeWidget()
        self.Throw_view.setHeaderLabels([self.tr("Nom"), self.tr("Taille"), self.tr("Nombre"), self.tr("Id")])
        self.Throw_view.hideColumn(3)
        self.Throw_view.setColumnWidth(0, 170)
        self.Throw_view.setMinimumHeight(120)
        self.connect(self.Throw_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.throw_options)
        """self.Throw_pop=ThrowPopup(self.Throw_view)
        self.Throw_firstindex=1
        self.Throw_view.bind("<Motion>",func=self.throw_schedule)
        self.Throw_view.bind("<Leave>",func=self.unschedule)
        self.Throw_view.bind("<Button-1>",func=self.throw_options)"""

        self.Shield_view = QTreeWidget()
        self.Shield_view.setHeaderLabels([self.tr("Nom"), self.tr("Taille"), self.tr("Nombre"), self.tr("Id")])
        self.Shield_view.hideColumn(3)
        self.Shield_view.setColumnWidth(0, 170)
        self.Shield_view.setMinimumHeight(120)
        self.connect(self.Shield_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.shield_options)
        """self.Shield_pop=ShieldPopup(self.Shield_view)
        self.Shield_firstindex=1
        self.Shield_view.bind("<Motion>",func=self.shield_schedule)
        self.Shield_view.bind("<Leave>",func=self.unschedule)
        self.Shield_view.bind("<Button-1>",func=self.shield_options)"""

        self.Armor_view = QTreeWidget()
        self.Armor_view.setHeaderLabels([self.tr("Nom"), self.tr("Position"), self.tr("Nombre"), self.tr("Id")])
        self.Armor_view.hideColumn(3)
        self.Armor_view.setColumnWidth(0, 170)
        self.Armor_view.setMinimumHeight(120)
        self.connect(self.Armor_view, SIGNAL("itemClicked(QTreeWidgetItem *, int)"), self.armor_options)
        """self.Armor_pop=ArmorPopup(self.Armor_view)
        self.Armor_firstindex=1
        self.Armor_view.bind("<Motion>",func=self.armor_schedule)
        self.Armor_view.bind("<Leave>",func=self.unschedule)
        self.Armor_view.bind("<Button-1>",func=self.armor_options)"""

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
        self.connect(self.Obj_transfer, SIGNAL("clicked()"), self.export_obj)
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
        self.Meleelist = []
        self.Throwlist = []
        self.Shieldlist = []
        self.Armorlist = []

        selectedchar = self.get_selectedchar()
        inventory = selectedchar.get_inventory()
        for duo in enumerate(inventory.keys()):
            if type(duo[1]) == Pc.Obj or type(duo[1]) == Pc.Cord:
                index = str(len(self.Objlist))
                item: Pc.Obj = duo[1]
                self.Objlist.append(item)
                name = item.get_stat("name")
                number = str(inventory[item])
                self.Obj_view.addTopLevelItem(QTreeWidgetItem([name, number, index]))

            elif type(duo[1]) == Pc.MeleeEquip:
                index = str(len(self.Meleelist))
                item: Pc.MeleeEquip = duo[1]
                self.Meleelist.append(item)
                statlist = item.get_stats_aslist(["name", "weight", "hand"])
                number = str(inventory[item])
                self.Melee_view.addTopLevelItem(QTreeWidgetItem(statlist[:2]+[self.tr("%n Main(s)", "", statlist[-1]),
                                                                              number, index]))
            elif type(duo[1]) == Pc.ThrowEquip:
                index = str(len(self.Throwlist))
                item: Pc.ThrowEquip = duo[1]
                self.Throwlist.append(item)
                statlist = item.get_stats_aslist(["name", "hand"])
                number = str(inventory[item])
                self.Throw_view.addTopLevelItem(QTreeWidgetItem([statlist[0], self.tr("%n Main(s)", "", statlist[-1]),
                                                                 number, index]))
            elif type(duo[1]) == Pc.ShieldEquip:
                index = str(len(self.Shieldlist))
                item: Pc.ShieldEquip = duo[1]
                self.Shieldlist.append(item)
                statlist = item.get_stats_aslist(["name", "hand"])
                number = str(inventory[item])
                self.Shield_view.addTopLevelItem(QTreeWidgetItem([statlist[0], self.tr("%n Main(s)", "", statlist[-1]),
                                                                  number, index]))

            elif type(duo[1]) == Pc.ArmorEquip:
                index = str(len(self.Armorlist))
                item: Pc.ArmorEquip = duo[1]
                self.Armorlist.append(item)
                statlist = item.get_stats_aslist(["name", "location"])
                number = str(inventory[item])
                self.Armor_view.addTopLevelItem(QTreeWidgetItem(statlist + [number, index]))

    # les popups n'apparaissent que si la souris ne bouge pas
    def obj_schedule(self):
        """
        "" Prépare à l'affichage du popup pour l'objet ""
        self.unschedule()
        if self.Obj_view.identify_row(event.y):
            self.id=self.after("500",self.Obj_pop.showinfo,self.Objlist[int(self.Obj_view.identify_row(event.y)[1:],base=16)-self.Obj_firstindex],event)
        """

    def melee_schedule(self):
        """
        ""Prépare à l'affichage du popup pour l'arme de mélée ""
        self.unschedule()
        if self.Melee_view.identify_row(event.y):
            self.id=self.after("500",self.Melee_pop.showinfo,self.Meleelist[int(self.Melee_view.identify_row(event.y)[1:],base=16)-self.Melee_firstindex],event)"""

    def throw_schedule(self):
        """
        ""Prépare à l'affichage du popup pour l'arme de jet ""
        self.unschedule()
        if self.Throw_view.identify_row(event.y):
            self.id=self.after("500",self.Throw_pop.showinfo,self.Throwlist[int(self.Throw_view.identify_row(event.y)[1:],base=16)-self.Throw_firstindex],event)"""

    def shield_schedule(self):
        """
        "" Prépare à l'affichage du popup pour le bouclier ""
        self.unschedule()
        if self.Shield_view.identify_row(event.y):
            self.id=self.after("500",self.Shield_pop.showinfo,self.Shieldlist[int(self.Shield_view.identify_row(event.y)[1:],base=16)-self.Shield_firstindex],event)"""

    def armor_schedule(self):
        """
        "" Prépare à l'affichage du popup pour l'armure ""
        self.unschedule()
        if self.Armor_view.identify_row(event.y):
            self.id=self.after("500",self.Armor_pop.showinfo,self.Armorlist[int(self.Armor_view.identify_row(event.y)[1:],base=16)-self.Armor_firstindex],event)
        """

    def unschedule(self):
        """
        "" Arrête l'attente pour afficher le popup, et efface le popup s'il est présent ""
        if self.id:
            self.after_cancel(self.id)
            self.id = None
        self.Obj_pop.hideinfo()
        self.Melee_pop.hideinfo()
        self.Throw_pop.hideinfo()
        self.Shield_pop.hideinfo()
        self.Armor_pop.hideinfo()
        """

    def unselect_previous(self):
        """ Désélectionne l'item précédent """

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

    @Slot()
    def obj_options(self):
        self.unselect_previous()

        selected_items = self.Obj_view.selectedItems()
        selectedchar = self.get_selectedchar()
        inventory = selectedchar.get_inventory()
        if len(selected_items) == 1:
            item = selected_items[0]
            try:
                self.selected_item: Pc.Obj = self.Objlist[int(item.text(4))]
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
    def melee_options(self):
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
        """
        "" fonction qui affiche les boutons adéquats à l'objet sélectionné ""
        """

    @Slot()
    def throw_options(self):
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

    @Slot()
    def shield_options(self):
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
    def armor_options(self):
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
        """
        "" fonction qui affiche les boutons adéquats à l'objet sélectionné ""
        """

    def import_obj(self):
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
                    if type(obj) in (Pc.Obj, Pc.MeleeEquip, Pc.ThrowEquip, Pc.ArmorEquip, Pc.ShieldEquip):
                        self.get_selectedchar().invent_add(obj)
            self.refresh()

    @Slot()
    def export_obj(self):
        """
        Slot called to export characters created to share them with other users

        :return: None
        """
        selected_item = self.selected_item.copy()
        if type(self.selected_item) == Pc.ThrowEquip:
            selected_item.del_cord()

        filename = QFileDialog.getSaveFileName(self, self.tr("Sauvegarder un objet"),
                                               path.dirname(__file__) + "/Objets/" + selected_item.get_stat("name"),
                                               self.tr("Tous fichiers (*)"))

        if filename[0]:
            with open(filename[0], "wb") as fichier:
                pk.Pickler(fichier).dump(selected_item)

    def change_number(self, number):
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
        """
        "" fonction pour changer le nombre d'instances d'un objet dans l'inventaire ""
        """

    def suppr_obj(self):
        # on retire l'objet de l'inventaire
        selectedchar = self.get_selectedchar()
        selectedchar.invent_suppr(self.selected_item)
        self.refresh()

        # si l'objet est équipé, on le déséquipe
        if self.selected_item in selectedchar.get_equipment().values():
            self.unequip_item()

        # on désélectionne l'objet, car il n'est plus censé exister
        self.unselect_previous()

    def equip_item(self, where=""):
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

    def unequip_item(self):
        self.get_selectedchar().unequip_obj(self.selected_item)
        self.Equip_remove.setDisabled(True)

        # on rafraîchit le cadre qui affichait l'objet déséquipé
        if type(self.selected_item) == Pc.ThrowEquip:
            self.selected_item.del_cord()
        """
        "" fonction pour déséquiper l'objet sélectionné ""
        """

    def equip_cord(self, where):
        """
        "" fonction pour équiper une corde sur un arc/ une arbalète ""
        if self.master.master.selectedchar.playerequipment["left_throw"] and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
            # si l'arme est à 2 mains, on vérifier juste qu'on a assez de cordes pour en "corder" une de plus
            if self.master.master.selectedchar.playerequipment["left_throw"].carac["hand"]==2:
                if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                    self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

            # sinon, on vérifie si la deuxième arme existe, puis si elle a besoin d'une corde
            elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:

                if (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0):
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]+self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

                elif (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc):
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]:
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

                elif self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

                else:
                    self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                    if where == "left":
                        self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)


        # sinon, on regarde pour la droite, qui est alors forcément à une main si elle existe
        elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
            # si on a assez de corde pour corder à droite, on dévérouille le bouton
            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc:
                if where == "right":
                    self.master.master.selectedchar.playerequipment[where+"_throw"].load_cord(self.selected_item)"""

    def change_solid(self, number):
        if self.selected_item:
            self.selected_item.upsolid(number)
            self.refresh()

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
