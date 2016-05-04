# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyPanel10
###########################################################################
import connectDB
import addSQL
import splitSQL


class subMain(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.topSizer = wx.BoxSizer(wx.VERTICAL)

        self.connectDB = connectDB.connectDBPanel(self)
        self.topSizer.Add(self.connectDB, 0, wx.EXPAND | wx.ALL, 5)

        self.sqlSizer = wx.BoxSizer(wx.HORIZONTAL)


        self.splitSQL = splitSQL.splitSQL(self)
        self.sqlSizer.Add(self.splitSQL, 2, wx.ALL | wx.EXPAND, 5)

        self.AddSQL = addSQL.addSQL(self)
        self.AddSQL.Hide()

        self.sqlSizer.Add(self.AddSQL, 1, wx.EXPAND | wx.ALL, 5)

        self.topSizer.Add(self.sqlSizer, 1, wx.EXPAND, 5)

        self.SetSizer(self.topSizer)
        self.Layout()

    def __del__(self):
        pass

