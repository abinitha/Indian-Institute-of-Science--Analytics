import matplotlib.pyplot as plt
import csv
import numpy as np
from matplotlib.font_manager import FontProperties

x=[]
y=[]

with open("IISc.csv",'rt') as csvfile:
	plots= csv.reader(csvfile,delimiter=',')
	for row in csvfile
	#print row
	x.append(row[1])
	y.append(row[2])
        print (x,y)

