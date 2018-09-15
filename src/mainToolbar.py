#! /usr/bin/env python3
# coding: utf-8
import wx

class MainToolbar(wx.ToolBar):
    def __init__(self, parent):
        """Create tool bar."""
        wx.ToolBar.__init__(self, parent)

        #self.AddTool(wx.ID_NEW, wx.Bitmap("images/new.png"))
        #self.SetToolShortHelp(wx.ID_NEW, 'New file')
        #self.Bind(wx.EVT_TOOL, parent.panel.on_new_menu_click, id=wx.ID_NEW)
        self.Realize()
