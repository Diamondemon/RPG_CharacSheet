from PySide6.QtCore import SIGNAL, Slot, Qt, QObject
from PySide6.QtWidgets import (QWidget, QLineEdit, QComboBox, QPushButton, QLabel, QGridLayout, QPlainTextEdit,
                               QCheckBox, QTableWidget)
from PySide6.QtGui import QIntValidator
import Perso_class as Pc
import CIF


class ObjCreatorFrame(QWidget):
    """ Widget de création des objets pour l'inventaire du personnage """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        # Widgets et variables nécessaires à la création de tout type d'objet
        self.genericValid = QIntValidator(0, 100, self)
        self.statValid = QIntValidator(-100, 100, self)

        self.Name_entry = QLineEdit()
        self.Description_entry = QPlainTextEdit()
        self.Stackable_entry = QCheckBox()
        self.ObjType = QComboBox()
        for key in ["Objet", "Arme de mélée", "Arme de jet", "Corde", "Bouclier", "Armure"]:
            self.ObjType.addItem(self.tr(key))
        self.ObjType.setEditable(False)
        self.ObjType.setCurrentIndex(0)
        self.connect(self.ObjType, SIGNAL("currentIndexChanged(int)"), self.change_obj_type)
        self.Register = QPushButton(self.tr("Ajouter"))
        self.connect(self.Register, SIGNAL("clicked()"), self.inventory_add)

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
        self.Melee = {"weight_QLabel": QLabel(self.tr("Type d'arme")), "hand_QLabel": QLabel(self.tr("Taille")),
                      "tr_QLabel": QLabel(self.tr("Tranchant")), "ctd_QLabel": QLabel(self.tr("Contondant")),
                      "estoc_QLabel": QLabel(self.tr("Estoc")), "hast_QLabel": QLabel(self.tr("Hast")),
                      "hast_bonus_QLabel": QLabel(self.tr("Bonus de hast")), "vit_QLabel": QLabel(self.tr("Vitesse")),
                      "quality_QLabel": QLabel(self.tr("Qualité")), "solidity_QLabel": QLabel(self.tr("Solidité")),
                      "weight_entry": QComboBox()}

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
        self.Melee["tr_entry"].setText("0")
        self.Melee["tr_entry"].setValidator(self.genericValid)
        self.Melee["tr_entry"].setAlignment(Qt.AlignCenter)
        self.Melee["ctd_entry"] = QLineEdit()
        self.Melee["ctd_entry"].setText("0")
        self.Melee["ctd_entry"].setValidator(self.genericValid)
        self.Melee["ctd_entry"].setAlignment(Qt.AlignCenter)
        self.Melee["estoc_entry"] = QLineEdit()
        self.Melee["estoc_entry"].setText("0")
        self.Melee["estoc_entry"].setValidator(self.genericValid)
        self.Melee["estoc_entry"].setAlignment(Qt.AlignCenter)
        self.Melee["hast_entry"] = QCheckBox()
        self.Melee["hast_bonus_entry"] = QLineEdit()
        self.Melee["hast_bonus_entry"].setText("0")
        self.Melee["hast_bonus_entry"].setValidator(self.statValid)
        self.Melee["hast_bonus_entry"].setAlignment(Qt.AlignCenter)
        self.Melee["vit_entry"] = QLineEdit()
        self.Melee["vit_entry"].setText("0")
        self.Melee["vit_entry"].setValidator(self.statValid)
        self.Melee["vit_entry"].setAlignment(Qt.AlignCenter)
        self.Melee["quality_entry"] = QLineEdit()
        self.Melee["quality_entry"].setText("0")
        self.Melee["quality_entry"].setValidator(self.genericValid)
        self.Melee["quality_entry"].setAlignment(Qt.AlignCenter)
        self.Melee["solidity_entry"] = QLineEdit()
        self.Melee["solidity_entry"].setText("0")
        self.Melee["solidity_entry"].setValidator(self.genericValid)
        self.Melee["solidity_entry"].setAlignment(Qt.AlignCenter)

        self.connect(self.Melee["hast_entry"], SIGNAL("stateChanged(int)"), self.hast_change)

        # dictionnaire de tous les widgets et variables pour la création d'arme de jet
        self.Throw = {"hand_QLabel": QLabel(self.tr("Taille")), "type_QLabel": QLabel(self.tr("Type")),
                      "dgt_QLabel": QLabel(self.tr("Dégats")), "pa_QLabel": QLabel(self.tr("Perce-armure")),
                      "solidity_QLabel": QLabel(self.tr("Solidité")), "scope": QTableWidget(),
                      "hand_entry": QComboBox()}

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
        self.Throw["dgt_entry"].setText("0")
        self.Throw["dgt_entry"].setValidator(self.genericValid)
        self.Throw["dgt_entry"].setMaximumWidth(40)
        self.Throw["dgt_entry"].setAlignment(Qt.AlignCenter)
        self.Throw["pa_entry"] = QLineEdit()
        self.Throw["pa_entry"].setText("0")
        self.Throw["pa_entry"].setValidator(self.genericValid)
        self.Throw["pa_entry"].setMaximumWidth(40)
        self.Throw["pa_entry"].setAlignment(Qt.AlignCenter)
        self.Throw["solidity_entry"] = QLineEdit()
        self.Throw["solidity_entry"].setText("0")
        self.Throw["solidity_entry"].setValidator(self.genericValid)
        self.Throw["solidity_entry"].setMaximumWidth(40)
        self.Throw["solidity_entry"].setAlignment(Qt.AlignCenter)
        self.Throw["scope"].setColumnCount(3)
        self.Throw["scope"].setHorizontalHeaderLabels([self.tr("Po. max"), self.tr("Vit."), self.tr("Préc.")])
        for column in range(3):
            self.Throw["scope"].setColumnWidth(column, 50)
        self.Throw["scope"].setRowCount(6)
        self.Throw["scope"].verticalHeader().hide()

        # widget pour le pourcentage de la corde
        self.Cord_QLabel = QLabel(self.tr("Casse (en %)"))
        self.Cord_entry = QLineEdit()
        self.Cord_entry.setText("0")
        self.Cord_entry.setValidator(self.genericValid)

        # dictionnaire de tous les widgets et variables pour la création de bouclier
        self.Shield = {"hand_QLabel": QLabel(self.tr("Taille")), "close_QLabel": QLabel(self.tr("Parade CàC")),
                       "dist_QLabel": QLabel(self.tr("Parade distance")), "mobi_QLabel": QLabel(self.tr("Mobilité")),
                       "vit_QLabel": QLabel(self.tr("Vitesse")), "quality_QLabel": QLabel(self.tr("Qualité")),
                       "solidity_QLabel": QLabel(self.tr("Solidité")), "hand_entry": QComboBox()}

        for key in ["1 main", "2 mains"]:
            self.Shield["hand_entry"].addItem(self.tr(key))
        self.Shield["hand_entry"].setEditable(False)
        self.Shield["hand_entry"].setCurrentIndex(0)
        self.Shield["close_entry"] = QLineEdit()
        self.Shield["close_entry"].setText("0")
        self.Shield["close_entry"].setValidator(self.genericValid)
        self.Shield["close_entry"].setAlignment(Qt.AlignCenter)
        self.Shield["dist_entry"] = QLineEdit()
        self.Shield["dist_entry"].setText("0")
        self.Shield["dist_entry"].setValidator(self.genericValid)
        self.Shield["dist_entry"].setAlignment(Qt.AlignCenter)
        self.Shield["mobi_entry"] = QLineEdit()
        self.Shield["mobi_entry"].setText("0")
        self.Shield["mobi_entry"].setValidator(self.statValid)
        self.Shield["mobi_entry"].setAlignment(Qt.AlignCenter)
        self.Shield["vit_entry"] = QLineEdit()
        self.Shield["vit_entry"].setText("0")
        self.Shield["vit_entry"].setValidator(self.statValid)
        self.Shield["vit_entry"].setAlignment(Qt.AlignCenter)
        self.Shield["quality_entry"] = QLineEdit()
        self.Shield["quality_entry"].setText("0")
        self.Shield["quality_entry"].setValidator(self.genericValid)
        self.Shield["quality_entry"].setAlignment(Qt.AlignCenter)
        self.Shield["solidity_entry"] = QLineEdit()
        self.Shield["solidity_entry"].setText("0")
        self.Shield["solidity_entry"].setValidator(self.genericValid)
        self.Shield["solidity_entry"].setAlignment(Qt.AlignCenter)

        # dictionnaire de tous les widgets et variables pour la création d'armure
        self.Armor = {"location_QLabel": QLabel(self.tr("Localisation")), "prot_QLabel": QLabel(self.tr("Protection")),
                      "amort_QLabel": QLabel(self.tr("Amortissement")), "mobi_QLabel": QLabel(self.tr("Mobilité")),
                      "vit_QLabel": QLabel(self.tr("Vitesse")), "solidity_QLabel": QLabel(self.tr("Solidité")),
                      "location_entry": QComboBox()}

        for key in ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette", "Cuissots",
                    "Grèves", "Solerets"]:
            self.Armor["location_entry"].addItem(self.tr(key))
        self.Armor["location_entry"].setEditable(False)
        self.Armor["location_entry"].setCurrentIndex(0)
        self.Armor["prot_entry"] = QLineEdit()
        self.Armor["prot_entry"].setText("0")
        self.Armor["prot_entry"].setValidator(self.genericValid)
        self.Armor["prot_entry"].setAlignment(Qt.AlignCenter)
        self.Armor["amort_entry"] = QLineEdit()
        self.Armor["amort_entry"].setText("0")
        self.Armor["amort_entry"].setValidator(self.genericValid)
        self.Armor["amort_entry"].setAlignment(Qt.AlignCenter)
        self.Armor["mobi_entry"] = QLineEdit()
        self.Armor["mobi_entry"].setText("0")
        self.Armor["mobi_entry"].setValidator(self.statValid)
        self.Armor["mobi_entry"].setAlignment(Qt.AlignCenter)
        self.Armor["vit_entry"] = QLineEdit()
        self.Armor["vit_entry"].setText("0")
        self.Armor["vit_entry"].setValidator(self.statValid)
        self.Armor["vit_entry"].setAlignment(Qt.AlignCenter)
        self.Armor["solidity_entry"] = QLineEdit()
        self.Armor["solidity_entry"].setText("0")
        self.Armor["solidity_entry"].setValidator(self.genericValid)
        self.Armor["solidity_entry"].setAlignment(Qt.AlignCenter)

        self.grid_all()
        self.clear()

    @Slot()
    def change_obj_type(self):
        """
        Method called to show the right widgets according to the selected type of object

        :return: None
        """
        self.clear()

        # listes des caractéristiques demandées pour chaque objet
        meleelist = ["weight", "hand", "tr", "ctd", "estoc", "hast", "quality", "solidity"]

        val = self.ObjType.currentIndex()

        if val == 1:
            for key in meleelist:
                self.Melee[key + "_QLabel"].show()
                self.Melee[key + "_entry"].show()
                if key == "hast":
                    if self.Melee["hast_entry"].isChecked():
                        key = "hast_bonus"
                        self.Melee[key + "_QLabel"].show()
                        self.Melee[key + "_entry"].show()
                    else:
                        key = "vit"
                        self.Melee[key + "_QLabel"].show()
                        self.Melee[key + "_entry"].show()

        elif val == 2:
            for widget in self.Throw.values():
                widget.show()

        elif val == 3:
            self.Cord_QLabel.show()
            self.Cord_entry.show()

        elif val == 4:
            for widget in self.Shield.values():
                widget.show()

        elif val == 5:
            for widget in self.Armor.values():
                widget.show()

    def clear(self):
        """
        Method called to hide all the non-generic widgets used for the creation of an object

        :return: None
        """
        for widget in self.Melee.values():
            widget.hide()

        for widget in self.Throw.values():
            widget.hide()

        for widget in self.Shield.values():
            widget.hide()

        for widget in self.Armor.values():
            widget.hide()

            self.Cord_entry.hide()
            self.Cord_QLabel.hide()

    def get_scope(self):
        """
        Method called to get the scope from the Throw[scope] tablewidget

        :return: None
        """
        scopelist = []
        for i in range(self.Throw["scope"].rowCount()):
            sublist = []
            for j in range(3):
                try:
                    value = int(self.Throw["scope"].item(i, j).text())
                    sublist.append(value)
                except ValueError:
                    return scopelist
            scopelist.append(sublist)
        return scopelist

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.Player)
        """
        return self.parent().get_selectedchar()

    def grid_all(self):
        """
        Method called to grid all the QLabels and QLineEdits for the creation of the object (once, at the __init__)

        :return: None
        """
        meleelist = ["weight", "hand", "tr", "ctd", "estoc", "hast", "quality", "solidity"]
        i = 0
        for key in meleelist:

            self.grid.addWidget(self.Melee[key + "_QLabel"], 3, i)
            self.grid.addWidget(self.Melee[key + "_entry"], 4, i)
            i += 1
            if key == "hast":
                key = "hast_bonus"
                self.grid.addWidget(self.Melee[key + "_QLabel"], 3, i)
                self.grid.addWidget(self.Melee[key + "_entry"], 4, i)
                key = "vit"
                self.grid.addWidget(self.Melee[key + "_QLabel"], 3, i)
                self.grid.addWidget(self.Melee[key + "_entry"], 4, i)
                i += 1

        throwlist = ["hand", "type", "dgt", "pa", "solidity"]
        i = 0
        for key in throwlist:
            self.grid.addWidget(self.Throw[key + "_QLabel"], 3, i)
            self.grid.addWidget(self.Throw[key + "_entry"], 4, i)
            i += 1
        self.grid.addWidget(self.Throw["scope"], 3, i, 3, 2)

        self.grid.addWidget(self.Cord_QLabel, 3, 0)
        self.grid.addWidget(self.Cord_entry, 3, 1)

        shieldlist = ["hand", "close", "dist", "mobi", "vit", "quality", "solidity"]
        i = 0
        for key in shieldlist:
            self.grid.addWidget(self.Shield[key + "_QLabel"], 3, i)
            self.grid.addWidget(self.Shield[key + "_entry"], 4, i)
            i += 1

        armorlist = ["location", "prot", "amort", "mobi", "vit", "solidity"]
        i = 0
        for key in armorlist:
            self.grid.addWidget(self.Armor[key + "_QLabel"], 3, i)
            self.grid.addWidget(self.Armor[key + "_entry"], 4, i)
            i += 1

    def hast_change(self):
        """
        Method called when switching between the creation of a hast weapon and a non-hast weapon

        :return: None
        """
        if self.Melee["hast_entry"].isChecked():
            self.Melee["vit_QLabel"].hide()
            self.Melee["vit_entry"].hide()

            self.Melee["hast_bonus_QLabel"].show()
            self.Melee["hast_bonus_entry"].show()

        else:
            self.Melee["hast_bonus_QLabel"].hide()
            self.Melee["hast_bonus_entry"].hide()

            self.Melee["vit_QLabel"].show()
            self.Melee["vit_entry"].show()

    @Slot()
    def inventory_add(self):
        """
        Method called to create the object and add it to the character's inventory

        :return: None
        """
        throwlist = ["Lancer", "Tir"]
        meleelist = ["Poings", "Légère", "Moyenne", "Lourde"]
        armorlist = ["Heaume", "Spallières", "Brassards", "Avant-bras", "Plastron", "Jointures", "Tassette",
                     "Cuissots", "Grèves", "Solerets"]

        new_obj = None

        val = self.ObjType.currentIndex()
        if self.Name_entry.text():
            if val == 0:
                new_obj = Pc.Obj(self.Name_entry.text(), self.Description_entry.toPlainText(),
                                 self.Stackable_entry.isChecked())

            elif val == 1:
                new_obj = Pc.MeleeEquip(self.Name_entry.text(), self.Description_entry.toPlainText(),
                                        self.Stackable_entry.isChecked(),
                                        meleelist[self.Melee["weight_entry"].currentIndex()],
                                        self.Melee["hast_entry"].isChecked())
                if self.Melee["hast_entry"].isChecked():
                    new_obj.upstats(self.Melee["hand_entry"].currentIndex() + 1, int(self.Melee["tr_entry"].text()),
                                    int(self.Melee["ctd_entry"].text()), int(self.Melee["estoc_entry"].text()),
                                    int(self.Melee["hast_bonus_entry"].text()))
                else:
                    new_obj.upstats(self.Melee["hand_entry"].currentIndex() + 1, int(self.Melee["tr_entry"].text()),
                                    int(self.Melee["ctd_entry"].text()), int(self.Melee["estoc_entry"].text()),
                                    int(self.Melee["vit_entry"].text()))

                new_obj.newquali(int(self.Melee["quality_entry"].text()))
                new_obj.upsolid(int(self.Melee["solidity_entry"].text()))

            elif val == 2:
                new_obj = Pc.ThrowEquip(self.Name_entry.text(), self.Description_entry.toPlainText(),
                                        self.Stackable_entry.isChecked(),
                                        throwlist[self.Throw["type_entry"].currentIndex()])
                new_obj.upstats(self.Throw["hand_entry"].currentIndex() + 1, int(self.Throw["dgt_entry"].text()),
                                int(self.Throw["pa_entry"].text()))
                new_obj.upsolid(int(self.Throw["solidity_entry"].text()))

                new_obj.newscope(self.get_scope())

            elif val == 3:
                new_obj = Pc.Cord(self.Name_entry.text(), self.Description_entry.toPlainText(),
                                  self.Stackable_entry.isChecked(),
                                  int(self.Cord_entry.text()))

            elif val == 4:
                new_obj = Pc.ShieldEquip(self.Name_entry.text(), self.Description_entry.toPlainText(),
                                         self.Stackable_entry.isChecked())
                new_obj.upstats(self.Shield["hand_entry"].currentIndex() + 1, int(self.Shield["close_entry"].text()),
                                int(self.Shield["dist_entry"].text()), int(self.Shield["mobi_entry"].text()),
                                int(self.Shield["vit_entry"].text()))
                new_obj.upsolid(int(self.Shield["solidity_entry"].text()))
                new_obj.newquali(int(self.Shield["quality_entry"].text()))

            elif val == 5:
                new_obj = Pc.ArmorEquip(self.Name_entry.text(), self.Description_entry.toPlainText(),
                                        self.Stackable_entry.isChecked(),
                                        armorlist[self.Armor["location_entry"].currentIndex()])
                new_obj.upstats(int(self.Armor["prot_entry"].text()), int(self.Armor["amort_entry"].text()),
                                int(self.Armor["mobi_entry"].text()), int(self.Armor["vit_entry"].text()))
                new_obj.upsolid(int(self.Armor["solidity_entry"].text()))

        if new_obj:
            self.get_selectedchar().invent_add(new_obj)  # par défaut, on gagne 1 objet et il n'est pas équipé
            self.parent().refresh()
            self.save_character()

    def parent(self) -> CIF.CharIFrame:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        return QWidget.parent(self)

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        self.parent().save_character()
