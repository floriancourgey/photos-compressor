#! /usr/bin/env python3
# coding: utf-8
import wx

class StatusBar(object):
    def __init__(self, parent):
        """Create status bar."""
        self.status_bar = parent.CreateStatusBar()
