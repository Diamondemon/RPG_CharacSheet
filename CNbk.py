import CDF


class CharNotebook:

    def refresh(self):
        pass

    def get_selectedchar(self):
        return self.parent().get_selectedchar()

    def parent(self) -> CDF.CharDisplayFrame:
        pass
