# -*- coding: utf-8 -*-

import tkinter as tk
from get_data import get_data
from draw import draw
from output import output

win=tk.Tk()
win.title("StatTrak丨数聚")
win.geometry('300x350')

l1 = tk.Label(win, text="2月1日-29日全国新冠疫情", fg='black', font=('Arial', 12), width=50, height=1)
l1.pack()
l2 = tk.Label(win, text="每日新增确诊人数数据可视化", fg='black', font=('Arial', 12), width=50, height=1)
l2.pack()
l3 = tk.Label(win, text="请先获取数据，再进行数据可视化和数据分析。", fg='black', font=('Arial', 8), width=50, height=1)
l3.pack()

button = tk.Button(win,text="从Internet获取数据",height = 4,width = 20,command=get_data)
button.pack()

button = tk.Button(win,text="绘制折线图",height = 4,width = 20,command=draw)
button.pack()

button = tk.Button(win,text="显示数据分析结果",height = 4,width = 20,command=output)
button.pack()

l3 = tk.Label(win, text="Code by 张可 丨 2020/3/15", fg='black', font=('Arial', 8), width=50, height=2)
l3.pack()
win.mainloop()
