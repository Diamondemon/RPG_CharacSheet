from PySide6.QtCore import Slot, SIGNAL
from PySide6.QtWidgets import (QWidget, QLineEdit, QLabel, QCheckBox, QGridLayout, QPushButton)


class SpellCreatorFrame(QWidget):
    """ Widget de création des sorts """

    def __init__(self):
        QWidget.__init__(self)
        """
        Label(self, text="Créer un sort").grid(row=0, column=0, sticky="w", columnspan=2)
        self.selected_item = None
        self.elemlist = ["Foudre"]
        self.subcateglist = ["Emprise", "Appel", "Altération", "Transfert", "Divination", "Lien"]
        self.Name_var = StringVar()
        self.Cost_var = IntVar()

        Label(self, text="Elément").grid(row=1, column=0, sticky="w")
        Label(self, text="Sous-catégorie").grid(row=1, column=1, sticky="w")
        Label(self, text="Nom").grid(row=1, column=2, sticky="w")
        Label(self, text="Effets").grid(row=3, column=0, sticky="w")
        Label(self, text="Description").grid(row=3, column=2, sticky="w")
        Label(self, text="Coût").grid(row=1, column=3, sticky="w")

        self.Elem_entry = ttk.Combobox(self, values=self.elemlist, state="readonly")
        self.Elem_entry.current(0)
        self.Subcateg_entry = ttk.Combobox(self, values=self.subcateglist, state="readonly")
        self.Subcateg_entry.current(0)
        self.Name_entry = Entry(self, textvariable=self.Name_var)
        self.Effect_entry = Text(self, width=50, height=5)
        self.Description_entry = Text(self, width=50, height=5)
        self.Cost_entry = Entry(self, textvariable=self.Cost_var)
        self.Register_choice = Button(self, text="Enregistrer", command=self.register)
        self.suppr_choice = Button(self, text="Supprimer", command=self.suppr, state="disabled")

        self.Elem_entry.grid(row=2, column=0, sticky="w", padx='4p')
        self.Subcateg_entry.grid(row=2, column=1, sticky="w", padx='4p')
        self.Name_entry.grid(row=2, column=2, sticky="w", padx='4p')
        self.Effect_entry.grid(row=4, column=0, padx='4p', columnspan=2, sticky="w")
        self.Cost_entry.grid(row=2, column=3, padx="4p", sticky="w")
        self.Description_entry.grid(row=4, column=2, padx='4p', columnspan=2, sticky="w")
        self.Register_choice.grid(row=2, column=4, rowspan=3, padx='4p')
        self.suppr_choice.grid(row=5, column=4, padx='4p')

        # les sorts qui existent déjà
        self.Spell_view = ttk.Treeview(self)
        self.Spell_view["columns"] = ("0", "1", "2")
        self.Spell_view.heading("0", text="Effet")
        self.Spell_view.heading("1", text="Description")
        self.Spell_view.heading("2", text="Coût")
        self.Spell_view.column("#0", width=110)
        self.Spell_view.column("0", width=400)
        self.Spell_view.column("1", width=400)
        self.Spell_view.column("2", width=50)
        # les catégories
        for key in self.elemlist:
            self.Spell_view.insert("", "end", key, text=key)

            for kkey in self.subcateglist:
                self.Spell_view.insert(key, "end", key+kkey, text=kkey)

        self.Spell_view.grid(row=5, column=0, columnspan=4, pady="8p", sticky="w")
        self.Spell_view.bind("<Button-1>", func=self.select_spell)


    def register(self):
        "" Méthode qui crée le nouveau sort ""
        new_spell = pc.Spell(self.Elem_entry.get(), self.Subcateg_entry.get(), self.Name_var.get(), self.Effect_entry.get(0.0, "end"), self.Description_entry.get(0.0, "end"), self.Cost_var.get())

        self.master.spelllist.append(new_spell)
        self.Spell_view.insert(new_spell.elem+new_spell.subcateg, "end", (len(self.master.spelllist)), text=new_spell.name, values=[new_spell.effect, new_spell.description, new_spell.cost])

    def refresh(self):
        "" Méthode qui rafraîchit la liste des sorts ""

        for key in self.elemlist:
            for kkey in self.subcateglist:
                for i in self.Spell_view.get_children(key+kkey):
                    self.Spell_view.delete(i)

        if self.master.spelllist:
            i = 1
            for key in self.master.spelllist:
                self.Spell_view.insert(key.elem+key.subcateg, "end", i, text=key.name, values=[key.effect,key.description,key.cost])

                i += 1

    def select_spell(self,event):
        "" Méthode qui est appelée quand on sélectionne une compétence, pour ensuite la supprimer si besoin ""
        if self.Spell_view.identify_row(event.y):

            try:
                self.selected_item = int(self.Spell_view.identify_row(event.y))
                self.suppr_choice["state"] = "normal"

            except:
                self.selected_item = None
                self.suppr_choice["state"] = "disabled"

        else:
            self.selected_item = None
            self.suppr_choice["state"] = "disabled"

    def suppr(self):
        "" Méthode qui supprime la compétence sélectionnée ""
        if type(self.selected_item) == int:
            self.master.spelllist.pop(self.selected_item-1)
            self.refresh()
            self.selected_item = None
            self.suppr_choice["state"] = "disabled"

    def grid(self, **kw):
        Frame.grid(self, **kw)
        self.refresh()"""