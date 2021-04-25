import CNbk


class CharIFrame:
    """Inventaire d'un personnage"""

    def refresh(self):
        """
         Method called to refresh the content of the character's inventory

        :return: None
        """
        pass

    def unselect_previous(self):
        """ Désélectionne l'item précédent """
        pass

    def obj_options(self):
        pass

    def melee_options(self):
        pass

    def throw_options(self):
        pass

    def shield_options(self):
        pass

    def armor_options(self):
        pass

    def import_obj(self):
        """
        Slot called to import objects created by other users

        :return: None
        """
        pass

    def export_obj(self):
        """
        Slot called to export characters created to share them with other users

        :return: None
        """
        pass

    def change_number(self, number):
        pass

    def suppr_obj(self):
        pass

    def equip_item(self, where=""):
        pass

    def unequip_item(self):
        pass

    def equip_cord(self, where):
        pass

    def change_solid(self, number):
        pass

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
        return self.parent().get_selectedchar()

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the CharUsefulFrame)

        :return: the reference to the parent
        """
        pass

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        pass
