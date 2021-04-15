import Perso_class as Pc
import MW


class CharDisplayFrame:
    """Affichage des statistiques d'un personnage"""

    def add_GM(self):
        pass

    def add_xp(self):
        pass

    def get_selectedchar(self) -> Pc.player:
        pass

    def GM_reinit_char(self):
        pass

    def legal_onMove(self, value: int):
        pass

    def parent(self) -> MW.UIWindow:
        """
        Method called to get the parent widget (the main window)

        :return: the reference to the parent
        """
        pass

    def refresh(self):

        pass

    def refresh_base(self):
        """
        Method called to refresh only the base frame

        :return: None
        """
        pass

    def reinit_char(self):
        pass

    def set_selectedchar(self, character: Pc.player):
        pass
