from PySide6.QtWidgets import (QGroupBox, QGridLayout)


class CharMelFrame(QGroupBox):

    def __init__(self, parent):
        QGroupBox.__init__(self, " Mélée ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        """self.mastery_image = ImageTk.PhotoImage(Image.open("Images/symb-mastery.png").resize((10, 10), Image.ANTIALIAS))

        for i in range(1, 9):
            self.grid_columnconfigure(i, weight=1)

    def refresh(self):
        "" Fonction pour rafraîchir les équipements de mélée du personnage ""
        Meleelist = ["dgt_tr", "dgt_ctd", "estoc", "vit", "mastery", "quality", "solid"]
        Shieldlist = ["close", "dist", "mobi", "vit", "mastery", "quality", "solid"]
        for i in self.grid_slaves():
            i.destroy()

        i = 1
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
                    Label(self, text="...").grid(row=4, column=i)

    def up_mastery(self, where, number):
        self.master.master.master.selectedchar.playerequipment[where + "_melee"].upmastery(number)

        if where == "left":
            item = self.grid_slaves(1, 6)
        else:
            item = self.grid_slaves(4, 6)
        item[0]["text"] = str(
            self.master.master.master.selectedchar.get_weapon(where, "melee").get_stats_aslist(["mastery"])[0])

    def get_selectedchar(self):
        return self.master.get_selectedchar()"""
