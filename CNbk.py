import CDF


class CharNotebook:

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
        Method called to get the available competences

        :return: Reference to the list of competences
        """
        return self.parent().get_spelllist()

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
