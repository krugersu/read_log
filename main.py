import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip
from fabric.connection import Connection
import os
import paramiko
from ttkbootstrap.constants import *


    
    
    
class LogEntryForm(ttk.Frame):
    
    def __init__(self, master):
            super().__init__(master)
          
            #self.pack(fill=BOTH, expand=YES)
            # self.create_widget_elements()

            colors = app.style.colors
            coldata = [
                {"text": "Дата", "stretch": True},
                "Уровень",
            {"text": "Модуль", "stretch": True},
            {"text": "Функция", "stretch": True},
            {"text": "Сообщение", "stretch": True},
            ]
            rowdata = []
        
    
            self.dt = Tableview(
    
                coldata=coldata,
                rowdata=rowdata,
                paginated=False,
                searchable=True,
                bootstyle=PRIMARY,
                autofit=True,
                autoalign=True,
                stripecolor=(colors.light, None),    
            )

            # b1 = ttk.Button(app, text="Обновить",command= self.refresh_data(dt), bootstyle=SUCCESS)
            # b1.pack(side=LEFT, padx=5, pady=10)
            browse_btn = ttk.Button(self, text="Обновить",command=self.get_file, bootstyle=SUCCESS )
            browse_btn.pack(side=LEFT,  padx=5, pady=10)
            self.dt.pack(side=RIGHT, padx=5, pady=10)
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

if __name__ == "__main__":
    
    app = ttk.Window("Data Entry", "lumen", resizable=(True, True))
    LogEntryForm(app)
    app.mainloop()