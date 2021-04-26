import CDF


class CharNotebook:
    """ Widget that contains all the wigets used to display and manage the character """

    def get_competlist(self):
        """
        Method called to get the available competences

        :return: Reference to the list of competences
        """
        return self.parent().get_competlist()

    def get_selectedchar(self):
        """
        Method called to get the character to be displayed

        :return: the reference to the character
        """
        return self.parent().get_selectedchar()

    def get_spelllist(self):
        """
        Method called to get the available spells

        :return: Reference to the list of spells
        """
        return self.parent().get_spelllist()

    def handle_spells(self):
        """
        Method called to handle the display of the spell tab

        :return: None
        """
        pass

    def parent(self) -> CDF.CharDisplayFrame:
        """
        Method called to get the parent widget (the char display)

        :return: the reference to the parent
        """
        pass

    def refresh(self):
        """
        Method called to refresh all the widgets contained

        :return: None
        """
        pass

    def refresh_base(self):
        """
        Method called to refresh the base frame of the CharDisplay

        :return: None
        """
        pass

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        pass
