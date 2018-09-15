#! /usr/bin/env python3
# coding: utf-8
import wx

from .mainPanel import MainPanel
from .menuBar import MenuBar
from .mainToolbar import MainToolbar
from .statusBar import StatusBar

class MainFrame(wx.Frame):
    """Create MainFrame class."""
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Basic wxPython module')
        self.panel = MainPanel(self)
        self.SetMenuBar(MenuBar(self))
        self.ToolBar = MainToolbar(self)
        self.status_bar = StatusBar(self).status_bar
        self.Bind(wx.EVT_CLOSE, self.panel.onQuit)
        self.SetSize((950, 600))
        self.Centre()
        self.Show()
