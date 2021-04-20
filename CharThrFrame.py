from PySide6.QtCore import SIGNAL, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QGroupBox, QGridLayout, QLabel, QPushButton, QFrame)
from functools import partial
import CUF
import Perso_class as Pc


class CharThrFrame(QGroupBox):

    def __init__(self):
        QGroupBox.__init__(self, " Jet ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)

        self.mastery_image = QIcon("./Images/symb-mastery.svg")

        self.throwlist = ["Dég.", "P.-Arm.", "Cordes", "Maîtr.", "Sol."]

        self.leftlist = {"title": QLabel(), "name": QLabel(), "equip_name": QLabel(),
                         "mastery_add": QPushButton("+"), "mastery_rm": QPushButton("-")}
        self.leftlist["mastery_add"].setIcon(self.mastery_image)
        self.leftlist["mastery_rm"].setIcon(self.mastery_image)
        self.grid.addWidget(self.leftlist["title"], 1, 0)
        self.grid.addWidget(self.leftlist["name"], 0, 1)
        self.grid.addWidget(self.leftlist["equip_name"], 1, 1)
        self.grid.addWidget(self.leftlist["mastery_add"], 0, 9)
        self.grid.addWidget(self.leftlist["mastery_rm"], 1, 9)
        for i in range(5):
            self.leftlist[str(i)] = QLabel()
            self.grid.addWidget(self.leftlist[str(i)], 0, i + 2)
            self.leftlist["equip_" + str(i)] = QLabel()
            self.grid.addWidget(self.leftlist["equip_" + str(i)], 1, i + 2)

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
        for i in range(5):
            self.rightlist[str(i)] = QLabel()
            self.grid.addWidget(self.rightlist[str(i)], 3, i + 2)
            self.rightlist["equip_" + str(i)] = QLabel()
            self.grid.addWidget(self.rightlist["equip_" + str(i)], 4, i + 2)

        for key in self.rightlist.keys():
            if (key != "mastery_add") and (key != "mastery_rm"):
                self.leftlist[key].setAlignment(Qt.AlignCenter)
                self.rightlist[key].setAlignment(Qt.AlignCenter)
            elif key == "mastery_add":
                self.connect(self.leftlist[key], SIGNAL("clicked()"), partial(self.up_mastery, "left", 1))
                self.connect(self.rightlist[key], SIGNAL("clicked()"), partial(self.up_mastery, "right", 1))

            else:
                self.connect(self.leftlist[key], SIGNAL("clicked()"), partial(self.up_mastery, "left", -1))
                self.connect(self.rightlist[key], SIGNAL("clicked()"), partial(self.up_mastery, "right", -1))

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

    def refresh(self):
        """
        Method called to refresh the throwable/throwing equipment of the character

        :return: None
        """
        throwlist = ["dgt", "pa", "cord", "mastery", "solid"]

        for widget in self.leftlist.values():
            widget.hide()

        self.separator.hide()

        for widget in self.rightlist.values():
            widget.hide()

        selectedchar = self.get_selectedchar()
        left_equip = selectedchar.get_weapon("left", "throw")

        # si l'objet est équipé, on met ses caractéristiques, sinon, on met des "..."
        if left_equip:
            self.leftlist["name"].setText(self.tr("Nom"))
            self.leftlist["name"].show()
            self.leftlist["equip_name"].setText(left_equip.get_stat("name"))
            self.leftlist["equip_name"].show()
            self.leftlist["mastery_add"].show()
            self.leftlist["mastery_rm"].show()

            statlist = left_equip.get_stats_aslist(throwlist)
            for i in range(5):
                if statlist[i] is not None:
                    self.leftlist[str(i)].setText(self.tr(self.throwlist[i]))
                    self.leftlist[str(i)].show()
                    self.leftlist["equip_" + str(i)].setText(str(statlist[i]))
                    self.leftlist["equip_" + str(i)].show()

            if left_equip.get_stat("hand") == 2:
                self.leftlist["title"].setText(self.tr("2 mains"))
                self.leftlist["title"].show()

            else:
                self.leftlist["title"].setText(self.tr("Main gauche"))
                self.leftlist["title"].show()
                self.refresh_right(selectedchar)

        else:
            self.leftlist["title"].setText(self.tr("Main gauche"))
            self.leftlist["title"].show()
            self.leftlist["name"].setText("...")
            self.leftlist["name"].show()
            self.leftlist["equip_name"].setText("...")
            self.leftlist["equip_name"].show()
            for i in range(5):
                self.leftlist[str(i)].setText("...")
                self.leftlist[str(i)].show()
                self.leftlist["equip_"+str(i)].setText("...")
                self.leftlist["equip_"+str(i)].show()

            self.refresh_right(selectedchar)
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

    def refresh_right(self, selectedchar: Pc.player):
        """
        Method called to refresh only the throwable/throwing equipment in the right hand of the character

        :param selectedchar: the character displayed
        :return: None
        """
        throwlist = ["dgt", "pa", "cord", "mastery", "solid"]

        self.separator.show()
        self.rightlist["title"].show()

        right_equip = selectedchar.get_weapon("right", "throw")

        if right_equip:
            self.rightlist["name"].setText(self.tr("Nom"))
            self.rightlist["name"].show()
            self.rightlist["equip_name"].setText(right_equip.get_stat("name"))
            self.rightlist["equip_name"].show()
            self.rightlist["mastery_add"].show()
            self.rightlist["mastery_rm"].show()

            statlist = right_equip.get_stats_aslist(throwlist)
            for i in range(5):
                if statlist[i] is not None:
                    self.rightlist[str(i)].setText(self.tr(self.throwlist[i]))
                    self.rightlist[str(i)].show()
                    self.rightlist["equip_" + str(i)].setText(str(statlist[i]))
                    self.rightlist["equip_" + str(i)].show()

        else:
            self.rightlist["name"].setText("...")
            self.rightlist["name"].show()
            self.rightlist["equip_name"].setText("...")
            self.rightlist["equip_name"].show()
            for i in range(5):
                self.rightlist[str(i)].setText("...")
                self.rightlist[str(i)].show()
                self.rightlist["equip_" + str(i)].setText("...")
                self.rightlist["equip_" + str(i)].show()

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()

    def up_mastery(self, where, number):
        """
        Method called to manage the mastery the character has with its weapon

        :param where: "left" or "right", side of the weapon
        :param number: number to increase mastery by
        :return: None
        """
        selectedchar = self.parent().get_selectedchar()
        selectedchar.get_weapon(where, "throw").upmastery(number)

        if where == "left":
            self.leftlist["equip_3"].setText(str(selectedchar.get_weapon(where, "throw").get_stat("mastery")))
        else:
            self.rightlist["equip_3"].setText(str(selectedchar.get_weapon(where, "throw").get_stat("mastery")))

        self.save_character()
