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

###########################################################################
## Class MyPanel23
###########################################################################
from control import GenericTable
from control import read_file
from control import deligate


class execSQL ( wx.Panel ):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(512, 387),
                          style=wx.TAB_TRAVERSAL)

        topSizer = wx.BoxSizer(wx.VERTICAL)

        self.codePanel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        codePanel = wx.BoxSizer(wx.VERTICAL)

        self.code_text = wx.richtext.RichTextCtrl(self.codePanel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                  wx.DefaultSize,
                                                  0 | wx.VSCROLL | wx.HSCROLL | wx.NO_BORDER | wx.WANTS_CHARS)
        codePanel.Add(self.code_text, 1, wx.EXPAND | wx.ALL, 5)

        self.codePanel1.SetSizer(codePanel)
        self.codePanel1.Layout()
        codePanel.Fit(self.codePanel1)
        topSizer.Add(self.codePanel1, 1, wx.EXPAND | wx.ALL, 5)

        self.gridPanel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        gridSizer = wx.BoxSizer(wx.VERTICAL)

        self.result_grid = wx.grid.Grid(self.gridPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.result_grid.CreateGrid(5, 5)
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
        gridSizer.Add(self.result_grid, 0, wx.ALL, 5)

        self.gridPanel.SetSizer(gridSizer)
        self.gridPanel.Layout()
        gridSizer.Fit(self.gridPanel)
        topSizer.Add(self.gridPanel, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(topSizer)
        self.Layout()

        # Connect Events
        self.code_text.Bind(wx.EVT_KEY_DOWN, self.run_code_action)

        self.shareData = deligate.ShareData()
        self.read_file = read_file.getData()


    def __del__( self ):
        pass

    
    # Virtual event handlers, overide them in your derived class
    def run_code_action( self, event ):
        # run sql code
        kc = event.GetKeyCode()

        if kc == 344:  # F5
            self.db = self.shareData.getDB()
            select_sql = self.code_text.GetStringSelection()
            all_sql = self.code_text.GetValue()
            if select_sql:
                sql = select_sql
            elif all_sql:
                sql = all_sql
            else:
                wx.MessageBox('have something wrong in the sql')
                return ''

            if self.db:
                result = self.db.fetchall(sql)
                col_value = self.db.get_column_name()
                if isinstance(result, list):
                    # show the result to Grid
                    rowLabels = range(0, result.__len__())
                    colLabels = col_value
                    tableBase = GenericTable.GenericTable(result, rowLabels,
                                                          colLabels)
                    self.result_grid.SetTable(tableBase)
                    self.result_grid.ForceRefresh()
                else:
                    wx.MessageBox('have something wrong in the sql')
            else:
                wx.MessageBox("do not connected to db")
        if kc == 345:  # F6 update the SQL string
            all_sql = self.code_text.GetValue()
            if all_sql:
                sql = all_sql
            else:
                wx.MessageBox('have something wrong in the sql')
                return ''
            print sql
            self.read_file.updateSQL(sql, self.shareData.getL1(), self.shareData.getL2(),
                                     self.shareData.getL3(), self.shareData.getName())

        event.Skip()



