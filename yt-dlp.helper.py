''' yt-dlp gui helper '''
# youtube download helper for yt-dlp v0.1
# must work with yt-dlp
# download from [https://github.com/yt-dlp/]

import os
import sys
import subprocess

import wx
import uimodule


class PyytdlpGUIHelper(uimodule.HelperFrame):
    ''' yt-dlp helper init class '''
    def __init__(self, parent):
        super().__init__(parent)
        
        self.b_ready = False
        self.view_id = "0"
        self.url_view = "https://www.youtube.com/"
        self.shorts_postfix = "/shorts/"
        self.watch_postfix = "/watch?v="
        
        # self.m_textCtrl.OnText.connect(self.evt_input_text_chaned)
        # self.button_exit.clicked.connect(self.evt_button_exit_clicked)
        # self.m_button_download.clicked.connect(self.evt_button_download_clicked)

        # event binds
        # self.m_textCtrl.Bind(wx.EVT_SET_FOCUS, self.on_m_textCtrl_focus_on)
        # self.m_textCtrl.Bind(wx.EVT_KILL_FOCUS, self.on_m_textCtrl_focus_off)
        
        self.init_app()

    def init_app(self):
        ''' ready for app '''

        self.b_ready = self.check_ready()
        # self.m_textCtrl.setEnabled(self.b_ready)
        # self.m_textCtrl.setText("")
        self.m_textCtrl.text = ""
        self.executable_path = os.getcwd()

        if self.b_ready is True:
            self.set_status("Ready app")
            self.m_textCtrl.SetEditable(True)
        else:
            self.set_status("'yt-dlp.exe' is need to run")
            self.m_textCtrl.SetEditable(False)

    def on_m_textCtrl_focus_on(self, evt):
        print("on_m_textCtrl_focus_on :EVT_SET_FOCUS:", evt)

    def on_m_textCtrl_focus_off(self, evt):
        print("on_m_textCtrl_focus_off :EVT_KILL_FOCUS:", evt)
        # self.m_textCtrl
            
    def check_ready(self)->bool:
        ''' check for excutable '''
        path = os.path.abspath(__file__)
        path = os.path.dirname(path)
        
        if os.listdir(path).count("yt-dlp.exe") > 0:
            return True
        elif os.listdir(os.curdir).count("yt-dlp.exe") > 0:
            return True
        else:
            return False
           
    def set_status(self, txt:str):
        ''' set label '''
        # self.m_statusBar.setText(txt)
        self.m_statusBar.SetStatusText(txt)

    def evt_input_text_chaned(self, e_change):
        ''' text input check for validation '''
        # self.m_statusBar.setStatusText(e_change)
        url = self.m_textCtrl.GetLineText(0)

        self.view_id = self.get_view_id(url)
        self.is_valid = self.is_valid_url(url)
        self.is_valid = self.is_valid & (self.view_id is not None)
        
        if self.is_valid is False:
            self.set_status("Not valid URL : " + url)
        self.m_button_download.Enabled = self.is_valid
    
    def get_view_id(self, url:str)->str:
        ''' retruns youtube video id '''
        # TODO: remove app=desktop / make downloadable playlist
        str_idx = url.find(self.watch_postfix)
        if str_idx > 0:
            str_idx += len(self.watch_postfix)
            return url[str_idx:str_idx+11]

        str_idx = url.find(self.shorts_postfix)
        if str_idx > 0:
            str_idx += len(self.shorts_postfix)
            return url[str_idx:str_idx+11]
        
        return None
    
    def is_valid_url(self, url:str)->bool:
        ''' check url address for download youtube '''
        if "www.youtube.com" not in url :
            return False
        self.set_status("Ready : " + self.view_id)
        return True
    
    def evt_button_download_clicked(self, e_click):
        ''' start download '''
        self.set_status("Start Downloading... " + self.view_id)
        self.req_download()

    def req_download(self):
        ''' send commands to cmd for running yt-dlp '''
        self.m_button_download.Enabled = False
        command = self.executable_path + "//yt-dlp.exe https://www.youtube.com/watch?v=" + self.view_id
        
        # stream = os.popen(command)
        # output = stream.read()
        # self.download_complete(output)
        
        result = subprocess.getstatusoutput(command)
        self.download_complete(str(result))
    
    def download_complete(self, result):
        idx = result.find("[download] 100% of")
        if idx > 0:
            self.set_status("Download Complete... Ready")
            self.init_app()
        else:
            self.set_status("Sorry. something went wrong...")
            print(result)
    
    def evt_button_exit_clicked(self, e_click):
        ''' close app '''
        self.label_process.text = "exit!"
        self.closeEvent(None)
    
if __name__ == '__main__':
    app = wx.App(False)
    frame = PyytdlpGUIHelper(None)
    frame.Show(True)
    app.MainLoop()
    
    # sys.exit(app.exec_())
    sys.exit(app.OnExit())
#EOF