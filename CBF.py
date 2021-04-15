import CCaF


class CharBundleFrame:
    """ Widget d'affichage de toutes les caractéristiques """

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def modify_abi(self):
        """
        Method called to modify the travelling statistics of the character

        :return: None
        """
        pass

    def modify_atk(self):
        """
        Method called to modify the offensive statistics of the character

        :return: None
        """
        pass

    def modify_def(self):
        """
        Method called to modify the defensive statistics of the character

        :return: None
        """
        pass

    def modify_eth(self):
        """
        Method called to modify the magical statistics of the character

        :return: None
        """
        pass

    def modify_phy(self):
        """
        Method called to modify the physical statistics of the character

        :return: None
        """
        pass

    def modify_soc(self):
        """
        Method called to modify the social statistics of the character

        :return: None
        """
        pass

    def parent(self) -> CCaF.CharCaracFrame:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        pass

    def refresh(self):
        pass
