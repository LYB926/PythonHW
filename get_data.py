# -*- coding: utf-8 -*-

import requests
import csv
import os
import tkinter as tk
import tkinter.messagebox

def get_data():
    url = 'https://gitee.com/PNRetr0/PythonHW/raw/master/data_csv.CSV'
    try:
        data = requests.get(url)
        with open("data_csv.csv","wb") as data_file:
            data_file.write(data.content)
        tk.messagebox.showinfo(title='All done!', message='数据获取完成，请进行可视化和数据分析。')
    except Exception:
        tk.messagebox.showerror(title='Error!', message='计算机似乎未连接到Internet。将运行ping指令。')
        os.system(u"ping 114.114.114.114")