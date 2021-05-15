import CNbk


class CharUsefulFrame:
    """ Widget representing the character sheet summed up """

    def refresh(self, event=None):
        """
        Method called to refresh all the statistics displayed in the widget

        :return: None
        """
        pass

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.Player)
        """
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
