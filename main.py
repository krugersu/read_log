import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from fabric.connection import Connection
import os
import paramiko
from ttkbootstrap.constants import *


    # test
    
    
class LogEntryForm(ttk.Frame):
    
    def __init__(self, master):
            super().__init__(master)
          
            #self.pack(fill=BOTH, expand=YES)
            # self.create_widget_elements()

            colors = app.style.colors
            coldata = [
                {"text": "Дата", "stretch": False, 'width':150, 'minwidth':30},
                {"text": "Уровень", "stretch": False, 'width':80, 'minwidth':30},
            {"text": "Модуль", "stretch": False,'width':250, 'minwidth':30},
            {"text": "Функция-строка", "stretch":  False,'width':250, 'minwidth':30},
            {"text": "Сообщение", "stretch": True},
            ]
            rowdata = []
        
    
            self.dt = Tableview(
    
                coldata=coldata,
                rowdata=rowdata,
                paginated=False,
                searchable=True,
                bootstyle=PRIMARY,
                autofit=False,
                autoalign=True,
                stripecolor=(colors.light, None),    
            )

            # b1 = ttk.Button(app, text="Обновить",command= self.refresh_data(dt), bootstyle=SUCCESS)
            # b1.pack(side=LEFT, padx=5, pady=10)
            hdr_frame = ttk.Frame(self, padding=5, bootstyle=DEFAULT)
            hdr_frame.grid(row=1, column=0, columnspan=3, sticky=EW)

            browse_btn = ttk.Button(hdr_frame, text="Кассовые смены",command=self.get_file, bootstyle=SUCCESS,width=15, )
            browse_btn.pack(side=TOP,  padx=5, pady=10)
            browse_btn_test = ttk.Button(hdr_frame, text="Тест Http",command=self.get_file_test, bootstyle=SUCCESS,width=15, )
            browse_btn_test.pack(side=TOP,  padx=5, pady=10)
            self.dt.pack(fill=BOTH,side=RIGHT,expand=YES,  padx=5, pady=10)
            self.pack(fill=BOTH, expand=YES)
            self.create_widget_elements()

    def create_widget_elements(self):
        """Create and add the widget elements"""
        
            

    def refresh_data(self):
        
            self.dt.delete_rows()
            filename = 'ws_log.log'
            with open(filename) as file:
                while (line := file.readline().rstrip()):
                    n_str = line.split('|')
                    self.dt.insert_row('end', [n_str[0], n_str[1], n_str[2],n_str[3],n_str[4]])        
                    self.dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)
            self.dt.load_table_data()
#    # 
#     #get_file()
    
    def get_file(self):
        host = '192.168.0.87'
        user = 'administrator'
        localpath = os.path.abspath(os.curdir) +  '/ws_log.log'
        remotepath = '/home/administrator/Workshift_load/log/ws_log.log'
        ssh = paramiko.SSHClient()
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        ssh.connect(host, username=user, password='200488')
        sftp = ssh.open_sftp()
        sftp.get(remotepath,localpath )
        sftp.close()
        ssh.close()
        self.refresh_data()

    def get_file_test(self):
        host = '192.168.0.87'
        user = 'administrator'
        localpath = os.path.abspath(os.curdir) +  '/ws_log.log'
        remotepath = '/home/administrator/log/py_log.log'
        ssh = paramiko.SSHClient()
        ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
        ssh.connect(host, username=user, password='200488')
        sftp = ssh.open_sftp()
        sftp.get(remotepath,localpath )
        sftp.close()
        ssh.close()
        self.refresh_data()


if __name__ == "__main__":
    
    app = ttk.Window("Анализ лог-файла", "lumen", resizable=(False, False),size=(1800, 550))
    LogEntryForm(app)
    app.mainloop()
