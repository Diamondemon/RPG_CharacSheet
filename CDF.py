import Perso_class as Pc
import MW


class CharDisplayFrame:
    """Affichage des statistiques d'un personnage"""

    def add_GM(self):
        """
        Method called when the Game Master wants to give points into specific stats

        :return: None
        """
        pass

    def add_xp(self):
        """
        Method called to give experience points to the character

        :return: None
        """
        pass

    def get_competlist(self):
        """
        Method called to get the available competences

        :return: Reference to the list of competences
        """
        return self.parent().get_competlist()

    def get_selectedchar(self) -> Pc.Player:
        """
        Method called to get the character to be displayed

        :return: the reference to the character
        """
        pass

    def get_spelllist(self):
        """
        Method called to get the available spells

        :return: Reference to the list of spells
        """
        return self.parent().get_spelllist()

    def GM_reinit_char(self):
        """
        Method called to reset all the stats given to the character by the Game Master in specific stats.

        :return: None
        """
        pass

    def legal_onMove(self, value: int):
        """
        Method called when the value of the legal stat is changed through the QSlider

        :param value: new value to register
        :return: None
        """
        pass

    def parent(self) -> MW.UIWindow:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        pass

    def refresh(self):
        """
        Method called to refresh all the widgets displaying the stats of the character

        :return: None
        """
        pass

    def refresh_base(self):
        """
        Method called to refresh only the base frame

        :return: None
        """
        pass

    def reinit_char(self):
        """
        Method called to reset all the statistics of the displayed character

        :return: None
        """
        pass

    def save_character(self):
        """
        Method called to save the character

        :return: None
        """
        pass

    def set_selectedchar(self, character: Pc.Player):
        """
        Method called to select the character to load and edit

        :param character: character to load
        :return: None
        """
        pass
