#! /usr/bin/env python3
# coding: utf-8
import wx

class MenuBar(wx.MenuBar):
    """Create the menu bar class."""
    def __init__(self, parent):
        wx.MenuBar.__init__(self)
        # file
        fileMenu = wx.Menu()
        mi = fileMenu.Append(wx.ID_OPEN, '&Open\tCtrl+O')
        self.Bind(wx.EVT_MENU, self.onOpen, mi)
        mi = fileMenu.Append(wx.ID_EXIT, '&Quit\tCtrl+Q')
        self.Bind(wx.EVT_MENU, self.onQuit, mi)
        # tools
        toolsMenu = wx.Menu()
        mi = toolsMenu.Append(wx.NewIdRef(), 'Count occurences')
        self.Bind(wx.EVT_MENU, self.onCountOccurences, mi)
        # help
        helpMenu = wx.Menu()
        mi = helpMenu.Append(wx.ID_ABOUT)
        self.Bind(wx.EVT_MENU, self.onAbout, mi)

        self.Append(fileMenu, '&File')
        self.Append(toolsMenu, 'Tools')
        self.Append(helpMenu, "&Help")

    def onOpen(self, e):
        pass
    def onQuit(self, e):
        pass
    def onCountOccurences(self, e):
        pass
    def onAbout(self, e):
        pass
