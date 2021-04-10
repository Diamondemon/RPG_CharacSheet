from PySide6.QtCore import SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QGridLayout, QPlainTextEdit, QComboBox, QPushButton,
                               QTreeWidget, QTreeWidgetItem)
import Perso_class as Pc


class CharDisplayFrame(QWidget):
    """Affichage des statistiques d'un personnage"""

    def __init__(self):
        QWidget.__init__(self)
        self.grid = QGridLayout(self)

        self.selectedchar = None
        self.selected = ""  # Partie des caractéristiques sélectionnée
        self.subFrame_1 = QWidget(self)
        self.subFrame_1.setLayout(QGridLayout(self))
        self.subFrame_1.layout().addWidget(QLabel(self.tr("Personnage")), 0, 0)
        self.subFrame_1.layout().addWidget(QLabel(self.tr("Xp totale")), 1, 0)
        self.subFrame_1.layout().addWidget(QLabel(self.tr("Xp restante")), 2, 0)
        self.subFrame_1.layout().addWidget(QLabel(self.tr("Force")), 3, 0)
        self.subFrame_1.layout().addWidget(QLabel(self.tr("Gagner de l'xp")), 4, 0)
        self.New_xp = QLineEdit()
        self.New_xp.setText("0")
        self.subFrame_1.layout().addWidget(self.New_xp, 5, 0)
        self.subFrame_1.layout().addWidget(QLabel(self.tr("Gain MJ")), 6, 0)
        self.GM_wheel = QComboBox()
        self.GM_wheel.setEditable(False)
        self.New_GM = QLineEdit()
        self.New_GM.setText("0")
        self.subFrame_1.layout().addWidget(self.New_GM, 8, 0)

        self.plus_xp = QPushButton(self.tr("+"))
        self.plus_GM = QPushButton(self.tr("+"))
        self.subFrame_1.connect(self.plus_xp, SIGNAL("clicked()"), self.add_xp)
        self.subFrame_1.connect(self.plus_GM, SIGNAL("clicked()"), self.add_GM)

        self.restat_choice = QPushButton(self.tr("Restat"))
        self.connect(self.restat_choice, SIGNAL("clicked()"), self.reinit_char)
        self.grid.addWidget(self.restat_choice, 1, 0)
        self.GM_restat_choice = QPushButton(self.tr("Restat MJ"))
        self.connect(self.GM_restat_choice, SIGNAL("clicked()"), self.GM_reinit_char)
        self.grid.addWidget(self.GM_restat_choice, 2, 0)

        self.grid.addWidget(self.subFrame_1, 0, 0)


        """
        self.legal_scale = Scale(self.subFrame_1, label="Légal", orient="horizontal", from_=-50, to=50, length=150,
                                 tickinterval=25, showvalue='yes', command=self.legal_onMove)


        self.NBK = CharNotebook(self)"""

    def refresh(self, event=None):
        self.subFrame_1.layout().addWidget(QLabel(str(self.selectedchar.get_name())), 0, 1)
        self.subFrame_1.layout().addWidget(QLabel(str(self.selectedchar.totalxp)), 1, 1)
        self.subFrame_1.layout().addWidget(QLabel(str(self.selectedchar.xp)), 2, 1)
        self.subFrame_1.layout().addWidget(QLabel(str(self.selectedchar.secondstats["symb-strength"][0]) + "/" + str(
            self.selectedchar.secondstats["symb-strength"][1]) + " (" + str(
            self.selectedchar.secondstats["symb-strength"][2]) + ")"), 3, 1)
        self.GM_wheel.addItems(list(self.selectedchar.GMstats.keys()))
        self.GM_wheel.setCurrentIndex(0)
        self.subFrame_1.layout().addWidget(self.GM_wheel, 7, 0, 1, 2)
        self.subFrame_1.layout().addWidget(self.plus_xp, 5, 1)
        self.subFrame_1.layout().addWidget(self.plus_GM, 8, 1)
        """self.legal_scale.set(self.selectedchar.passivestats["legal"][0])
        self.legal_scale.grid(row=9, column=0, columnspan=2)
        self.NBK.CharCF.BNDL.SYM.refresh()"""

    def legal_onMove(self, value):
        self.selectedchar.change_passive("legal", int(value))

    def add_xp(self, event=None):
        self.selectedchar.upxp(int(self.New_xp.text()))
        self.refresh()

    def add_GM(self, event=None):
        self.selectedchar.GM_gain(self.GM_wheel.currentText(), int(self.New_GM.text()))
        self.refresh()

    def reinit_char(self):
        self.selectedchar.clearstats()
        self.NBK.refresh()

    def get_selectedchar(self):
        return self.selectedchar

    def GM_reinit_char(self):
        self.selectedchar.GM_clearstats()
        self.NBK.refresh()

    def set_selectedchar(self, character):
        if type(character == Pc.player):
            self.selectedchar = character