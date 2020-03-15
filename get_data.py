# -*- coding: utf-8 -*-

import requests
import csv
import tkinter as tk
import tkinter.messagebox

def get_data():
    url = 'https://gitee.com/PNRetr0/PythonHW/raw/master/data_csv.CSV'
    data = requests.get(url)
    with open("data_csv.csv","wb") as data_file:
        data_file.write(data.content)
    tk.messagebox.showinfo(title='All done!', message='数据获取完成，请进行可视化和数据分析。')