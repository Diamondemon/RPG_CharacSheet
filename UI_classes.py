import wx


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title)
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)


app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = MyFrame(None, "Multiline editor")  # A Frame is a top-level window.

app.MainLoop()
