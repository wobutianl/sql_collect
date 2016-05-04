# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.richtext

###########################################################################
## Class addSQL
###########################################################################
from control import deligate

class addSQL ( wx.Panel ):

    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 230,300 ), style = wx.TAB_TRAVERSAL )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"level1", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )
        bSizer7.Add( self.m_staticText6, 0, wx.ALL, 5 )

        level_1_comboChoices = ['here','navinfo','tomtom','mid','tbl']
        self.level_1_combo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, level_1_comboChoices, 0 )
        bSizer7.Add( self.level_1_combo, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer7, 1, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"level2", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer10.Add( self.m_staticText7, 0, wx.ALL, 5 )

        level_2_comboChoices = []
        self.level_2_combo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, level_2_comboChoices,
                                          wx.CB_DROPDOWN | wx.TE_PROCESS_ENTER | wx.CB_SORT )
        bSizer10.Add( self.level_2_combo, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer10, 1, wx.EXPAND, 5 )

        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText81 = wx.StaticText( self, wx.ID_ANY, u"level3", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText81.Wrap( -1 )
        bSizer101.Add( self.m_staticText81, 0, wx.ALL, 5 )

        level_3_comboChoices = []
        self.level_3_combo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, level_3_comboChoices, 0 )
        bSizer101.Add( self.level_3_combo, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer101, 0, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"sql_name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )
        bSizer11.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.sql_name_text = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.sql_name_text, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer11, 1, wx.EXPAND, 5 )


        bSizer5.Add( bSizer6, 0, wx.EXPAND, 5 )

        self.add_code_text = wx.richtext.RichTextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0|wx.VSCROLL|wx.HSCROLL|wx.NO_BORDER|wx.WANTS_CHARS )
        bSizer5.Add( self.add_code_text, 1, wx.EXPAND |wx.ALL, 5 )

        self.add_code_btn = wx.Button( self, wx.ID_ANY, u"add", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer5.Add( self.add_code_btn, 0, wx.ALL, 5 )


        self.SetSizer( bSizer5 )
        self.Layout()

        # Connect Events
        self.level_1_combo.Bind(wx.EVT_COMBOBOX, self.GetLevel1Name)
        self.level_2_combo.Bind(wx.EVT_COMBOBOX, self.GetLevel2Name)
        self.level_3_combo.Bind(wx.EVT_COMBOBOX, self.GetLevel3Name)
        self.add_code_btn.Bind(wx.EVT_BUTTON, self.add_code_action)

        self.level_1_combo.Bind(wx.EVT_TEXT, self.l1_enter)
        self.level_2_combo.Bind(wx.EVT_TEXT, self.l2_enter)
        self.level_3_combo.Bind(wx.EVT_TEXT, self.l3_enter)

        self.shareData = deligate.ShareData()

    def __del__( self ):
        pass

    def l1_text(self, event):
        self.level1 = event.GetString()

    def l1_enter(self, event):
        self.level1 = event.GetString()
        event.Skip()

    def l2_enter(self, event):
        self.level2 = event.GetString()
        event.Skip()

    def l3_enter(self, event):
        self.level3 = event.GetString()
        event.Skip()

    # Virtual event handlers, overide them in your derived class
    def GetLevel1Name( self, event ):
        self.data = self.shareData.getData()

        level1_name = self.level_1_combo.GetStringSelection()
        level2_list = self.data.getLevel2(level1_name)
        for level2 in level2_list:
            self.level_2_combo.Append(level2)
        event.Skip()

    def GetLevel2Name( self, event ):
        level1_name = self.level_1_combo.GetStringSelection()
        level2_name = self.level_2_combo.GetStringSelection()
        if level2_name:
            level3_list = self.data.getLevel3(level1_name, level2_name)
            for level3 in level3_list:
                self.level_3_combo.Append(level3)
        else:
            self.level_3_combo.Append('')
        event.Skip()

    def GetLevel3Name( self, event ):
        event.Skip()

    def add_code_action( self, event ):
        level1 = self.level_1_combo.GetStringSelection()

        level2 = self.level_2_combo.GetStringSelection()
        if level2=='':
            level2 = self.level2

        level3 = self.level_3_combo.GetStringSelection()
        if level3=='' and self.level3:
            level3 =self.level3

        sql_name = self.sql_name_text.GetValue()
        sql = self.add_code_text.GetValue()

        add_flag = False
        if sql:
            if sql_name:
                self.data.insertSQL(level1, level2, level3, sql_name, sql)
                add_flag = True
            else:
                wx.MessageBox(" input this sql name first ")
        else:
            wx.MessageBox("input sql string first ")

        if add_flag :
            tree = self.shareData.getTree()
            tree.refresh_tree_list(tree.treeroot)
        event.Skip()


