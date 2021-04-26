import CCaF


class CharBundleFrame:
    """ Widget to display all the caracteristics of the character """

    def get_selectedchar(self):
        """
        Method called to get the character selected to display

        :return: character (Perso_class.player)
        """
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

    def refresh_abi(self):
        """
        Method called to refresh only the ability frame

        :return: None
        """
        pass

    def refresh_atk(self):
        """
        Method called to refresh only the attack frame

        :return: None
        """
        pass

    def refresh_base(self):
        """
        Method called to refresh the base frame of the CharDisplay

        :return: None
        """
        pass

    def refresh_def(self):
        """
        Method called to refresh only the defense frame

        :return: None
        """
        pass

    def refresh_eth(self):
        """
        Method called to refresh only the magic frame

        :return: None
        """
        pass

    def refresh_phy(self):
        """
        Method called to refresh only the physical frame

        :return: None
        """
        pass

    def refresh_soc(self):
        """
        Method called to refresh only the social frame

        :return: None
        """
        pass
