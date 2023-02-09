# def main():
    
    
    
# # default tooltip
# #ToolTip(dt, text="Содержимое лог файла")

#     get_file()
#     filename = 'ws_log.log'
#     with open(filename) as file:
#         while (line := file.readline().rstrip()):
#             n_str = line.split('|')
#             dt.insert_row('end', [n_str[0], n_str[1], n_str[2],n_str[3],n_str[4]])        

#     dt.load_table_data()
#     #dt.delete_rows()
#     dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

# def refresh_data():
#     pass
#   #  print('11')
#    # dt.delete_rows()
#     #get_file()
    

# def get_file():
#     host = '192.168.0.87'
#     user = 'administrator'
#     localpath = os.path.abspath(os.curdir) +  '/ws_log.log'
#     remotepath = '/home/administrator/Workshift_load/log/ws_log.log'
#     ssh = paramiko.SSHClient()
#     ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
#     ssh.connect(host, username=user, password='200488')
#     sftp = ssh.open_sftp()
#     sftp.get(remotepath,localpath )
#     sftp.close()
#     ssh.close()
    
    
    

# if __name__ == '__main__':
    
#     app = ttk.Window(title='Анализ лог файлов', themename="lumen")

#     colors = app.style.colors
#     coldata = [
#         {"text": "Дата", "stretch": False},
#         "Уровень",
#         {"text": "Модуль", "stretch": False},
#         {"text": "Функция", "stretch": False},
#         {"text": "Сообщение", "stretch": True},
#     ]
#     rowdata = [ ]
    
#     dt = Tableview(
#             master=app,
#             coldata=coldata,
#             rowdata=rowdata,
#             paginated=False,
#             searchable=True,
#             bootstyle=PRIMARY,
#             stripecolor=(colors.light, None),
#         )
    
#     b1 = ttk.Button(app, text="Обновить",command= refresh_data(), bootstyle=SUCCESS)
#     b1.pack(side=LEFT, padx=5, pady=10)
#     main()
#     app.mainloop()
