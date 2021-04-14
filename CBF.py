import CCaF


class CharBundleFrame:
    """ Widget d'affichage de toutes les caractéristiques """

    def refresh(self):
        pass

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        pass
