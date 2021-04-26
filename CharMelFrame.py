from PySide6.QtCore import Qt, SIGNAL
from PySide6.QtWidgets import (QGroupBox, QGridLayout, QLabel, QPushButton, QFrame)
from PySide6.QtGui import QIcon
import Perso_class as Pc
from functools import partial
import CUF


class CharMelFrame(QGroupBox):
    """ Widget to display the melee equipment of the character """

    def __init__(self):
        QGroupBox.__init__(self, " Mélée ")
        self.grid = QGridLayout(self)
        self.setLayout(self.grid)
        self.meleelist = ["Dég. Tr.", "Dég. Ctd.", "Estoc", "Vit.", "Maîtr.", "Qual.", "Sol."]
        self.shieldlist = ["Par. CàC", "Par. Dist.", "Mobi.", "Vit.", "Maîtr.", "Qual.", "Sol."]

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
        return QGroupBox.parent(self)

    def refresh(self):
        """
        Method called to refresh the melee equipment of the character

        :return: None
        """
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
            self.leftlist["mastery_add"].show()
            self.leftlist["mastery_rm"].show()

            if type(left_equip) == Pc.MeleeEquip:
                if left_equip.is_hast():
                    meleelist[3] = "hast_bonus"
                statlist = left_equip.get_stats_aslist(meleelist)
                for i in range(7):
                    if i == 3 and meleelist[i] == "hast_bonus":
                        self.leftlist[str(i)].setText(self.tr("Bon. Hast"))
                    else:
                        self.leftlist[str(i)].setText(self.tr(self.meleelist[i]))
                    self.leftlist[str(i)].show()
                    self.leftlist["equip_" + str(i)].setText(str(statlist[i]))
                    self.leftlist["equip_" + str(i)].show()

            elif type(left_equip) == Pc.ShieldEquip:
                statlist = left_equip.get_stats_aslist(shieldlist)
                for i in range(7):
                    self.leftlist[str(i)].setText(self.tr(self.shieldlist[i]))
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
            for i in range(7):
                self.leftlist[str(i)].setText("...")
                self.leftlist[str(i)].show()
                self.leftlist["equip_"+str(i)].setText("...")
                self.leftlist["equip_"+str(i)].show()

            self.refresh_right(selectedchar)

    def refresh_right(self, selectedchar: Pc.player):
        """
        Method called to refresh only the melee equipment in the right hand of the character

        :param selectedchar: the character displayed
        :return: None
        """
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
            self.rightlist["mastery_add"].show()
            self.rightlist["mastery_rm"].show()

            if type(right_equip) == Pc.MeleeEquip:
                if right_equip.is_hast():
                    meleelist[3] = "hast_bonus"
                statlist = right_equip.get_stats_aslist(meleelist)
                for i in range(7):
                    if i == 3 and meleelist[i] == "hast_bonus":
                        self.rightlist[str(i)].setText(self.tr("Bon. Hast"))
                    else:
                        self.rightlist[str(i)].setText(self.tr(self.meleelist[i]))
                    self.rightlist[str(i)].show()
                    self.rightlist["equip_" + str(i)].setText(str(statlist[i]))
                    self.rightlist["equip_" + str(i)].show()

            elif type(right_equip) == Pc.ShieldEquip:
                statlist = right_equip.get_stats_aslist(shieldlist)
                for i in range(7):
                    self.rightlist[str(i)].setText(self.tr(self.shieldlist[i]))
                    self.rightlist[str(i)].show()
                    self.rightlist["equip_" + str(i)].setText(str(statlist[i]))
                    self.rightlist["equip_" + str(i)].show()

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

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()

    def up_mastery(self, where: str, number: int):
        """
        Method called to manage the mastery the character has with its weapon

        :param where: "left" or "right", side of the weapon
        :param number: number to increase mastery by
        :return: None
        """
        selectedchar = self.parent().get_selectedchar()
        selectedchar.get_weapon(where, "melee").upmastery(number)

        if where == "left":
            self.leftlist["equip_4"].setText(str(selectedchar.get_weapon(where, "melee").get_stat("mastery")))
        else:
            self.rightlist["equip_4"].setText(str(selectedchar.get_weapon(where, "melee").get_stat("mastery")))

        self.save_character()
