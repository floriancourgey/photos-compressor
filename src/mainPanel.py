#! /usr/bin/env python3
# coding: utf-8
import os
import wx
from PIL import Image, ExifTags
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk

class MainPanel(wx.Panel):
    """Create a panel class to contain screen widgets."""
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        # init
        self.folder = os.getcwd()
        self.images = []
        # UI
        self.initUI()
    def initUI(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        # folder line 1
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(wx.StaticText(self, label='Folder'))
        self.folderWx = wx.TextCtrl(self, value=self.folder)
        hbox.Add(self.folderWx, 1, wx.ALL)
        x = wx.Button(self, label="Open Folder")
        x.Bind(wx.EVT_BUTTON, self.onOpenDirectory)
        hbox.Add(x)
        sizer.Add(hbox, 1, wx.EXPAND)
        # load
        x = wx.Button(self, wx.NewIdRef(), "Load files to view")
        self.Bind(wx.EVT_BUTTON, self.onLoad, x)
        # sizer.Add(x)
        # files list
        self.list_ctrl = wx.ListCtrl(self,
                                     style=wx.LC_REPORT
                                     |wx.BORDER_SUNKEN
                                     )
        columns = ['Name', 'Format', 'Width', 'Height', 'Mode', 'Size']
        for i,column in enumerate(columns):
            self.list_ctrl.InsertColumn(i, column)

        sizer.Add(self.list_ctrl, 1, wx.ALL|wx.EXPAND, 5)
        # Compress
        x = wx.Button(self, wx.NewIdRef(), "Generate")
        self.Bind(wx.EVT_BUTTON, self.onGenerate, x)
        sizer.Add(x)
        # quit
        cmd_quit = wx.Button(self, id=wx.ID_EXIT)
        cmd_quit.Bind(wx.EVT_BUTTON, self.onQuit)
        sizer.Add(cmd_quit)
        self.SetSizerAndFit(sizer)

    def onOpenDirectory(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:")
        dlg.SetPath(self.folder) # default its path to the current path
        if dlg.ShowModal() == wx.ID_OK:
            self.folder = dlg.GetPath()
            self.folderWx.SetValue(self.folder)
        dlg.Destroy()

    def onLoad(self, event):
        self.folder = self.folderWx.GetValue()
        self.images = []
        self.list_ctrl.DeleteAllItems()
        for root, dirs, files in os.walk(self.folder):
            for file in files:
                try:
                    print('Found file', file)
                    im = Image.open(file)
                    self.images.append(im)
                    print('Image OK')
                except IOError as e:
                    print('But not an image')
                    continue
        if len(self.images) == 0:
            print('ShowModal')
            dlg = wx.MessageDialog(self, "No images found", "No images")
            dlg.ShowModal()
            return
        for index, im in enumerate(self.images):
            self.list_ctrl.InsertItem(index, "")
            values = [im.filename, im.format, str(im.size[0]), str(im.size[1]),
                im.mode,
                str(int(os.path.getsize(im.filename)/1000))+' kb'
            ]
            for i,value in enumerate(values):
                self.list_ctrl.SetItem(index, i, value)
    def onGenerate(self, event):
        pass
    def onQuit(self, event):
        del event
        quit()
