import CNbk


class CharUsefulFrame:
    """ Fiche personnage résumée """

    def refresh(self, event=None):
        pass

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CNbk.CharNotebook:
        """
        Method called to get the parent widget (the Notebook)

        :return: the reference to the parent
        """
        pass

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        pass
