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
## Class connectDBPanel
###########################################################################
from control import Global_param
from control import database_base
from control import deligate

class connectDBPanel ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 537,92 ), style = wx.TAB_TRAVERSAL )
        
        topSizer = wx.BoxSizer( wx.VERTICAL )
        
        choiceSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"IP", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        choiceSizer.Add( self.m_staticText9, 0, wx.ALL, 5 )
        
        host_comboChoices = [ u"172.26.185.139", u"192.168.8.18" ]
        self.host_combo = wx.ComboBox( self, wx.ID_ANY, u"172.26.185.139", wx.DefaultPosition, wx.DefaultSize, host_comboChoices, 0 )
        self.host_combo.SetSelection( 0 )
        choiceSizer.Add( self.host_combo, 0, wx.ALL, 5 )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Port", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        choiceSizer.Add( self.m_staticText10, 0, wx.ALL, 5 )
        
        m_choice2Choices = [ u"5432", u"35432" ]
        self.m_choice2 = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice2Choices, 0 )
        self.m_choice2.SetSelection( 0 )
        choiceSizer.Add( self.m_choice2, 0, wx.ALL, 5 )
        
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"comp", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        choiceSizer.Add( self.m_staticText11, 0, wx.ALL, 5 )
        
        vendor_comboChoices = [ u"here", u"sensis", u"zenrin", u"navinfo", u"mmi", u"tomtom" ]
        self.vendor_combo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, vendor_comboChoices, 0 )
        choiceSizer.Add( self.vendor_combo, 0, wx.ALL, 5 )
        
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"area", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        choiceSizer.Add( self.m_staticText12, 0, wx.ALL, 5 )
        
        area_comboChoices = [ u"bra", u"arg", u"twn", u"chn", u"ind", u"tha", u"sea", u"me8", u"saf8", u"sgp", u"mys", u"hkgmac", u"aus", u"sga" ]
        self.area_combo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, area_comboChoices, 0 )
        choiceSizer.Add( self.area_combo, 0, wx.ALL, 5 )
        
        
        topSizer.Add( choiceSizer, 1, wx.EXPAND, 5 )
        
        dbSizer = wx.BoxSizer( wx.HORIZONTAL )
        
        self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"db", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText21.Wrap( -1 )
        dbSizer.Add( self.m_staticText21, 0, wx.ALL, 5 )
        
        db_comboChoices = []
        self.db_combo = wx.ComboBox( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, db_comboChoices, 0 )
        self.db_combo.SetSelection( 0 )
        dbSizer.Add( self.db_combo, 1, wx.ALL, 5 )
        
        
        topSizer.Add( dbSizer, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( topSizer )
        self.Layout()
        
        # Connect Events
        self.host_combo.Bind( wx.EVT_COMBOBOX, self.GetHostSel )
        self.host_combo.Bind( wx.EVT_TEXT_ENTER, self.get_enter_host_action )
        self.m_choice2.Bind( wx.EVT_CHOICE, self.portChoice )
        self.vendor_combo.Bind( wx.EVT_COMBOBOX, self.GetVendorSel )
        self.vendor_combo.Bind( wx.EVT_TEXT_ENTER, self.get_enter_vendor_action )
        self.area_combo.Bind( wx.EVT_COMBOBOX, self.GetAreaSel )
        self.db_combo.Bind( wx.EVT_COMBOBOX, self.GetDbSel )
        self.db_combo.Bind( wx.EVT_TEXT_ENTER, self.get_enter_db_action )

        self.db = database_base.database()
        self.shareData = deligate.ShareData()
        self.fillVendor()
        self.host = ''
        self.vendor = ''
        self.area = ''
        self.db_name = ''
        self.port = ''
    
    def __del__( self ):
        pass
    
    def fillVendor(self):
        vendor_list = Global_param.vendor_area.keys()
        self.vendor_combo.Clear()
        for vendor in vendor_list:
            self.vendor_combo.Append(vendor)

    # Virtual event handlers, overide them in your derived class
    def GetHostSel( self, event ):
        # vendor_list = Global_param.vendor_area.keys()
        # for vendor in vendor_list:
        #     self.vendor_combo.Append(vendor)
        self.host = self.host_combo.GetStringSelection()
        event.Skip()
    
    def get_enter_host_action( self, event ):
        event.Skip()
    
    def portChoice( self, event ):
        self.port = self.m_choice2.GetStringSelection()
        event.Skip()
    
    def GetVendorSel( self, event ):
        self.vendor = self.vendor_combo.GetStringSelection()

        area_list = Global_param.vendor_area[self.vendor]
        self.area_combo.Clear()
        for area in area_list:
            self.area_combo.Append(area)
        event.Skip()
    
    def get_enter_vendor_action( self, event ):
        event.Skip()
    
    def GetAreaSel( self, event ):

        if self.host == '':
            self.host = self.host_combo.GetString(1)
        if self.port == '':
            self.port = '5432'

        # get all db name
        self.db.connect(self.host, self.port)
        db_name_list = self.db.get_db_name()

        # get db name list which with vendor name
        self.area = self.area_combo.GetStringSelection()
        for db_name in db_name_list:
            if db_name[0].lower().find(self.vendor) != -1 and db_name[0].lower().find(self.area) != -1:
                self.db_combo.Append(db_name[0])
        self.db.close()

        event.Skip()
    
    def GetDbSel( self, event ):
        self.db_name = self.db_combo.GetStringSelection()
        if self.host and self.db_name:
            self.db.connect(self.host, self.port, self.db_name)
            self.shareData.con_db = self.db
        else:
            wx.MessageBox(' u must choose host first')
        event.Skip()
    
    def get_enter_db_action( self, event ):
        event.Skip()
    

