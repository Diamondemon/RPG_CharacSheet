import CNbk


class CharCaracFrame:
    """Affichage des statistiques d'un personnage"""

    def refresh(self):
        pass

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CNbk.CharNotebook:
        pass
