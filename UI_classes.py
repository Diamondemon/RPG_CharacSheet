import wx
from pickle import Unpickler  # , Pickler


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.characlist = []
        self.selectedchar = None

        with open("characters", "rb") as file:
            self.characlist = Unpickler(file).load()

        self.CreateStatusBar()
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.menu = MainMenuBar(self)
        self.SetMenuBar(self.menu)
        self.Show(True)

    def get_characlist(self):

        return self.characlist

    def get_selectedchar(self):

        return self.selectedchar

    def launch_charedit(self, index):

        self.selectedchar = self.characlist[index]

    def login(self):
        pass


class MainMenuBar(wx.MenuBar):

    def __init__(self, master=None):
        wx.MenuBar.__init__(self)
        self.master = master
        self.charmenu = wx.Menu()
        self.Append(self.charmenu, "Personnages")
        item = self.charmenu.Append(wx.ID_ANY, "Créer un personnage", "Ouvrir le menu de création des personnages")
        self.Bind(wx.EVT_MENU, self.goto_create, item)
        self.charmenu.AppendSeparator()
        self.refresh()

    def get_characlist(self):

        return self.master.characlist

    def goto_charedit(self, _event, index):

        print("On part sur le perso", index)
        self.master.launch_charedit(index)

    def goto_create(self, _event=None):
        self.refresh()

    def goto_login(self,_event=None):
        self.master.login()

    def refresh(self):

        for i in range(self.charmenu.GetMenuItemCount()-1, 1, -1):
            item = self.charmenu.FindItemByPosition(i)
            self.Unbind(wx.EVT_MENU, item)
            self.charmenu.DestroyItem(item)

        i = 0
        for charac in self.get_characlist():
            item = self.charmenu.Append(wx.ID_ANY, charac.get_name(), "Afficher le personnage " + charac.get_name())
            self.Bind(wx.EVT_MENU, lambda event, temp=i: self.goto_charedit(event, temp), item)
            i += 1


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame(None, "Multiline editor")  # A Frame is a top-level window.

app.MainLoop()
