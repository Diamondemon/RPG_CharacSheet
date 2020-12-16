import wx
from pickle import Unpickler  # , Pickler


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.characlist = []

        with open("characters", "rb") as file:
            self.characlist = Unpickler(file).load()

        self.CreateStatusBar()
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.menu = MainMenuBar()
        self.SetMenuBar(self.menu)
#        self.Bind(wx.EVT_MENU, self.problem, id=0)
        self.Show(True)

    def get_characlist(self):

        return self.characlist

    def problem(self, event):
        print("ouch")


class MainMenuBar(wx.MenuBar):

    def __init__(self, master=None):
        wx.MenuBar.__init__(self)
        self.master = master
        self.charmenu = wx.Menu()
        self.Append(self.charmenu, "Personnages")
        item = self.charmenu.Append(wx.ID_ANY, "Créer un personnage", "Ouvrir le menu de création des personnages")
        self.Bind(wx.EVT_MENU, self.goto_create, item)
        self.charmenu.AppendSeparator()

        for charac in self.get_characlist():
            item = self.charmenu.Append(wx.ID_ANY, charac.get_name(), "Afficher le personnage "+charac.get_name())
            self.Bind(wx.EVT_MENU)

    def get_characlist(self):

        return self.master.characlist

    def goto_create(self, event=None):
        print(self.get_characlist())


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame(None, "Multiline editor")  # A Frame is a top-level window.

app.MainLoop()
