from PySide6.QtWidgets import (QGroupBox, QGridLayout)
from PySide6.QtGui import QPixmap


class CharThrFrame(QGroupBox):

    def __init__(self, parent):
        QGroupBox.__init__(self, " Jet ", parent)
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.mastery_image = QPixmap("./Images/symb-perception.png")
        self.mastery_image = self.mastery_image.scaled(10, 10)

        """for i in range(1, 7):
            self.grid_columnconfigure(i, weight=1)
        self.grid_columnconfigure(8, weight=2)"""

    def refresh(self):
        """ Fonction pour rafraîchir les armes de jet du personnage """
        Throwlist = ["dgt", "pa", "cord", "mastery", "solid"]
        for i in self.grid_slaves():
            i.destroy()
        """
        i = 1
        # si l'objet est équipé, on met ses caractéristiques, sinon, on met des "..."
        if self.master.master.master.selectedchar.playerequipment["left_throw"]:
            Label(self, text=self.master.master.master.selectedchar.playerequipment["left_throw"].name).grid(row=1,
                                                                                                             column=1)
            if self.master.master.master.selectedchar.playerequipment["left_throw"].carac["hand"] == 2:
                Label(self, text="2 mains").grid(row=0, column=0, rowspan=2)
                i = 1
                for key in ["Nom", "Dég.", "P.-Arm.", "Cordes", "Maîtr.", "Sol."]:
                    if key != "Cordes" or self.master.master.master.selectedchar.playerequipment["left_throw"].carac[
                        "cord"]:
                        Label(self, text=key).grid(row=0, column=i)
                        i += 1
                i = 2
                for key in Throwlist:
                    if key != "cord":
                        Label(self, text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac[
                            key]).grid(row=1, column=i)
                        i += 1

                    elif self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                        Label(self, text=str(
                            self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][
                                0]) + " - " + str(
                            self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][
                                1]) + "%").grid(row=1, column=i)
                        i += 1

                scopeFrame = Frame(self)
                scopeFrame.grid(row=0, column=7, rowspan=2)
                Label(scopeFrame, text="Préc.").grid(row=1, column=0)
                Label(scopeFrame, text="Vit.").grid(row=2, column=0)
                Label(scopeFrame, text=0).grid(row=0, column=1)
                ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=1, rowspan=2, sticky="ns")

                for i in range(
                        len(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"])):
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][
                              0]).grid(row=0, column=3 + 2 * i)
                    ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=3 + 2 * i, rowspan=2, sticky="NS")
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][
                              2]).grid(row=1, column=2 + 2 * i)
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][
                              1]).grid(row=2, column=2 + 2 * i)



            else:
                Label(self, text="Main gauche").grid(row=0, column=0, rowspan=2)
                i = 1
                for key in ["Nom", "Dég.", "P.-Arm.", "Cordes", "Maîtr.", "Sol."]:
                    if key != "Cordes" or self.master.master.master.selectedchar.playerequipment["left_throw"].carac[
                        "cord"]:
                        Label(self, text=key).grid(row=0, column=i)
                        i += 1
                i = 2
                for key in Throwlist:
                    if key != "cord":
                        Label(self, text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac[
                            key]).grid(row=1, column=i)
                        i += 1

                    elif self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"]:
                        Label(self, text=str(
                            self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][
                                0]) + " - " + str(
                            self.master.master.master.selectedchar.playerequipment["left_throw"].carac["cord"][
                                1]) + "%").grid(row=1, column=i)
                        i += 1

                scopeFrame = Frame(self)
                scopeFrame.grid(row=0, column=7, rowspan=2)
                Label(scopeFrame, text="Vit.").grid(row=1, column=0)
                Label(scopeFrame, text="Préc.").grid(row=2, column=0)
                Label(scopeFrame, text=0).grid(row=0, column=1)
                ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=1, rowspan=2, sticky="ns")

                for i in range(
                        len(self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"])):
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][
                              0]).grid(row=0, column=3 + 2 * i)
                    ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=3 + 2 * i, rowspan=2, sticky="NS")
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][
                              1]).grid(row=1, column=2 + 2 * i)
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["left_throw"].carac["scope"][i][
                              2]).grid(row=2, column=2 + 2 * i)

                ttk.Separator(self, orient="horizontal").grid(row=2, column=0, columnspan=9, sticky="we", padx="4p",
                                                              pady="4p")

                Label(self, text="Main droite").grid(row=3, column=0, rowspan=2)

                if self.master.master.master.selectedchar.playerequipment["right_throw"]:
                    Label(self, text=self.master.master.master.selectedchar.playerequipment["right_throw"].name).grid(
                        row=4, column=1)
                    i = 1
                    for key in ["Nom", "Dég.", "P.-Arm.", "Cordes", "Maîtr.", "Sol."]:
                        if key != "Cordes" or \
                                self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                            Label(self, text=key).grid(row=3, column=i)
                            i += 1
                    i = 2
                    for key in Throwlist:
                        if key != "cord":
                            Label(self,
                                  text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac[
                                      key]).grid(row=4, column=i)
                            i += 1
                        elif self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                            Label(self, text=str(
                                self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][
                                    0]) + " - " + str(
                                self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][
                                    1]) + "%").grid(row=4, column=i)
                            i += 1

                    scopeFrame = Frame(self)
                    scopeFrame.grid(row=3, column=7, rowspan=2)
                    Label(scopeFrame, text="Vit.").grid(row=1, column=0)
                    Label(scopeFrame, text="Préc.").grid(row=2, column=0)
                    Label(scopeFrame, text=0).grid(row=0, column=1)
                    ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=1, rowspan=2, sticky="ns")

                    for i in range(
                            len(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"])):
                        Label(scopeFrame, text=
                        self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][
                            0]).grid(row=0, column=3 + 2 * i)
                        ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=3 + 2 * i, rowspan=2,
                                                                          sticky="NS")
                        Label(scopeFrame, text=
                        self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][
                            1]).grid(row=1, column=2 + 2 * i)
                        Label(scopeFrame, text=
                        self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][
                            2]).grid(row=2, column=2 + 2 * i)

                    Button(self, text="+", image=self.mastery_image, compound="right",
                           command=partial(self.up_mastery, "right", 1)).grid(sticky="we", row=3, column=8, padx="4p")
                    Button(self, text="-", image=self.mastery_image, compound="right",
                           command=partial(self.up_mastery, "right", -1)).grid(sticky="we", row=4, column=8, padx="4p")

                else:
                    for i in range(1, 8):
                        Label(self, text="...").grid(row=3, column=i)
                        Label(self, text="...").grid(row=4, column=i)

            Button(self, text="+", image=self.mastery_image, compound="right",
                   command=partial(self.up_mastery, "left", 1)).grid(sticky="we", row=0, column=8, padx="4p")
            Button(self, text="-", image=self.mastery_image, compound="right",
                   command=partial(self.up_mastery, "left", -1)).grid(sticky="we", row=1, column=8, padx="4p")


        else:
            Label(self, text="Main gauche").grid(row=0, column=0, rowspan=2)
            for i in range(1, 8):
                Label(self, text="...").grid(row=1, column=i)
                Label(self, text="...").grid(row=0, column=i)

            ttk.Separator(self, orient="horizontal").grid(row=2, column=0, columnspan=9, sticky="we", padx="4p",
                                                          pady="4p")

            Label(self, text="Main droite").grid(row=3, column=0, rowspan=2)

            if self.master.master.master.selectedchar.playerequipment["right_throw"]:
                Label(self, text=self.master.master.master.selectedchar.playerequipment["right_throw"].name).grid(row=4,
                                                                                                                  column=1)
                i = 1
                for key in ["Nom", "Dég.", "P.-Arm.", "Cordes", "Maîtr.", "Sol."]:
                    if key != "Cordes" or self.master.master.master.selectedchar.playerequipment["right_throw"].carac[
                        "cord"]:
                        Label(self, text=key).grid(row=3, column=i)
                        i += 1

                i = 2
                for key in Throwlist:
                    if key != "cord":
                        Label(self, text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac[
                            key]).grid(row=4, column=i)
                        i += 1

                    elif self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"]:
                        Label(self, text=str(
                            self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][
                                0]) + " - " + str(
                            self.master.master.master.selectedchar.playerequipment["right_throw"].carac["cord"][
                                1]) + "%").grid(row=4, column=i)
                        i += 1

                scopeFrame = Frame(self)
                scopeFrame.grid(row=3, column=7, rowspan=2)
                Label(scopeFrame, text="Vit.").grid(row=1, column=0)
                Label(scopeFrame, text="Préc.").grid(row=2, column=0)
                Label(scopeFrame, text=0).grid(row=0, column=1)
                ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=1, rowspan=2, sticky="ns")

                for i in range(
                        len(self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"])):
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][
                              0]).grid(row=0, column=3 + 2 * i)
                    ttk.Separator(scopeFrame, orient="vertical").grid(row=1, column=3 + 2 * i, rowspan=2, sticky="NS")
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][
                              1]).grid(row=1, column=2 + 2 * i)
                    Label(scopeFrame,
                          text=self.master.master.master.selectedchar.playerequipment["right_throw"].carac["scope"][i][
                              2]).grid(row=2, column=2 + 2 * i)

                Button(self, text="+", image=self.mastery_image, compound="right",
                       command=partial(self.up_mastery, "right", 1)).grid(sticky="we", row=3, column=8, padx="4p")
                Button(self, text="-", image=self.mastery_image, compound="right",
                       command=partial(self.up_mastery, "right", -1)).grid(sticky="we", row=4, column=8, padx="4p")

            else:
                for i in range(1, 8):
                    Label(self, text="...").grid(row=3, column=i)
                    Label(self, text="...").grid(row=4, column=i)"""

    def up_mastery(self, where, number):
        self.master.master.master.selectedchar.get_weapon(where, "throw").upmastery(number)

        if self.master.master.master.selectedchar.get_weapon(where, "throw").get_stats_aslist(["type"])[0] == "Tir":
            col = 5
        else:
            col = 4

        if where == "left":
            item = self.grid_slaves(1, col)
        else:
            item = self.grid_slaves(4, col)
        item[0]["text"] = str(
            self.master.master.master.selectedchar.get_weapon(where, "throw").get_stats_aslist(["mastery"])[0])

    def get_selectedchar(self):
        return self.master.get_selectedchar()