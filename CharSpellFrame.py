from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QPushButton, QTreeWidget, QFrame, QComboBox, QLineEdit, \
    QPlainTextEdit
from functools import partial


class CharSpellFrame(QWidget):
    """ Widget de création des sorts """

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)
        self.selected_item = None
        self.selected_charitem = None
        self.spells_list = []

        """"""""""""""""""""""""""""METTTTTTTTTTTTTTTRRRRRRRRRREEEEEEEEEE ICONNNNNNNNNNNNNNEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"""""
        """self.lightning_image = ImageTk.PhotoImage(Image.open("Images/symb-lightning.png").resize((12, 15), Image.ANTIALIAS))"""

        self.elemlist = ["Foudre"]
        self.subcateglist = ["Emprise", "Appel", "Altération", "Transfert", "Divination", "Lien"]

        self.grid.addWidget(QLabel(self.tr("Sorts du personnage")), 0, 0)
        self.plus_lightning = QPushButton(self.tr("+"))
        self.plus_lightning.setDisabled(True)
        self.connect(self.plus_lightning, SIGNAL("clicked()"), partial(self.modif_lightning, 1))
        self.grid.addWidget(self.plus_lightning, 1, 6)
        self.min_lightning = QPushButton(self.tr("-"))
        self.min_lightning.setDisabled(True)
        self.connect(self.min_lightning, SIGNAL("clicked()"), partial(self.modif_lightning, -1))
        self.grid.addWidget(self.min_lightning, 1, 7)
        self.remove_choice = QPushButton(self.tr("Retirer"))
        self.remove_choice.setDisabled(True)
        self.connect(self.remove_choice, SIGNAL("clicked()"), self.remove_charspell)
        self.grid.addWidget(self.remove_choice, 2, 6, 1, 2)

        # les sorts que le personnage a déjà
        self.CharSpell_view = QTreeWidget()
        self.CharSpell_view.setHeaderLabels(["", self.tr("Effet"), self.tr("Description"), self.tr("Coût"),
                                              self.tr("Eclairs")])

        self.grid.addWidget(self.CharSpell_view, 1, 0, 3, 5)

        self.grid.addWidget(QLabel(self.tr("Sorts disponibles")), 4, 0)
        self.transfer_choice = QPushButton(self.tr("Prendre"))
        self.transfer_choice.setDisabled(True)
        self.connect(self.transfer_choice, SIGNAL("clicked()"), self.transfer_spell)
        self.grid.addWidget(self.transfer_choice, 5, 6, 1, 2)

        # les sorts qui existent
        self.Spell_view = QTreeWidget()
        self.Spell_view.setHeaderLabels(["", self.tr("Effet"), self.tr("Description"), self.tr("Coût")])

        self.grid.addWidget(self.Spell_view, 5, 0, 1, 5)

        # la FUUUU-SIOOOON de sorts

        separator = QFrame(self)
        separator.setFrameShape(QFrame.HLine)
        self.grid.addWidget(separator, 6, 0, 1, 8)

        self.grid.addWidget(QLabel(self.tr("Sort spécial")), 7, 0)
        self.grid.addWidget(QLabel(self.tr("Elément")), 8, 0)
        self.grid.addWidget(QLabel(self.tr("Sous-catégorie")), 8, 1)
        self.grid.addWidget(QLabel(self.tr("Nom")), 8, 2)
        self.grid.addWidget(QLabel(self.tr("Coût")), 8, 3)
        self.grid.addWidget(QLabel(self.tr("Effets")), 10, 0)
        self.grid.addWidget(QLabel(self.tr("Description")), 10, 2)

        self.Elem_entry = QComboBox()
        self.Elem_entry.addItems(self.elemlist)
        self.Elem_entry.setEditable(False)
        self.Elem_entry.setCurrentIndex(0)
        self.Subcateg_entry = QComboBox()
        self.Subcateg_entry.addItems(self.subcateglist)
        self.Subcateg_entry.setEditable(False)
        self.Subcateg_entry.setCurrentIndex(0)

        self.Name_entry = QLineEdit()
        self.Cost_entry = QLineEdit()
        self.Effect_entry = QPlainTextEdit()
        self.Description_entry = QPlainTextEdit()

        self.Special_register = QPushButton(self.tr("Enregistrer"))
        self.Special_register.setDisabled(True)
        self.connect(self.Special_register, SIGNAL("clicked()"), self.special_create)

        self.grid.addWidget(self.Elem_entry, 9, 0)
        self.grid.addWidget(self.Subcateg_entry, 9, 1)
        self.grid.addWidget(self.Name_entry, 9, 2)
        self.grid.addWidget(self.Cost_entry, 9, 3)
        self.grid.addWidget(self.Effect_entry, 11, 0, 1, 2)
        self.grid.addWidget(self.Description_entry, 11, 2, 1, 2)
        self.grid.addWidget(self.Special_register, 9, 4)

    def modif_lightning(self, number):
        pass

    def remove_charspell(self):
        pass

    def transfer_spell(self):
        pass

    def special_create(self):
        pass
