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
## Class MyFrame33
###########################################################################

from Frame import subMainFrame

class MyFrame ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = "SQL collect", pos = wx.DefaultPosition, size = wx.Size( 900,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        self.m_toolBar2 = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY )
        self.show_add = wx.Button(self.m_toolBar2, wx.ID_ANY, u"showAddSQL", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_toolBar2.AddControl(self.show_add)
        self.m_toolBar2.Realize()

        bSizer126 = wx.BoxSizer( wx.VERTICAL )

        # sub main frame
        self.subMainPanel = subMainFrame.subMain(self)
        bSizer126.Add( self.subMainPanel, 1, wx.EXPAND |wx.ALL, 5 )

        self.SetSizer( bSizer126 )
        self.Layout()
        
        self.Centre( wx.BOTH )

        # Connect Events
        self.show_add.Bind(wx.EVT_BUTTON, self.show_addSQL)

        self.isShown = True
    
    def __del__( self ):
        pass

    # Virtual event handlers, overide them in your derived class
    def show_addSQL(self, event):
        # self.isShown = self.subMainPanel.AddSQL.IsShown
        if self.isShown:  # 如果当前控件已显示
            print 'is show'
            self.subMainPanel.sqlSizer.Hide(self.subMainPanel.AddSQL)  # 隐藏服务器设置部分
            self.isShown = False  # 服务器设置部分当前已隐藏
            self.SetClientSize((900, 500))  # 更新面板尺寸
        else:
            print 'is hidden'
            self.subMainPanel.sqlSizer.Show(self.subMainPanel.AddSQL)  # 如果当前控件已隐藏
            self.isShown = True  # 服务器设置部分当前已显示
            self.SetClientSize((900, 500))  # 更新面板尺寸
        self.subMainPanel.Layout()  # 关键所在，强制sizer重新计算并布局sizer中的控件


# app = wx.App(False)
# frame = MyFrame(None)
# frame.Show(True)
# app.MainLoop() #循环监听事件
#
if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = MyFrame(None)
    frame.Show(True)
    app.MainLoop()