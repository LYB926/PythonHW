# -*- coding: utf-8 -*-

import csv
from matplotlib import pyplot as plt

def draw():
    date = []
    diagnosed = []
    for i in range(1,30):
        date.append(i)
    with open ("data_csv.csv") as csvfile:
        plots = csv.reader(csvfile,delimiter = ",")
        for row in plots:
            diagnosed.append(int(row[0]))
    plt.plot(date,diagnosed,"m")
    plt.axis([0,30,0,15000])
    plt.xlabel("Date")
    plt.ylabel("diagnosed")
    plt.title("Demo")
    plt.show()
    
