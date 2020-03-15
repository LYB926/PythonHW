# -*- coding: utf-8 -*-
import numpy as np
import csv
import tkinter as tk
import tkinter.messagebox

def output():
    diagnosed = []
    with open ("data_csv.csv") as csvfile:
        plots = csv.reader(csvfile,delimiter = ",")
        for row in plots:
            diagnosed.append(int(row[0]))
    #寻找最大值和对应日期
    maxNum = max(diagnosed)
    max_date = diagnosed.index(maxNum) + 1
    #寻找最小值和对应日期
    minNum = min(diagnosed)
    min_date = diagnosed.index(minNum) + 1
    #计算平均值和中位值
    ava = np.mean(diagnosed)
    median = np.median(diagnosed)
    #组装字符串
    output_str = "新增确诊人数最大值：" + str(maxNum) + "\n新增确诊人数最大日期：二月" + str(max_date) \
        + "日\n新增确诊人数最小值：" + str(minNum) + "\n新增确诊人数最小日期：二月" + str(min_date) + "日\n" \
        +  "新增确诊人数平均值：" + str(ava) + "\n新增确诊人数中位数：" + str(median)
    #使用TK输出
    tk.messagebox.showinfo(title='数据分析结果', message=output_str)