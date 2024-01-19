# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.0.0-0-g0efcecf)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class HelperFrame
###########################################################################

class HelperFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"YT-DLP.HELPER", pos = wx.DefaultPosition, size = wx.Size( 800,130 ), style = wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.MINIMIZE|wx.SYSTEM_MENU|wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 800,130 ), wx.Size( 800,130 ) )

		self.m_statusBar = self.CreateStatusBar( 1, wx.STB_SIZEGRIP|wx.BORDER_STATIC, wx.ID_ANY )
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_files = wx.Menu()
		self.menu_files_downloads = wx.MenuItem( self.m_menu_files, wx.ID_ANY, u"Show Downloads", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_files.Append( self.menu_files_downloads )

		self.m_menubar.Append( self.m_menu_files, u"Files" )

		self.m_menu_help = wx.Menu()
		self.menu_help_yt_dlp = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Get YT-DLP", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.menu_help_yt_dlp )

		self.menu_help_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"about...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.Append( self.menu_help_about )

		self.m_menubar.Append( self.m_menu_help, u"Help" )

		self.SetMenuBar( self.m_menubar )

		fgSizer = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer.AddGrowableCol( 0 )
		fgSizer.AddGrowableRow( 0 )
		fgSizer.SetFlexibleDirection( wx.BOTH )
		fgSizer.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		sbSizer = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"URL" ), wx.VERTICAL )

		self.m_textCtrl = wx.TextCtrl( sbSizer.GetStaticBox(), wx.ID_ANY, u"https://www.youtube.com/watch?v=", wx.DefaultPosition, wx.Size( 650,-1 ), wx.TE_LEFT|wx.TE_NO_VSCROLL )
		sbSizer.Add( self.m_textCtrl, 0, wx.ALL, 5 )


		fgSizer.Add( sbSizer, 1, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_LEFT|wx.FIXED_MINSIZE, 5 )


		fgSizer.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button_download = wx.Button( self, wx.ID_ANY, u"Download", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button_download.Enable( False )
		self.m_button_download.SetMinSize( wx.Size( 110,45 ) )

		fgSizer.Add( self.m_button_download, 0, wx.ALL|wx.EXPAND|wx.FIXED_MINSIZE, 5 )


		self.SetSizer( fgSizer )
		self.Layout()

		# Connect Events
		self.m_textCtrl.Bind( wx.EVT_TEXT, self.evt_input_text_chaned )
		self.m_button_download.Bind( wx.EVT_BUTTON, self.evt_button_download_clicked )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def evt_input_text_chaned( self, event ):
		event.Skip()

	def evt_button_download_clicked( self, event ):
		event.Skip()


