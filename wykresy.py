from cProfile import label
import pandas
import matplotlib.pyplot as pyplot
from os import walk
from os import getcwd
import numpy as np

#mypath = getcwd()
mypath = r"N:\Studia\Studia\Semestr 9 FT\mud\Projekt\p2"

filenames = next(walk(mypath), (None, None, []))[2]  # [] if no file


for filen in filenames:
    if filen[-3:] == 'txt':
        data = pandas.read_csv(mypath+ "\\" + filen, names=['t', 'x','y'], delim_whitespace=True)
        pyplot.plot(data['t'], data['y'], label=filen[:-4])
        #pyplot.plot(data['t'], data['y'], label=filen[:-4])
        #pyplot.plot(data['x'], data['y'], label=filen[:-4], c='r')
        # pyplot.plot(data['y'],label=filen[:-4])

        # pyplot.plot(data['x'], data['y'],label=filen[:-4])
        # pyplot.legend()
        # pyplot.savefig("faz1"+filen[:-4])
        # pyplot.cla()
        # pyplot.close()

        # pyplot.plot(data['x'],label=filen[:-4])
#pyplot.legend()
#pyplot.ylim(-4, 2)
pyplot.savefig("testyY")

pyplot.cla()
pyplot.close()
