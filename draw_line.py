# -*- coding: utf-8 -*-

import csv
from matplotlib import pyplot as plt
import tkinter as tk
import tkinter.messagebox

def draw_line():
    date = []
    diagnosed = []
    for i in range(1,30):
        date.append(i)
    try:
        with open ("data_csv.csv") as csvfile:
            plots = csv.reader(csvfile,delimiter = ",")
            for row in plots:
                diagnosed.append(int(row[0]))
        plt.plot(date,diagnosed,"m")
        plt.axis([0,30,0,15000])
        plt.xlabel("Date")
        plt.ylabel("New confirmed patients")
        plt.title("New daily diagnoses in China (February 1 to February 29)")
        plt.show()
    except FileNotFoundError:
        tk.messagebox.showerror(title='Error!', message='您还未获取数据，请先获取数据。')
    
