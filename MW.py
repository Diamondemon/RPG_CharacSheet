import Perso_class as Pc


class UIWindow:
    """ Fenêtre de base, ne contient que le nécessaire """

    def generate(self, name: str, xp: int, mage: bool):
        """
        Method called to create a new character for the user

        :param name: name of the character
        :param xp: experience points to give to the character
        :param mage: boolean indicating whether the character to create is a mage of not
        :return: None
        """
        pass

    def generate_competence(self, categ: str, subcateg: str, name: str, effect: str):
        """
        Method called to create a new competence

        :param categ: category of the competence
        :param subcateg: subcategory of the competence
        :param name: name of the competence
        :param effect: description and effect of the competence
        :return: None
        """
        pass

    def generate_spell(self, elem: str, subcateg: str, name: str, effect: str, description: str, cost: int):
        """
        Method called to create a new spell

        :param elem: element of the spell
        :param subcateg: subcategory of the spell
        :param name: name of the spell
        :param effect: effect of the spell
        :param description: lore descripton of the spell
        :param cost: points of mana needed to use the spell
        :return: None
        """
        pass

    def get_characlist(self) -> list[Pc.Player]:
        """
        Getter for the characlist attribute

        :return: Reference to the list of characters
        """
        pass

    def get_competlist(self) -> list[Pc.Competence]:
        """
        Getter for the competlist attribute

        :return: Reference to the list of competences
        """
        pass

    def get_spelllist(self) -> list[Pc.Spell]:
        """
        Getter for the spelllist attribute

        :return: Reference to the list of spells
        """
        pass

    def goto_compet(self):
        """
        Method called to display the CompetCreatorFrame (competence creator) as the central widget

        :return: None
        """
        pass

    def goto_create(self):
        """
        Method called to display the CharCFrame (character creator) as the central widget

        :return: None
        """
        pass

    def goto_home(self):
        """
        Method called to display the HomeFrame as the central widget

        :return: None
        """
        pass

    def goto_modify(self):
        """
        Method called to display the CharDisplayFrame and modify the selected character

        :return: None
        """
        pass

    def goto_spell(self):
        """
        Method called to display the SpellCreator Frame as the central widget

        :return: None
        """
        pass

    def goto_suppr(self):
        """
        Method to display the CharSFrame and delete characters

        :return: None
        """
        pass

    def import_char(self, characters_list: list[Pc.Player]):
        """
        Method called to add characters to the list

        :param characters_list: list of characters
        :return: None
        """
        pass

    def pop(self, index: int):
        """
        Method called to delete one character from the list

        :param index: index of the character to delete
        :return: None
        """
        pass

    def pop_compet(self, index: int):
        """
        Method called to delete one competence from the list

        :param index: index of the competence to delete
        :return: None
        """
        pass

    def pop_spell(self, index: int):
        """
        Method called to delete one spell from the list

        :param index: index of the spell to delete
        :return: None
        """
        pass

    def save_characlist(self):
        """
        Method called to save the list of characters

        :return: None
        """
        pass

    def save_competlist(self):
        """
        Method called to save the list of competences

        :return: None
        """
        pass

    def save_spelllist(self):
        """
        Method called to save the list of spells

        :return: None
        """
        pass

    def set_selectedchar(self, number: int):
        """
        Method called select the character to load and edit

        :param number: index of the character to select
        :return: None
        """
        pass
