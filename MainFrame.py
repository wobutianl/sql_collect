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
import wx.grid
import GenericTable

import Global_param
import read_file
import database_base
###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent = None ):
        self.db = database_base.database()

        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1000, 532), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        bSizer1 = wx.BoxSizer(wx.VERTICAL)  # main frame

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)    # connect to db



        bSizer1.Add(bSizer2, 0, wx.EXPAND, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)  # (tree + code + add sql ) frame

        bSizer3.Add(self.kind_tree, 1, wx.ALL | wx.EXPAND, 5)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)

        self.code_text = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                                  0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        bSizer4.Add(self.code_text, 2, wx.EXPAND | wx.ALL, 5)

        self.result_grid = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        # self.result_grid.CreateGrid(5, 5)
        self.result_grid.EnableEditing(True)
        self.result_grid.EnableGridLines(True)
        self.result_grid.EnableDragGridSize(False)
        self.result_grid.SetMargins(0, 0)

        # Columns
        self.result_grid.EnableDragColMove(False)
        self.result_grid.EnableDragColSize(True)
        self.result_grid.SetColLabelSize(30)
        self.result_grid.SetColLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Rows
        self.result_grid.EnableDragRowSize(True)
        self.result_grid.SetRowLabelSize(80)
        self.result_grid.SetRowLabelAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)

        # Label Appearance

        # Cell Defaults
        self.result_grid.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer4.Add(self.result_grid, 1, wx.ALL | wx.EXPAND, 5)

        bSizer3.Add(bSizer4, 2, wx.EXPAND, 5)

        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        bSizer6 = wx.BoxSizer(wx.VERTICAL)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText6 = wx.StaticText(self, wx.ID_ANY, u"level1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText6.Wrap(-1)
        bSizer7.Add(self.m_staticText6, 0, wx.ALL, 5)

        level_1_comboChoices = []
        self.level_1_combo = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         level_1_comboChoices, 0)
        bSizer7.Add(self.level_1_combo, 0, wx.ALL, 5)

        bSizer6.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer10 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText7 = wx.StaticText(self, wx.ID_ANY, u"level2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText7.Wrap(-1)
        bSizer10.Add(self.m_staticText7, 0, wx.ALL, 5)

        level_2_comboChoices = []
        self.level_2_combo = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         level_2_comboChoices, 0)
        bSizer10.Add(self.level_2_combo, 0, wx.ALL, 5)

        bSizer6.Add(bSizer10, 1, wx.EXPAND, 5)

        bSizer101 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText81 = wx.StaticText(self, wx.ID_ANY, u"level3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText81.Wrap(-1)
        bSizer101.Add(self.m_staticText81, 0, wx.ALL, 5)

        level_3_comboChoices = []
        self.level_3_combo = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                         level_3_comboChoices, 0)
        bSizer101.Add(self.level_3_combo, 0, wx.ALL, 5)

        bSizer6.Add(bSizer101, 0, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText8 = wx.StaticText(self, wx.ID_ANY, u"sql_name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText8.Wrap(-1)
        bSizer11.Add(self.m_staticText8, 0, wx.ALL, 5)

        self.sql_name_text = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer11.Add(self.sql_name_text, 0, wx.ALL, 5)

        bSizer6.Add(bSizer11, 1, wx.EXPAND, 5)

        bSizer5.Add(bSizer6, 0, wx.EXPAND, 5)

        self.add_code_text = wx.richtext.RichTextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                      wx.DefaultSize,
                                                      0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        bSizer5.Add(self.add_code_text, 1, wx.EXPAND | wx.ALL, 5)

        self.add_code_btn = wx.Button(self, wx.ID_ANY, u"add", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer5.Add(self.add_code_btn, 0, wx.ALL, 5)

        bSizer3.Add(bSizer5, 1, wx.EXPAND, 5)

        bSizer1.Add(bSizer3, 1, wx.EXPAND, 5)

        self.SetSizer(bSizer1)
        self.Layout()
        self.m_toolBar2 = self.CreateToolBar(wx.TB_HORIZONTAL, wx.ID_ANY)
        self.m_tool1 = self.m_toolBar2.AddLabelTool(wx.ID_ANY, u"tool",
                                                    wx.Bitmap(r"d:\TEST\sql_collect\sql_file\UserHeadTemp.bmp",
                                                              wx.BITMAP_TYPE_ANY), wx.NullBitmap, wx.ITEM_NORMAL,
                                                    wx.EmptyString, wx.EmptyString, None)

        self.m_toolBar2.Realize()

        self.Centre(wx.BOTH)

        # Connect Events
        self.host_combo.Bind(wx.EVT_COMBOBOX, self.GetHostSel)
        self.host_combo.Bind(wx.EVT_TEXT_ENTER, self.get_enter_host_action)
        self.vendor_combo.Bind(wx.EVT_COMBOBOX, self.GetVendorSel)
        self.vendor_combo.Bind(wx.EVT_TEXT_ENTER, self.get_enter_vendor_action)
        self.area_combo.Bind(wx.EVT_COMBOBOX, self.GetAreaSel)
        self.db_combo.Bind(wx.EVT_COMBOBOX, self.GetDbSel)
        self.db_combo.Bind(wx.EVT_TEXT_ENTER, self.get_enter_db_action)
        self.connect_btn.Bind(wx.EVT_BUTTON, self.connect_db_action)
        self.kind_tree.Bind(wx.EVT_TREE_ITEM_RIGHT_CLICK, self.delete_item)
        self.kind_tree.Bind(wx.EVT_TREE_SEL_CHANGED, self.get_selected_item)
        self.code_text.Bind(wx.EVT_KEY_DOWN, self.run_code_action)
        self.level_1_combo.Bind(wx.EVT_COMBOBOX, self.GetLevel1Name)
        self.level_2_combo.Bind(wx.EVT_COMBOBOX, self.GetLevel2Name)
        self.level_3_combo.Bind(wx.EVT_COMBOBOX, self.GetLevel3Name)
        self.add_code_btn.Bind(wx.EVT_BUTTON, self.add_code_action)

        self.Bind(wx.EVT_TOOL, self.backup_action, id=self.m_tool1.GetId())

        self.treeroot = self.kind_tree.AddRoot(r'sql_list')
        self.tree_list = read_file.read_sql_txt(Global_param.tree_path)
        # fill the level1
        level1 = self.GetDictLevel1(self.tree_list)
        for key in level1:
            self.level_1_combo.Append(key)

        # fill the tree list
        self.refresh_tree_list(self.treeroot)

    def createToolBar(self):

        pass

    def createTreeCtrl(self):
        self.kind_tree = wx.TreeCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TR_DEFAULT_STYLE)

        pass

    def createConDB(self, bSizer2):
        self.m_staticText1 = wx.StaticText(self, wx.ID_ANY, u"host", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        host_comboChoices = [u"172.26.185.139", u"192.168.8.18"]
        self.host_combo = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      host_comboChoices, 0)
        bSizer2.Add(self.host_combo, 0, wx.ALL, 5)

        self.vendor_combo = wx.StaticText(self, wx.ID_ANY, u"vendor", wx.DefaultPosition, wx.DefaultSize, 0)
        self.vendor_combo.Wrap(-1)
        bSizer2.Add(self.vendor_combo, 0, wx.ALL, 5)

        vendor_comboChoices = []
        self.vendor_combo = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                        vendor_comboChoices, 0)
        bSizer2.Add(self.vendor_combo, 0, wx.ALL, 5)

        self.area = wx.StaticText(self, wx.ID_ANY, u"area", wx.DefaultPosition, wx.DefaultSize, 0)
        self.area.Wrap(-1)
        bSizer2.Add(self.area, 0, wx.ALL, 5)

        area_comboChoices = []
        self.area_combo = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                      area_comboChoices, 0)
        bSizer2.Add(self.area_combo, 0, wx.ALL, 5)

        self.m_staticText3 = wx.StaticText(self, wx.ID_ANY, u"db_name", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer2.Add(self.m_staticText3, 0, wx.ALL, 5)

        db_comboChoices = []
        self.db_combo = wx.ComboBox(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                    db_comboChoices, 0)
        bSizer2.Add(self.db_combo, 3, wx.ALL, 5)

        self.connect_btn = wx.Button(self, wx.ID_ANY, u"connect", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.connect_btn, 0, wx.ALL, 5)
        pass

    def __del__(self):
        pass

    def backup_action(self, event):
        import shutil
        import time
        sql_txt_path = Global_param.tree_path
        backup_name = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
        backup_path = r'd:\TEST\sql_collect\sql_file\backup' + '\\' + backup_name + '.txt'
        shutil.copy(sql_txt_path, backup_path)
        event.Skip()

    def GetHostSel(self, event):
        # fill the vendor through vendor_area
        vendor_list = Global_param.vendor_area.keys()
        for vendor in vendor_list:
            self.vendor_combo.Append(vendor)

        event.Skip()

    def get_enter_host_action(self, event):
        event.Skip()

    def GetVendorSel(self, event):
        # fill the area through vendor_area
        vendor = self.vendor_combo.GetStringSelection()

        area_list = Global_param.vendor_area[vendor]
        for area in area_list:
            self.area_combo.Append(area)
        event.Skip()

    def get_enter_vendor_action(self, event):
        event.Skip()

    def GetAreaSel(self, event):
        # get all db name list
        # get host
        host = self.host_combo.GetStringSelection()
        if host == '':
            host = self.host_combo.GetString(1)

        # get all db name
        self.db.connect(host)
        db_name_list = self.db.get_db_name()

        # get db name list which with vendor name
        vendor = self.vendor_combo.GetStringSelection()
        area = self.area_combo.GetStringSelection()
        for db_name in db_name_list:
            if db_name[0].lower().find(vendor) != -1 and db_name[0].lower().find(area) != -1:
                self.db_combo.Append(db_name[0])
        event.Skip()

    def refresh_tree_list(self, root):
        # fill the tree list
        if self.kind_tree.GetCount() != 1:
            self.kind_tree.DeleteAllItems()
            self.treeroot = self.kind_tree.AddRoot(r'sql_list')
        self.AddItem(root, read_file.read_sql_txt(Global_param.tree_path))

    def GetDbSel(self, event):

        # connect db
        host = self.host_combo.GetStringSelection()
        db = self.db_combo.GetStringSelection()
        self.db.close()
        if host and db:
            self.db.connect( host, db)
        else:
            wx.MessageBox(' u must choose host first')
        event.Skip()

    def get_enter_db_action(self, event):
        event.Skip()

    def connect_db_action(self, event):
        event.Skip()

    def delete_item(self, event):
        # right click item , delete the item from tree and sql_list
        item = event.GetItem()
        if item:
            dlg = wx.MessageDialog(None, " this will delete this sql ",
                                   "MessageDialog", wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:

                # self.DeleteSelectedTreeItem(item, self.tree_list)
                self.DeleteSelectedTreeItem( self.list_heritage, self.tree_list )
                read_file.write_sql_txt(Global_param.tree_path, str(self.tree_list))
                # self.refresh_tree_list(self.treeroot)
                # self.tree_list = read_file.read_sql_txt(Global_param.tree_path)
                self.kind_tree.Delete(item)
        event.Skip()

    def GetLevel1Name(self, event):
        # make the level2 combo list
        level1_name = self.level_1_combo.GetStringSelection()
        level2_list = self.GetDictLevel2(self.tree_list, level1_name)
        self.level_2_combo.Clear()
        for level2 in level2_list:
            self.level_2_combo.Append(level2)

    def GetLevel2Name(self, event):
        # make the level3 combo list
        level1_name = self.level_1_combo.GetStringSelection()
        level2_name = self.level_2_combo.GetStringSelection()
        if level2_name:
            level3_list = self.GetDictLevel3(self.tree_list, level1_name, level2_name)
            for level3 in level3_list:
                self.level_3_combo.Append(level3)
        else:
            self.level_3_combo.Append('')

    def GetLevel3Name(self, event):
        event.Skip()

    def get_selected_item(self, event):
        # show sql in the code_text
        tree_item_id = event.GetItem()
        self.list_heritage = self.GetItemText(tree_item_id)

        sql = self.GetTreeItemValue(self.list_heritage)
        if sql:
            self.code_text.SetValue( sql )

    def run_code_action(self, event):
        # run sql code
        kc = event.GetKeyCode()

        if kc == 344:  # F5
            select_sql = self.code_text.GetStringSelection()
            all_sql = self.code_text.GetValue()
            if select_sql :
                sql = select_sql
            elif all_sql:
                sql = all_sql
            else:
                wx.MessageBox('have something wrong in the sql')
                return ''
            self.SetTitle('collect sql')
            if self.db.isconnected():
                result = self.db.fetchall(sql)
                col_value = self.db.get_column_name()
                print col_value
                if isinstance(result, list):
                    # show the result to Grid
                    rowLabels = range(0, result.__len__())
                    colLabels = col_value
                    tableBase = GenericTable.GenericTable(result, rowLabels,
                                                          colLabels)
                    self.result_grid.SetTable(tableBase)
                    self.result_grid.ForceRefresh()
                else:
                    wx.MessageBox( result )
            else:
                wx.MessageBox("do not connected to db")
        if kc == 345 : # F6 update the SQL string
            select_sql = self.code_text.GetStringSelection()
            all_sql = self.code_text.GetValue()
            if select_sql:
                sql = select_sql
            elif all_sql:
                sql = all_sql
            else:
                wx.MessageBox('have something wrong in the sql')
                return ''
            self.UpdateSelectedTreeItem(self.list_heritage, self.tree_list, sql)

        event.Skip()

    def add_code_action(self, event):
        # tree_list: level1, level2, level3 + name = Sql
        # if sql is null then not insert
        level1 = self.level_1_combo.GetStringSelection()
        level2 = self.level_2_combo.GetStringSelection()
        level3 = self.level_3_combo.GetStringSelection()

        sql_name = self.sql_name_text.GetValue()
        sql = self.add_code_text.GetValue()

        add_flag = False
        if sql:
            if sql_name:
                if level3 or level3 == '':
                    self.tree_list[level1][level2][sql_name] = sql
                    add_flag = True
                elif level2:
                    self.tree_list[level1][sql_name] = sql
                    add_flag = True
                elif level1:
                    self.tree_list[level1][sql_name] = sql
                    add_flag = True
                else:
                    wx.MessageBox(" u must choose one category ")
            else:
                wx.MessageBox(" input this sql name first ")
        else:
            wx.MessageBox("input sql string first ")

        if add_flag and self.tree_list:
            read_file.write_sql_txt( Global_param.tree_path, str(self.tree_list))
            self.refresh_tree_list(self.treeroot)
            self.tree_list = read_file.read_sql_txt(Global_param.tree_path)

        event.Skip()

    def AddItem(self, root, sql_list):
        # add items to tree
        for (key,value) in sql_list.items():
            if isinstance(value, __builtins__.dict) :
                child = self.kind_tree.AppendItem(root, key)
                self.AddItem(child, value)
            # 如果是目录的话
            else:
                child = self.kind_tree.AppendItem(root, key)

    # 获取treectrl  item text
    def GetItemText(self, item):
        if item and item != self.kind_tree.GetRootItem() :
            str = []
            str.append( self.kind_tree.GetItemText(item) )

            while self.kind_tree.GetItemParent(item) != self.kind_tree.GetRootItem():
                item = self.kind_tree.GetItemParent(item)
                str.append(self.kind_tree.GetItemText(item))

            return str
            # return self.GetTreeItemValue( str )
        else:
            ''

    def DeleteSelectedTreeItem(self, str, tree_list ):
        if str:
            j = 0
            for i in range(0, str.__len__())[::-1]:
                if j == 0:
                    old_value = tree_list[str[i]]
                    old_str = str[i]
                elif isinstance(old_value, __builtins__.dict):
                    new_value = old_value[str[i]]
                    new_str = str[i]

                    if not isinstance(new_value, __builtins__.dict):

                        del old_value[new_str]
                        return ''
                    old_str = new_str
                    old_value = new_value
                else:
                    pass
                j += 1
        else:
            return ''

    def UpdateSelectedTreeItem(self, str_list, tree_list, new_sql):
        if str_list and new_sql:
            j = 0
            for i in range(0, str_list.__len__())[::-1]:
                if j == 0:
                    old_value = tree_list[str_list[i]]
                    # old_str = str_list[i]
                elif isinstance(old_value, __builtins__.dict):
                    new_value = old_value[str_list[i]]
                    new_str = str_list[i]
                    if not isinstance(new_value, __builtins__.dict):
                        old_value[new_str] = new_sql
                        read_file.write_sql_txt(Global_param.tree_path, str(self.tree_list))
                        return ''
                    # old_str = new_str
                    old_value = new_value
                else:
                    pass
                j += 1
        else:
            return ''

    # from tree item desc list ,get the value from sql_dict
    def GetTreeItemValue(self, tree_name_list ):
        if tree_name_list:
            j = 0
            for i in range(0, tree_name_list.__len__())[::-1]:
                if j == 0:
                    value = self.tree_list[tree_name_list[i]]
                elif isinstance(value, __builtins__.dict) :
                    value = value[tree_name_list[i]]
                    if not isinstance(value, __builtins__.dict):
                        return value
                else:
                    pass
                j += 1
        else:
            return ''

    # get the first level key name of the dict, return list
    def GetDictLevel1(self, sql_list):
        if sql_list :
            return sql_list.keys()
        else:
            return []

    # the level2 name of the dict return list
    def GetDictLevel2(self, sql_list, level1_name):
        if sql_list:
            if isinstance(sql_list[level1_name], __builtins__.dict):
                return sql_list[level1_name].keys()
            else:
                return []
        else:
            return []

    # get the third level key name of the dict , return list
    def GetDictLevel3(self, sql_list, level1_name, level2_name):
        if sql_list:
            if isinstance(sql_list[level1_name],__builtins__.dict) and \
                    isinstance(sql_list[level1_name][level2_name],__builtins__.dict):
                return sql_list[level1_name][level2_name].keys()
            else:
                return []
        else:
            return []


    # get the forth level key name of the dict , return list
    def GetDictLevel4(self, sql_list, level1_name, level2_name, level3_name ):
        if sql_list:
            if isinstance(sql_list[level1_name], __builtins__.dict) and \
                    isinstance(sql_list[level1_name][level2_name], __builtins__.dict) and \
                    isinstance(sql_list[level1_name][level2_name][level3_name], __builtins__.dict) :
                return sql_list[level1_name][level2_name][level3_name].keys()
            else:
                return []
        else:
            return []


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame1()
    frame.Show(True)
    app.MainLoop()


# def __init__(self, parent=None, host_list=[], vendor_list=[], db_list=[], feature_list=[]):
#     host_comboChoices = host_list
#     vendor_comboChoices = vendor_list
#     db_comboChoices = db_list
#     vendor_list_comboChoices = vendor_list
#     feature_comboChoices = feature_list