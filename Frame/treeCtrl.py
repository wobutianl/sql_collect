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
## Class treeCtrl
###########################################################################
import control.read_file
from control import deligate

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class treeCtrl ( wx.Panel ):

    def __init__( self, parent, code_text ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 121,300 ), style = wx.TAB_TRAVERSAL )

        bSizer129 = wx.BoxSizer( wx.VERTICAL )

        self.kind_tree = wx.TreeCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE )
        bSizer129.Add( self.kind_tree, 2, wx.ALL|wx.EXPAND, 5 )

        self.m_searchCtrl1 = wx.SearchCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_searchCtrl1.ShowSearchButton( True )
        self.m_searchCtrl1.ShowCancelButton( True )
        bSizer129.Add( self.m_searchCtrl1, 0, wx.EXPAND, 5 )

        serch_resultChoices = []
        self.serch_result = wx.Choice(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, serch_resultChoices, 0)
        self.serch_result.SetSelection(0)
        bSizer129.Add(self.serch_result, 0, wx.ALL|wx.EXPAND, 5)

        self.SetSizer( bSizer129 )
        self.Layout()

        # Connect Events
        self.kind_tree.Bind( wx.EVT_TREE_ITEM_RIGHT_CLICK, self.delete_item )
        self.kind_tree.Bind( wx.EVT_TREE_SEL_CHANGED, self.get_selected_item )
        self.m_searchCtrl1.Bind( wx.EVT_TEXT, self.search )

        self.m_searchCtrl1.Bind(wx.EVT_SEARCHCTRL_CANCEL_BTN, self.cancel_search)
        self.m_searchCtrl1.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.sure_search)
        self.serch_result.Bind(wx.EVT_CHOICE, self.search_choice)

        self.treeroot = self.kind_tree.AddRoot(r'sql_list')
        self.read_file = control.read_file.getData()
        # self.tree_list = read_file.read_sql_txt(Global_param.tree_path)

        # fill the tree list
        self.shareData = deligate.ShareData()
        self.shareData.setTree(self)
        self.refresh_tree_list(self.treeroot)
        self.code_text = code_text


    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class

    def delete_item( self, event ):
        item = event.GetItem()
        if self.kind_tree.ItemHasChildren(item) == False:
            list_heritage = self.ItemText(item)
            if list_heritage:
                dlg = wx.MessageDialog(None, " this will delete this sql ",
                                       "MessageDialog", wx.YES_NO | wx.ICON_QUESTION)
                if dlg.ShowModal() == wx.ID_YES:
                    if list_heritage.__len__() == 3:
                        self.read_file.delSQL(list_heritage[2], list_heritage[1], '', name=list_heritage[0])
                    elif list_heritage.__len__() == 4:
                        self.read_file.delSQL(list_heritage[3], list_heritage[2], list_heritage[1],
                                                          list_heritage[0])
            self.refresh_tree_list(self.treeroot)
        event.Skip()

    def get_selected_item( self, event ):
        # show sql in the code_text
        item = event.GetItem()
        if self.kind_tree.ItemHasChildren(item)==False:
            self.list_heritage = self.ItemText(item)
            # print self.list_heritage
            sql = self.GetTreeItemValue(self.list_heritage)

            if self.list_heritage.__len__()==3:
                self.shareData.setL1(self.list_heritage[2])
                self.shareData.setL2(self.list_heritage[1])
                self.shareData.setL3('0')
                self.shareData.setName(self.list_heritage[0])
            if sql:
                self.code_text.SetValue(sql)
        event.Skip()

    def GetTreeItemValue(self, list_heritage):
        value = []
        if list_heritage:
            if list_heritage.__len__() == 3:
                value = self.read_file.getSQLInfo(list_heritage[2], list_heritage[1], '', name=list_heritage[0])
            elif list_heritage.__len__() == 4:
                value = self.read_file.getSQLInfo(list_heritage[3], list_heritage[2], list_heritage[1], list_heritage[0])
        else:
            value = ['']
        return value[0]
        pass

    def ItemText(self, item):
        if item and item != self.kind_tree.GetRootItem():
            str = []
            str.append(self.kind_tree.GetItemText(item))

            while self.kind_tree.GetItemParent(item) != self.kind_tree.GetRootItem():
                item = self.kind_tree.GetItemParent(item)
                str.append(self.kind_tree.GetItemText(item))
            return str
        else:
            ''

    def search( self, event ):
        self.search_string = event.GetString()
        event.Skip()

    def cancel_search(self, event):
        self.m_searchCtrl1.Clear()
        event.Skip()

    def sure_search(self, event):
        search_string = self.m_searchCtrl1.GetValue()
        self.search_result_string = {}
        for name in self.data:
            if name[4].find(search_string) != -1:
                key = name[4] + '('+name[2]+','+name[1]+')'
                key = key.encode('utf-8')
                self.search_result_string[key]=name[5]
                self.serch_result.Append(key)
        event.Skip()

    def search_choice(self, event):
        key = event.GetString()
        key = key.encode('utf-8')
        self.code_text.SetValue(self.search_result_string[key])
        event.Skip()

    def AddItem(self, root, sql_list):
        # add items to tree
        for (key, value) in sql_list.items():
            if isinstance(value, dict):
                child = self.kind_tree.AppendItem(root, key)
                self.AddItem(child, value)
            else:
                child = self.kind_tree.AppendItem(root, key)

    def refresh_tree_list(self, root):
        # fill the tree list
        self.data = self.read_file.getAllData()
        self.shareData.setData(self.read_file)
        if self.kind_tree.GetCount() != 1:
            self.kind_tree.DeleteAllItems()
            self.treeroot = self.kind_tree.AddRoot(r'sql_list')
        self.AddItem(root, self.read_file.getTreeDict())