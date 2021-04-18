from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (QGroupBox, QGridLayout, QLabel, QPushButton, QFrame)
from PySide6.QtGui import QPixmap, QIcon
import Perso_class as Pc
import CUF


class CharMelFrame(QGroupBox):

    def __init__(self):
        QGroupBox.__init__(self, " Mélée ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.meleelist = ["Nom", "Dég. Tr.", "Dég. Ctd.", "Estoc", "Vit.", "Maîtr.", "Qual.", "Sol."]
        self.shieldlist = ["Nom", "Par. CàC", "Par. Dist.", "Mobi.", "Vit.", "Maîtr.", "Qual.", "Sol."]

        self.mastery_image = QIcon("./Images/symb-mastery.svg")

        self.leftlist = {"title": QLabel(), "name": QLabel(), "equip_name": QLabel(),
                         "mastery_add": QPushButton("+"), "mastery_rm": QPushButton("-")}
        self.leftlist["mastery_add"].setIcon(self.mastery_image)
        self.leftlist["mastery_rm"].setIcon(self.mastery_image)
        self.grid.addWidget(self.leftlist["title"], 1, 0)
        self.grid.addWidget(self.leftlist["name"], 0, 1)
        self.grid.addWidget(self.leftlist["equip_name"], 1, 1)
        self.grid.addWidget(self.leftlist["mastery_add"], 0, 9)
        self.grid.addWidget(self.leftlist["mastery_rm"], 1, 9)
        for i in range(7):
            self.leftlist[str(i)] = QLabel()
            self.grid.addWidget(self.leftlist[str(i)], 0, i+2)
            self.leftlist["equip_" + str(i)] = QLabel()
            self.grid.addWidget(self.leftlist["equip_" + str(i)], 1, i+2)

        self.separator = QFrame()
        self.separator.setFrameShape(QFrame.HLine)
        self.grid.addWidget(self.separator, 2, 0, 1, 10)

        self.rightlist = {"title": QLabel(self.tr("Main droite")), "name": QLabel(), "equip_name": QLabel(),
                          "mastery_add": QPushButton("+"), "mastery_rm": QPushButton("-")}
        self.rightlist["mastery_add"].setIcon(self.mastery_image)
        self.rightlist["mastery_rm"].setIcon(self.mastery_image)
        self.grid.addWidget(self.rightlist["title"], 4, 0)
        self.grid.addWidget(self.rightlist["name"], 3, 1)
        self.grid.addWidget(self.rightlist["equip_name"], 4, 1)
        self.grid.addWidget(self.rightlist["mastery_add"], 3, 9)
        self.grid.addWidget(self.rightlist["mastery_rm"], 4, 9)
        for i in range(7):
            self.rightlist[str(i)] = QLabel()
            self.grid.addWidget(self.rightlist[str(i)], 3, i+2)
            self.rightlist["equip_" + str(i)] = QLabel()
            self.grid.addWidget(self.rightlist["equip_" + str(i)], 4, i+2)

    def refresh(self):
        """ Fonction pour rafraîchir les équipements de mélée du personnage """
        meleelist = ["dgt_tr", "dgt_ctd", "estoc", "vit", "mastery", "quality", "solid"]
        shieldlist = ["close", "dist", "mobi", "vit", "mastery", "quality", "solid"]
        for widget in self.leftlist.values():
            widget.hide()

        self.separator.hide()

        for widget in self.rightlist.values():
            widget.hide()
        selectedchar = self.get_selectedchar()
        left_equip = selectedchar.get_weapon("left", "melee")

        # si l'objet est équipé, on met ses caractéristiques, sinon, on met des "..."
        # disjonction de cas si c'est une arme ou un bouclier
        if left_equip:
            self.leftlist["name"].setText(self.tr("Nom"))
            self.leftlist["name"].show()
            self.leftlist["equip_name"].setText(left_equip.get_stat("name"))
            self.leftlist["equip_name"].show()

            if left_equip.get_stat("hand") == 2:
                self.leftlist["title"].setText(self.tr("2 mains"))
                self.leftlist["title"].show()

            else:
                self.leftlist["title"].setText(self.tr("Main gauche"))
                self.refresh_right(selectedchar)

        else:
            self.leftlist["title"].setText(self.tr("Main gauche"))
            self.leftlist["title"].show()
            self.leftlist["name"].setText("...")
            self.leftlist["name"].show()
            self.leftlist["equip_name"].setText("...")
            self.leftlist["equip_name"].show()
            for i in range(7):
                self.leftlist[str(i)].setText("...")
                self.leftlist[str(i)].show()
                self.leftlist["equip_"+str(i)].setText("...")
                self.leftlist["equip_"+str(i)].show()

            self.refresh_right(selectedchar)
        """i = 1
        # si l'objet est équipé, on met ses caractéristiques, sinon, on met des "..."
        # disjonction de cas si c'est une arme ou un bouclier
        if self.master.master.master.selectedchar.playerequipment["left_melee"]:
            Label(self, text=self.master.master.master.selectedchar.playerequipment["left_melee"].name).grid(row=1,
                                                                                                             column=1)
            if self.master.master.master.selectedchar.playerequipment["left_melee"].carac["hand"] == 2:
                Label(self, text="2 mains").grid(row=0, column=0, rowspan=2)
                if type(self.master.master.master.selectedchar.playerequipment["left_melee"]) == pc.MeleeEquip:
                    i = 1
                    for key in ["Nom", "Dég. Tr.", "Dég. Ctd.", "Estoc", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                        if key == "Vit." and self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                            "hast"]:
                            Label(self, text="Bon. Hast").grid(row=0, column=i)
                        else:
                            Label(self, text=key).grid(row=0, column=i)
                        i += 1
                    i = 2
                    for key in Meleelist:
                        if key == "vit" and self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                            "hast"]:
                            Label(self, text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                                "hast_bonus"]).grid(row=0, column=i)
                        else:
                            Label(self, text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                                key]).grid(row=1, column=i)
                        i += 1

                elif type(self.master.master.master.selectedchar.playerequipment["left_melee"]) == pc.ShieldEquip:
                    i = 1
                    for key in ["Nom", "Par. CàC", "Par. Dist.", "Mobi.", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                        Label(self, text=key).grid(row=3, column=i)
                        i += 1
                    i = 2
                    for key in Shieldlist:
                        Label(self, text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                            key]).grid(row=4, column=i)
                        i += 1

            else:
                Label(self, text="Main gauche").grid(row=0, column=0, rowspan=2)
                if type(self.master.master.master.selectedchar.playerequipment["left_melee"]) == pc.MeleeEquip:
                    i = 1
                    for key in ["Nom", "Dég. Tr.", "Dég. Ctd.", "Estoc", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                        if key == "Vit." and self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                            "hast"]:
                            Label(self, text="Bon. Hast").grid(row=0, column=i)
                        else:
                            Label(self, text=key).grid(row=0, column=i)
                        i += 1
                    i = 2
                    for key in Meleelist:
                        if key == "vit" and self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                            "hast"]:
                            Label(self, text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                                "hast_bonus"]).grid(row=0, column=i)
                        else:
                            Label(self, text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                                key]).grid(row=1, column=i)
                        i += 1

                elif type(self.master.master.master.selectedchar.playerequipment["left_melee"]) == pc.ShieldEquip:
                    i = 1
                    for key in ["Nom", "Par. CàC", "Par. Dist.", "Mobi.", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                        Label(self, text=key).grid(row=0, column=i)
                        i += 1
                    i = 2
                    for key in Shieldlist:
                        Label(self, text=self.master.master.master.selectedchar.playerequipment["left_melee"].carac[
                            key]).grid(row=1, column=i)
                        i += 1

                ttk.Separator(self, orient="horizontal").grid(row=2, column=0, columnspan=10, sticky="we", padx="4p",
                                                              pady="4p")

                Label(self, text="Main droite").grid(row=3, column=0, rowspan=2)

                if self.master.master.master.selectedchar.playerequipment["right_melee"]:
                    Label(self, text=self.master.master.master.selectedchar.playerequipment["right_melee"].name).grid(
                        row=4, column=1)
                    if type(self.master.master.master.selectedchar.playerequipment["right_melee"]) == pc.MeleeEquip:
                        i = 1
                        for key in ["Nom", "Dég. Tr.", "Dég. Ctd.", "Estoc", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                            if key == "Vit." and \
                                    self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast"]:
                                Label(self, text="Bon. Hast").grid(row=3, column=i)
                            else:
                                Label(self, text=key).grid(row=3, column=i)
                            i += 1
                        i = 2
                        for key in Meleelist:
                            if key == "vit" and \
                                    self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast"]:
                                Label(self,
                                      text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[
                                          "hast_bonus"]).grid(row=4, column=i)
                            else:
                                Label(self,
                                      text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[
                                          key]).grid(row=4, column=i)
                            i += 1

                    elif type(self.master.master.master.selectedchar.playerequipment["right_melee"]) == pc.ShieldEquip:
                        i = 1
                        for key in ["Nom", "Par. CàC", "Par. Dist.", "Mobi.", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                            Label(self, text=key).grid(row=3, column=i)
                            i += 1
                        i = 2
                        for key in Shieldlist:
                            Label(self,
                                  text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[
                                      key]).grid(row=4, column=i)
                            i += 1

                    Button(self, text="+", image=self.mastery_image, compound="right",
                           command=partial(self.up_mastery, "right", 1), takefocus=0).grid(row=3, column=9, padx="4p",
                                                                                           sticky="we")
                    Button(self, text="-", image=self.mastery_image, compound="right",
                           command=partial(self.up_mastery, "right", -1), takefocus=0).grid(row=4, column=9, padx="4p",
                                                                                            sticky="we")

                else:
                    for i in range(1, 9):
                        Label(self, text="...").grid(row=3, column=i)
                        Label(self, text="...").grid(row=4, column=i)

            Button(self, text="+", image=self.mastery_image, compound="right",
                   command=partial(self.up_mastery, "left", 1), takefocus=0).grid(row=0, column=9, padx="4p",
                                                                                  sticky="we")
            Button(self, text="-", image=self.mastery_image, compound="right",
                   command=partial(self.up_mastery, "left", -1), takefocus=0).grid(row=1, column=9, padx="4p",
                                                                                   sticky="we")

        else:
            Label(self, text="Main gauche").grid(row=0, column=0, rowspan=2)
            for i in range(1, 9):
                Label(self, text="...").grid(row=1, column=i)
                Label(self, text="...").grid(row=0, column=i)

            ttk.Separator(self, orient="horizontal").grid(row=2, column=0, columnspan=10, sticky="we", padx="4p",
                                                          pady="4p")

            Label(self, text="Main droite").grid(row=3, column=0, rowspan=2)

            if self.master.master.master.selectedchar.playerequipment["right_melee"]:
                Label(self, text=self.master.master.master.selectedchar.playerequipment["right_melee"].name).grid(row=4,
                                                                                                                  column=1)
                if type(self.master.master.master.selectedchar.playerequipment["right_melee"]) == pc.MeleeEquip:
                    i = 1
                    for key in ["Nom", "Dég. Tr.", "Dég. Ctd.", "Estoc", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                        if key == "Vit." and \
                                self.master.master.master.selectedchar.playerequipment["right_melee"].carac["hast"]:
                            Label(self, text="Bon. Hast").grid(row=3, column=i)
                        else:
                            Label(self, text=key).grid(row=3, column=i)
                        i += 1
                    i = 2
                    for key in Meleelist:
                        if key == "vit" and self.master.master.master.selectedchar.playerequipment["right_melee"].carac[
                            "hast"]:
                            Label(self,
                                  text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[
                                      "hast_bonus"]).grid(row=4, column=i)
                        else:
                            Label(self,
                                  text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[
                                      key]).grid(row=4, column=i)
                        i += 1

                elif type(self.master.master.master.selectedchar.playerequipment["right_melee"]) == pc.ShieldEquip:
                    i = 1
                    for key in ["Nom", "Par. CàC", "Par. Dist.", "Mobi.", "Vit.", "Maîtr.", "Qual.", "Sol."]:
                        Label(self, text=key).grid(row=3, column=i)
                        i += 1
                    i = 2
                    for key in Shieldlist:
                        Label(self, text=self.master.master.master.selectedchar.playerequipment["right_melee"].carac[
                            key]).grid(row=4, column=i)
                        i += 1

                Button(self, text="+", image=self.mastery_image, compound="right",
                       command=partial(self.up_mastery, "right", 1), takefocus=0).grid(row=3, column=9, padx="4p",
                                                                                       sticky="we")
                Button(self, text="-", image=self.mastery_image, compound="right",
                       command=partial(self.up_mastery, "right", -1), takefocus=0).grid(row=4, column=9, padx="4p",
                                                                                        sticky="we")



            else:
                for i in range(1, 9):
                    Label(self, text="...").grid(row=3, column=i)
                    Label(self, text="...").grid(row=4, column=i)"""

    def refresh_right(self, selectedchar: Pc.player):
        meleelist = ["dgt_tr", "dgt_ctd", "estoc", "vit", "mastery", "quality", "solid"]
        shieldlist = ["close", "dist", "mobi", "vit", "mastery", "quality", "solid"]

        self.separator.show()
        self.rightlist["title"].show()

        right_equip = selectedchar.get_weapon("right", "melee")

        if right_equip:
            self.rightlist["name"].setText(self.tr("Nom"))
            self.rightlist["name"].show()
            self.rightlist["equip_name"].setText(right_equip.get_stat("name"))
            self.rightlist["equip_name"].show()

        else:
            self.rightlist["name"].setText("...")
            self.rightlist["name"].show()
            self.rightlist["equip_name"].setText("...")
            self.rightlist["equip_name"].show()
            for i in range(7):
                self.rightlist[str(i)].setText("...")
                self.rightlist[str(i)].show()
                self.rightlist["equip_" + str(i)].setText("...")
                self.rightlist["equip_" + str(i)].show()

    def up_mastery(self, where, number):
        selectedchar = self.parent().get_selectedchar()
        selectedchar.get_weapon(where, "melee").upmastery(number)
        self.master.master.master.selectedchar.playerequipment[where + "_melee"].upmastery(number)

        if where == "left":
            item = self.grid_slaves(1, 6)
        else:
            item = self.grid_slaves(4, 6)
        item[0]["text"] = str(
            self.master.master.master.selectedchar.get_weapon(where, "melee").get_stats_aslist(["mastery"])[0])

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CUF.CharUsefulFrame:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        return self.parentWidget()
