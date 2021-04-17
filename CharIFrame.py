from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLabel, QPushButton, QTreeWidget, QGridLayout, QFrame)
from functools import partial

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
        self.Obj_view.setHeaderLabels([self.tr("Nom"), self.tr("Nombre")])
        """self.Obj_pop = ObjPopup(self.Obj_view)
        self.Obj_firstindex=1
        self.Obj_view.bind("<Motion>",func=self.obj_schedule)
        self.Obj_view.bind("<Leave>",func=self.unschedule)
        self.Obj_view.bind("<Button-1>",func=self.obj_options)"""

        self.Melee_view = QTreeWidget()
        self.Melee_view.setHeaderLabels([self.tr("Nom"), self.tr("Type"), self.tr("Taille"), self.tr("Nombre")])
        """self.Melee_pop=MeleePopup(self.Melee_view)
        self.Melee_firstindex=1
        self.Melee_view.bind("<Motion>",func=self.melee_schedule)
        self.Melee_view.bind("<Leave>",func=self.unschedule)
        self.Melee_view.bind("<Button-1>",func=self.melee_options)"""

        self.Throw_view = QTreeWidget()
        self.Throw_view.setHeaderLabels([self.tr("Nom"), self.tr("Taille"), self.tr("Nombre")])
        """self.Throw_pop=ThrowPopup(self.Throw_view)
        self.Throw_firstindex=1
        self.Throw_view.bind("<Motion>",func=self.throw_schedule)
        self.Throw_view.bind("<Leave>",func=self.unschedule)
        self.Throw_view.bind("<Button-1>",func=self.throw_options)"""

        self.Shield_view = QTreeWidget()
        self.Shield_view.setHeaderLabels([self.tr("Nom"), self.tr("Taille"), self.tr("Nombre")])
        """self.Shield_pop=ShieldPopup(self.Shield_view)
        self.Shield_firstindex=1
        self.Shield_view.bind("<Motion>",func=self.shield_schedule)
        self.Shield_view.bind("<Leave>",func=self.unschedule)
        self.Shield_view.bind("<Button-1>",func=self.shield_options)"""

        self.Armor_view = QTreeWidget()
        self.Armor_view.setHeaderLabels([self.tr("Nom"), self.tr("Position"), self.tr("Nombre")])
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
        self.grid.addWidget(self.Armor_view, 8, 0, 2, 3)

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

    def refresh(self, event=None):
        """
        "" fonction qui rafraîchit l'inventaire ""
        # self.master.master.selectedchar.inventory={}
        self.Objlist=[]
        self.Meleelist=[]
        self.Throwlist=[]
        self.Shieldlist=[]
        self.Armorlist=[]

        # on supprime tout l'affichage dans chaque tableau
        for item in self.Obj_view.get_children():
            self.Obj_view.delete(item)

        for item in self.Melee_view.get_children():
            self.Melee_view.delete(item)

        for item in self.Throw_view.get_children():
            self.Throw_view.delete(item)

        for item in self.Shield_view.get_children():
            self.Shield_view.delete(item)

        for item in self.Armor_view.get_children():
            self.Armor_view.delete(item)

        # on reprend la liste complète des objets dans l'inventaire et on les trie par type, puis on les affiche
        for i in self.master.master.selectedchar.inventory.keys():
            if type(i)==pc.Obj or type(i)==pc.Cord:
                self.Obj_view.insert("","end",text=i.name,values=[self.master.master.selectedchar.inventory[i]])
                self.Objlist.append(i)

            elif type(i)==pc.MeleeEquip:
                self.Melee_view.insert("","end",text=i.name,values=[i.carac["weight"],str(i.carac["hand"])+" Main(s)",self.master.master.selectedchar.inventory[i]])
                self.Meleelist.append(i)

            elif type(i)==pc.ThrowEquip:
                self.Throw_view.insert("","end",text=i.name,values=[str(i.carac["hand"])+" Main(s)",self.master.master.selectedchar.inventory[i]])
                self.Throwlist.append(i)

            elif type(i)==pc.ShieldEquip:
                self.Shield_view.insert("","end",text=i.name,values=[str(i.carac["hand"])+" Main(s)",self.master.master.selectedchar.inventory[i]])
                self.Shieldlist.append(i)

            elif type(i)==pc.ArmorEquip:
                self.Armor_view.insert("","end",text=i.name,values=[i.location,self.master.master.selectedchar.inventory[i]])
                self.Armorlist.append(i)


        # si des objets sont affichés dans les tableaux, on regarde quel est l'indice le plus bas donné aux objets
        if self.Obj_view.get_children():
            self.Obj_firstindex=int(self.Obj_view.get_children()[0][1:],base=16)

        if self.Melee_view.get_children():
            self.Melee_firstindex=int(self.Melee_view.get_children()[0][1:],base=16)

        if self.Throw_view.get_children():
            self.Throw_firstindex=int(self.Throw_view.get_children()[0][1:],base=16)

        if self.Shield_view.get_children():
            self.Shield_firstindex=int(self.Shield_view.get_children()[0][1:],base=16)

        if self.Armor_view.get_children():
            self.Armor_firstindex=int(self.Armor_view.get_children()[0][1:],base=16)


    # les popups n'apparaissent que si la souris ne bouge pas
    def obj_schedule(self,event=None):
        "" Prépare à l'affichage du popup pour l'objet ""
        self.unschedule()
        if self.Obj_view.identify_row(event.y):
            self.id=self.after("500",self.Obj_pop.showinfo,self.Objlist[int(self.Obj_view.identify_row(event.y)[1:],base=16)-self.Obj_firstindex],event)"""


    def melee_schedule(self,event=None):
        """
        ""Prépare à l'affichage du popup pour l'arme de mélée ""
        self.unschedule()
        if self.Melee_view.identify_row(event.y):
            self.id=self.after("500",self.Melee_pop.showinfo,self.Meleelist[int(self.Melee_view.identify_row(event.y)[1:],base=16)-self.Melee_firstindex],event)"""


    def throw_schedule(self,event=None):
        """
        ""Prépare à l'affichage du popup pour l'arme de jet ""
        self.unschedule()
        if self.Throw_view.identify_row(event.y):
            self.id=self.after("500",self.Throw_pop.showinfo,self.Throwlist[int(self.Throw_view.identify_row(event.y)[1:],base=16)-self.Throw_firstindex],event)"""


    def shield_schedule(self,event=None):
        """
        "" Prépare à l'affichage du popup pour le bouclier ""
        self.unschedule()
        if self.Shield_view.identify_row(event.y):
            self.id=self.after("500",self.Shield_pop.showinfo,self.Shieldlist[int(self.Shield_view.identify_row(event.y)[1:],base=16)-self.Shield_firstindex],event)"""


    def armor_schedule(self,event=None):
        """
        "" Prépare à l'affichage du popup pour l'armure ""
        self.unschedule()
        if self.Armor_view.identify_row(event.y):
            self.id=self.after("500",self.Armor_pop.showinfo,self.Armorlist[int(self.Armor_view.identify_row(event.y)[1:],base=16)-self.Armor_firstindex],event)
        """

    def unschedule(self,event=None):
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
        """
        "" Désélectionne l'item précédent ""

        # on désactive tous les boutons
        if self.selected_item:
            self.Obj_suppr["state"]="disabled"
            self.Obj_add["state"]="disabled"
            self.Obj_remove["state"]="disabled"
            self.Obj_transfer["state"]="disabled"
            self.Equip_remove["state"]="disabled"

            self.Solid_add["state"]="disabled"
            self.Solid_remove["state"]="disabled"


            if type(self.selected_item)==pc.MeleeEquip:
                self.Left_Melee["state"]="disabled"
                self.Right_Melee["state"]="disabled"

            elif type(self.selected_item)==pc.ThrowEquip:
                self.Left_Throw["state"]="disabled"
                self.Right_Throw["state"]="disabled"

            elif type(self.selected_item)==pc.ShieldEquip:
                self.Left_Shield["state"]="disabled"
                self.Right_Shield["state"]="disabled"

            elif type(self.selected_item)==pc.ArmorEquip:
                self.Armor_Equip["state"]="disabled"

            elif type(self.selected_item)==pc.Cord:
                self.Left_Cord["state"]="disabled"
                self.Right_Cord["state"]="disabled"

            self.selected_item=None
            """

    def obj_options(self,event=None):
        """
        "" fonction qui affiche les boutons adéquats à l'objet sélectionné ""

        self.unselect_previous()

        if self.Obj_view.identify_row(event.y):
            self.selected_item=self.Objlist[int(self.Obj_view.identify_row(event.y)[1:],base=16)-self.Obj_firstindex]
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            # si l'objet est une corde, on dévérouille les boutons de cordage si les conditions les permettent
            if type(self.selected_item)==pc.Cord:
                # on commence par vérifier si l'arme de jet gauche existe, puis si elle nécessite une corde
                if self.master.master.selectedchar.playerequipment["left_throw"] and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                    # si l'arme est à 2 mains, on vérifier juste qu'on a assez de cordes pour en "corder" une de plus
                    if self.master.master.selectedchar.playerequipment["left_throw"].carac["hand"]==2:
                        if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                            self.Left_Cord["state"]="normal"
                            self.Right_Cord["state"]="normal"
                    # sinon, on vérifie si la deuxième arme existe, puis si elle a besoin d'une corde
                    elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:

                        if (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==0) or (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==0):
                            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]+self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                                self.Left_Cord["state"]="normal"
                                self.Right_Cord["state"]="normal"

                        elif (self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc):
                            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["left_throw"].carac["cord"][0]:
                                self.Left_Cord["state"]="normal"
                                self.Right_Cord["state"]="normal"

                        elif self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]==self.selected_item.perc and self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                            if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerquipment["right_throw"].carac["cord"][0]:
                                self.Left_Cord["state"]="normal"
                                self.Right_Cord["state"]="normal"

                        else:
                            self.Left_Cord["state"]="normal"
                            self.Right_Cord["state"]="normal"

                    else:
                        if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][1]!=self.selected_item.perc:
                            self.Left_Cord["state"]="normal"


                # sinon, on regarde pour la droite, qui est alors forcément à une main si elle existe
                elif self.master.master.selectedchar.playerequipment["right_throw"] and self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                    # si on a assez de corde pour corder à droite, on dévérouille le bouton
                    if self.master.master.selectedchar.inventory[self.selected_item]>self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][0] or self.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][1]!=self.selected_item.perc:
                        self.Right_Cord["state"]="normal"
        """


    def melee_options(self,event=None):
        """
        "" fonction qui affiche les boutons adéquats à l'objet sélectionné ""

        self.unselect_previous()

        if self.Melee_view.identify_row(event.y):
            self.selected_item=self.Meleelist[int(self.Melee_view.identify_row(event.y)[1:],base=16)-self.Melee_firstindex]
            self.Left_Melee["state"]="normal"
            self.Right_Melee["state"]="normal"

            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"
        """

    def throw_options(self,event=None):
        """
        "" fonction qui affiche les boutons adéquats à l'objet sélectionné ""

        self.unselect_previous()

        if self.Throw_view.identify_row(event.y):
            self.selected_item=self.Throwlist[int(self.Throw_view.identify_row(event.y)[1:],base=16)-self.Throw_firstindex]
            self.Left_Throw["state"]="normal"
            self.Right_Throw["state"]="normal"
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"
        """



    def shield_options(self,event=None):
        """
        "" fonction qui affiche les boutons adéquats à l'objet sélectionné ""

        self.unselect_previous()

        if self.Shield_view.identify_row(event.y):
            self.selected_item=self.Shieldlist[int(self.Shield_view.identify_row(event.y)[1:],base=16)-self.Shield_firstindex]
            self.Left_Shield["state"]="normal"
            self.Right_Shield["state"]="normal"
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"
        """


    def armor_options(self,event=None):
        """
        "" fonction qui affiche les boutons adéquats à l'objet sélectionné ""

        self.unselect_previous()

        if self.Armor_view.identify_row(event.y):
            self.selected_item=self.Armorlist[int(self.Armor_view.identify_row(event.y)[1:],base=16)-self.Armor_firstindex]
            self.Armor_Equip["state"]="normal"
            self.Obj_suppr["state"]="normal"
            self.Obj_transfer["state"]="normal"

            self.Solid_add["state"]="normal"
            self.Solid_remove["state"]="normal"

            if self.selected_item.is_stackable:
                self.Obj_add["state"]="normal"
                self.Obj_remove["state"]="normal"

                if not self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="disabled"

            else:
                if self.master.master.selectedchar.inventory[self.selected_item]:
                    self.Obj_remove["state"]="normal"
                else:
                    self.Obj_add["state"]="normal"

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.Equip_remove["state"]="normal"
        """

    def import_obj(self):
        """
        "" Fonction pour équiper un objet venant des fichier""
        # on demande le fichier d'équipement à importer
        filenames=askopenfilenames(title="Choisissez le fichier d'objet",filetypes=[],initialdir=path.dirname(__file__))

        if filenames:
            for filename in filenames:
                with open(filename,"rb") as fichier:
                    # si le fichier importé est bien celui d'un objet, on le stocke dans l'inventaire
                    obj=pk.Unpickler(fichier).load()
                    if type(obj) in (pc.Obj,pc.MeleeEquip,pc.ThrowEquip,pc.ArmorEquip,pc.ShieldEquip):
                        self.master.master.selectedchar.inventory[obj]=1
            self.refresh()
        """

    def export_obj(self):
        """
        "" fonction pour exporter un objet de l'inventaire ""
        # on demande le nom d'exoprtation du importer
        filename=asksaveasfilename(title="Enregistrez l'objet",filetypes=[],defaultextension=[],initialfile=[self.selected_item.name],initialdir=path.dirname(__file__))

        selected_item = self.selected_item.copy()

        if type(self.selected_item)==pc.ThrowEquip:
            selected_item.del_cord()

        if filename:
            with open(filename,"wb") as fichier:
                pk.Pickler(fichier).dump(selected_item)
        """

    def change_number(self,number):
        """
        "" fonction pour changer le nombre d'instances d'un objet dans l'inventaire ""
        self.master.master.selectedchar.change_invent_number(self.selected_item,number)
        self.refresh()

        # si l'objet n'est pas stackable, on change les boutons disponibles
        if self.master.master.selectedchar.inventory[self.selected_item] and not self.selected_item.is_stackable:
            self.Obj_add["state"]="disabled"
            self.Obj_remove["state"]="normal"

        elif self.master.master.selectedchar.inventory[self.selected_item] and self.selected_item.is_stackable:
            self.Obj_remove["state"]="normal"

        # si le nombre atteint 0, on enlève la posiibilité de retirer un objet
        if not self.master.master.selectedchar.inventory[self.selected_item]:
            self.Obj_remove["state"]="disabled"
            self.Obj_add["state"]="normal"

            # si l'objet est équipé, on le déséquipe
            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.unequip_item()
        """

    def suppr_obj(self):
        """
        "" fonction pour supprimer un objet de l'inventaire ""
        # on retire l'objet de l'inventaire
        self.master.master.selectedchar.invent_suppr(self.selected_item)
        self.refresh()

        # si l'objet est équipé, on le déséquipe
        if self.selected_item in self.master.master.selectedchar.playerequipment.values():
            self.unequip_item()

        # on désélectionne l'objet, car il n'est plus censé exister
        self.unselect_previous()
        """

    def equip_item(self,where=""):
        """
        "" fonction pour équiper l'objet sélectionné ""

        # on équipe l'objet et on rafraichit le cadre qui affiche l'objet équipé. Si c'est une arme, on dit de quel côté l'équiper
        if type(self.selected_item)==pc.ArmorEquip:
            self.master.master.selectedchar.equip_obj(self.selected_item)
        elif type(self.selected_item)==pc.ThrowEquip:
            self.master.master.selectedchar.equip_obj(self.selected_item,where)
        else:
            self.master.master.selectedchar.equip_obj(self.selected_item,where)

        # on peut alors déséquiper l'objet du personnage
        self.Equip_remove["state"]="normal"

        # print(self.master.master.selectedchar.playerequipment["left_melee"]==self.master.master.selectedchar.playerequipment["right_melee"])
        """

    def unequip_item(self):
        """
        "" fonction pour déséquiper l'objet sélectionné ""
        self.master.master.selectedchar.unequip_obj(self.selected_item)
        self.Equip_remove["state"]="disabled"

        # on rafraîchit le cadre qui affichait l'objet déséquipé
        if type(self.selected_item)==pc.ThrowEquip:
            self.selected_item.del_cord()"""


    def equip_cord(self,where):
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



    def change_solid(self,number):
        """if self.selected_item:
            self.selected_item.upsolid(number)

            if self.selected_item in self.master.master.selectedchar.playerequipment.values():
                self.CharArmF.refresh()
                self.CharMelF.refresh()
                self.CharThrF.refresh()

            self.refresh()"""

    def get_selectedchar(self):
        """
        return self.master.get_selectedchar()"""