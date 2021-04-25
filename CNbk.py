import CDF


class CharNotebook:

    def get_competlist(self):
        """
        Method called to get the available competences

        :return: Reference to the list of competences
        """
        return self.parent().get_competlist()

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CDF.CharDisplayFrame:
        pass

    def refresh(self):
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
