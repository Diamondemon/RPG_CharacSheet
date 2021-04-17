from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QComboBox, QPushButton, QLabel, QGridLayout, QPlainTextEdit,
                               QCheckBox)


class ObjCreatorFrame(QWidget):
    """ Widget de création des objets pour l'inventaire du personnage """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        # Widgets et variables nécessaires à la création de tout type d'objet

        self.Name_entry = QLineEdit()
        self.Description_entry = QPlainTextEdit()
        self.Stackable_entry = QCheckBox()
        self.ObjType = QComboBox()
        for key in ["Objet", "Arme de mélée", "Arme de jet", "Corde", "Bouclier", "Armure"]:
            self.ObjType.addItem(self.tr(key))
        self.ObjType.setEditable(False)
        self.ObjType.setCurrentIndex(0)
        self.Register = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register, SIGNAL("clicked()"),self.inventory_add)

        self.Name_QLabel = QLabel(self.tr("Nom de l'objet"))
        self.Description_QLabel = QLabel(self.tr("Description"))
        self.Stackable_QLabel = QLabel(self.tr("Stackable"))
        
        self.grid.addWidget(self.Name_QLabel, 0, 0, 1, 2)
        self.grid.addWidget(self.Description_QLabel, 0, 2, 1, 6)
        self.grid.addWidget(self.Stackable_QLabel, 0, 8, 1, 2)
        self.grid.addWidget(self.Name_entry, 1, 0, 1, 2)
        self.grid.addWidget(self.ObjType, 2, 0, 1, 2)
        self.grid.addWidget(self.Description_entry, 1, 2, 2, 6)
        self.grid.addWidget(self.Stackable_entry, 1, 8, 1, 2)
        self.grid.addWidget(self.Register, 2, 8, 1, 2)

        # dictionnaire de tous les widgets et variables pour la création d'arme de mélée
        self.Melee = {}

        self.Melee["weight_QLabel"] = QLabel(self.tr("Type d'arme"))
        self.Melee["hand_QLabel"] = QLabel(self.tr("Taille"))
        self.Melee["tr_QLabel"] = QLabel(self.tr("Tranchant"))
        self.Melee["ctd_QLabel"] = QLabel(self.tr("Contondant"))
        self.Melee["estoc_QLabel"] = QLabel(self.tr("Estoc"))
        self.Melee["hast_QLabel"] = QLabel(self.tr("Hast"))
        self.Melee["hast_bonus_QLabel"] = QLabel(self.tr("Bonus de hast"))
        self.Melee["vit_QLabel"] = QLabel(self.tr("Vitesse"))
        self.Melee["quality_QLabel"] = QLabel(self.tr("Qualité"))
        self.Melee["solidity_QLabel"] = QLabel(self.tr("Solidité"))

        self.Melee["weight_entry"] = QComboBox()
        for key in ["Poings", "Légère", "Moyenne", "Lourde"]:
            self.Melee["weight_entry"].addItem(self.tr(key))
        self.Melee["weight_entry"].setEditable(False)
        self.Melee["weight_entry"].setCurrentIndex(0)
        self.Melee["hand_entry"] = QComboBox()
        for key in ["1 main", "2 mains"]:
            self.Melee["hand_entry"].addItem(self.tr(key))
        self.Melee["hand_entry"].setEditable(False)
        self.Melee["hand_entry"].setCurrentIndex(0)
        self.Melee["tr_entry"] = QLineEdit()
        self.Melee["ctd_entry"] = QLineEdit()
        self.Melee["estoc_entry"] = QLineEdit()
        self.Melee["hast_entry"] = QCheckBox()
        self.Melee["vit_entry"] = QLineEdit()
        self.Melee["quality_entry"] = QLineEdit()
        self.Melee["solidity_entry"] = QLineEdit()

        # dictionnaire de tous les widgets et variables pour la création d'arme de jet
        self.Throw = {}

        self.Throw["hand_QLabel"] = QLabel(self.tr("Taille"))
        self.Throw["type_QLabel"] = QLabel(self.tr("Type"))
        self.Throw["dgt_QLabel"] = QLabel(self.tr("Dégats"))
        self.Throw["pa_QLabel"] = QLabel(self.tr("Perce-armure"))
        self.Throw["solidity_QLabel"] = QLabel(self.tr("Solidité"))

        """self.Throw["scope"] = Frame(self)
        QLabel(self.Throw["scope"],text="Max palier portée").grid(row=0,column=0)
        QLabel(self.Throw["scope"],text="Vitesse").grid(row=0,column=1)
        QLabel(self.Throw["scope"],text="Précision").grid(row=0,column=2)
        QLineEdit().grid(row=1, column=0, padx="4p")  # scope
        QLineEdit().grid(row=1, column=1, padx="4p")
        QLineEdit().grid(row=1, column=2, padx="4p")"""

        """self.Throw["scope"].bind("<Button-3>",func=self.choose_scope)
        for i in self.Throw["scope"].grid_slaves():
            i.bind("<Button-3>",func=self.choose_scope)
        self.Throw["popup"] = Menu(self, tearoff=0)
        self.Throw["popup"].add_command(QLabel="Ajouter une ligne",command=self.scope_add)
        self.Throw["popup"].add_command(QLabel="Retirer une ligne",command=self.del_scope)"""

        self.Throw["hand_entry"] = QComboBox()
        for key in ["1 main", "2 mains"]:
            self.Throw["hand_entry"].addItem(self.tr(key))
        self.Throw["hand_entry"].setEditable(False)
        self.Throw["hand_entry"].setCurrentIndex(0)
        self.Throw["type_entry"] = QComboBox()
        for key in ["Lancer", "Tir"]:
            self.Throw["type_entry"].addItem(self.tr(key))
        self.Throw["type_entry"].setEditable(False)
        self.Throw["type_entry"].setCurrentIndex(1)
        self.Throw["dgt_entry"] = QLineEdit()
        self.Throw["pa_entry"] = QLineEdit()
        self.Throw["solidity_entry"] = QLineEdit()

        #widget pour le pourcentage de la corde
        self.Cord_QLabel = QLabel(self.tr("Casse (en %)"))
        self.Cord_entry = QLineEdit()

        # dictionnaire de tous les widgets et variables pour la création de bouclier
        self.Shield = {}

        self.Shield["hand_QLabel"] = QLabel(self.tr("Taille"))
        self.Shield["close_QLabel"] = QLabel(self.tr("Parade CàC"))
        self.Shield["dist_QLabel"] = QLabel(self.tr("Parade distance"))
        self.Shield["mobi_QLabel"] = QLabel(self.tr("Mobilité"))
        self.Shield["vit_QLabel"] = QLabel(self.tr("Vitesse"))
        self.Shield["quality_QLabel"] = QLabel(self.tr("Qualité"))
        self.Shield["solidity_QLabel"] = QLabel(self.tr("Solidité"))

        self.Shield["hand_entry"] = QComboBox()
        for key in ["1 main", "2 mains"]:
            self.Shield["hand_entry"].addItem(self.tr(key))
        self.Shield["hand_entry"].setEditable(False)
        self.Shield["hand_entry"].setCurrentIndex(0)
        self.Shield["close_entry"] = QLineEdit()
        self.Shield["dist_entry"] = QLineEdit()
        self.Shield["mobi_entry"] = QLineEdit()
        self.Shield["vit_entry"] = QLineEdit()
        self.Shield["quality_entry"] = QLineEdit()
        self.Shield["solidity_entry"] = QLineEdit()

        # dictionnaire de tous les widgets et variables pour la création d'armure
        self.Armor = {}

        self.Armor["location_QLabel"] = QLabel(self.tr("Localisation"))
        self.Armor["prot_QLabel"] = QLabel(self.tr("Protection"))
        self.Armor["amort_QLabel"] = QLabel(self.tr("Amortissement"))
        self.Armor["mobi_QLabel"] = QLabel(self.tr("Mobilité"))
        self.Armor["vit_QLabel"] = QLabel(self.tr("Vitesse"))
        self.Armor["solidity_QLabel"] = QLabel(self.tr("Solidité"))

        self.Armor["location_entry"] = QComboBox()
        for key in ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette", "Cuissots",
                    "Grèves", "Solerets"]:
            self.Armor["location_entry"].addItem(self.tr(key))
        self.Armor["location_entry"].setEditable(False)
        self.Armor["location_entry"].setCurrentIndex(0)
        self.Armor["prot_entry"] = QLineEdit()
        self.Armor["amort_entry"] = QLineEdit()
        self.Armor["mobi_entry"] = QLineEdit()
        self.Armor["vit_entry"] = QLineEdit()
        self.Armor["solidity_entry"] = QLineEdit()


    def change_obj_type(self,event=None):
        """
        ""Fonction pour alterner entre les différents types d'objets et faire changer les widgets""
        for i in self.grid_slaves(row=3):
            i.grid_forget()

        for i in self.grid_slaves(row=4):
            i.grid_forget()

        val=self.ObjType.get()

        # listes des caractéristiques demandées pour chaque objet
        meleelist=["weight","hand","tr","ctd","estoc","hast","quality","solidity"]
        throwlist=["hand","type","dgt","pa","solidity"]
        shieldlist=["hand","close","dist","mobi","vit","quality","solidity"]
        armorlist=["location","prot","amort","mobi","vit","solidity"]

        if val=="Arme de mélée":
            i=0
            for key in meleelist:
                self.Melee[key+"_QLabel"].grid(row=3,column=i,padx="4p")
                self.Melee[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
                if key=="hast":
                    if self.Melee["hast_var"].get():
                        key="hast_bonus"
                        self.Melee[key+"_QLabel"].grid(row=3,column=i,padx="4p")
                        self.Melee[key+"_entry"].grid(row=4,column=i,padx="4p")
                    else:
                        key="vit"
                        self.Melee[key+"_QLabel"].grid(row=3,column=i,padx="4p")
                        self.Melee[key+"_entry"].grid(row=4,column=i,padx="4p")
                    i+=1

        elif val=="Arme de jet":
            i=0
            for key in throwlist:
                self.Throw[key+"_QLabel"].grid(row=3,column=i,padx="4p")
                self.Throw[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
            self.Throw["scope"].grid(row=3,column=i,rowspan=3)


        elif val=="Bouclier":
            i=0
            for key in shieldlist:
                self.Shield[key+"_QLabel"].grid(row=3,column=i,padx="4p")
                self.Shield[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
        elif val=="Armure":
            i=0
            for key in armorlist:
                self.Armor[key+"_QLabel"].grid(row=3,column=i,padx="4p")
                self.Armor[key+"_entry"].grid(row=4,column=i,padx="4p")
                i+=1
        elif val=="Corde":
            self.Cord_QLabel.grid(row=3,column=0)
            self.Cord_entry.grid(row=3,column=1)
    """


    def hast_change(self):
        """
        ""Fonction pour passer du titre vitesse au titre bonus de hast ""

        if self.Melee["hast_var"].get():
            self.Melee["vit_QLabel"].grid_forget()

            self.Melee["hast_bonus_QLabel"].grid(row=3,column=5,padx="4p")

        else:
            self.Melee["hast_bonus_QLabel"].grid_forget()

            self.Melee["vit_QLabel"].grid(row=3,column=5,padx="4p")
        """

    def choose_scope(self,event=None):
        """
        ""Fonction d'apparition du popup pour ajouter/supprimer des lignes du tableau de portée ""

        self.Throw["popup"].tk_popup(event.x_root,event.y_root+20,0)
        """

    def del_scope(self,event=None):
        """
        "" Fonction de suppression d'une ligne du tableau de portée ""
        i=self.Throw["scope"].grid_size()[1]
        if i>2:
            for i in self.Throw["scope"].grid_slaves(row=i-1):
                i.destroy()
        """


    def scope_add(self,event=None):
        """
        "" Fonction d'ajout d'une ligne au tableau de portée""
        i=self.Throw["scope"].grid_size()[1]
        QLineEdit(self.Throw["scope"],textvariable=IntVar(),width=16).grid(row=i,column=0,padx="4p")
        QLineEdit(self.Throw["scope"],textvariable=IntVar(),width=6).grid(row=i,column=1,padx="4p")
        QLineEdit(self.Throw["scope"],textvariable=IntVar(),width=9).grid(row=i,column=2,padx="4p")

        for key in self.Throw["scope"].grid_slaves(row=i):
            key.bind("<Button-3>",self.choose_scope)
        """



    def inventory_add(self):
        """
        "" Fonction qui ajoute l'objet au personnage selectionné dans CharDFrame ""
        val=self.ObjType.get()

        if val=="Objet":
            new_obj=pc.Obj(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get())

        elif val=="Arme de mélée":
            new_obj=pc.MeleeEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Melee["weight_entry"].get(),self.Melee["hast_var"].get())
            new_obj.upstats(self.Melee["hand_entry"].current()+1,self.Melee["tr_var"].get(),self.Melee["ctd_var"].get(),self.Melee["estoc_var"].get(),self.Melee["vit_var"].get())
            new_obj.newquali(self.Melee["quality_var"].get())
            new_obj.upsolid(self.Melee["solidity_var"].get())


        elif val=="Arme de jet":
            new_obj=pc.ThrowEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Throw["type_entry"].get())
            new_obj.upstats(self.Throw["hand_entry"].current()+1,self.Throw["dgt_var"].get(),self.Throw["pa_var"].get())
            new_obj.upsolid(self.Throw["solidity_var"].get())

            scopelist=[]
            for i in range(1,self.Throw["scope"].grid_size()[1]):
                sublist=[]
                for key in self.Throw["scope"].grid_slaves(row=i):
                    sublist.insert(0,int(key.get()))
                scopelist.append(sublist)
            new_obj.newscope(scopelist)

        elif val=="Armure":
            new_obj=pc.ArmorEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Armor["location_entry"].get())
            new_obj.upstats(self.Armor["prot_var"].get(),self.Armor["amort_var"].get(),self.Armor["mobi_var"].get(),self.Armor["vit_var"].get())
            new_obj.upsolid(self.Armor["solidity_var"].get())


        elif val=="Bouclier":
            new_obj=pc.ShieldEquip(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get())
            new_obj.upstats(self.Shield["hand_entry"].current()+1,self.Shield["close_var"].get(),self.Shield["dist_var"].get(),self.Shield["mobi_var"].get(),self.Shield["vit_var"].get())
            new_obj.upsolid(self.Shield["solidity_var"].get())
            new_obj.newquali(self.Shield["quality_var"].get())

        elif val=="Corde":
            new_obj=pc.Cord(self.New_name.get(),self.Description_entry.get(0.0,"end"),self.New_stackable.get(),self.Cord_var.get())


        self.master.master.master.selectedchar.inventory[new_obj]=1 #par défaut, on gagne 1 objet et il n'est pas équipé
        # print(self.master.master.master.selectedchar.inventory)
        self.master.refresh()
        """

    def get_selectedchar(self):
        return self.master.get_selectedchar()
