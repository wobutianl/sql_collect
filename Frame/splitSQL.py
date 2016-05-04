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
## Class subMain
###########################################################################

import exeSQLPanel
import treeCtrl

class splitSQL ( wx.Panel ):

    def __init__( self, parent):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )

        topSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.exeSQL = exeSQLPanel.execSQL(self)
        self.treeCtrl = treeCtrl.treeCtrl(self, self.exeSQL.code_text)

        topSizer.Add(self.treeCtrl, 1, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(self.exeSQL, 3, wx.EXPAND | wx.ALL, 5)

        self.SetSizer( topSizer )
        self.Layout()

    def __del__( self ):
        pass

