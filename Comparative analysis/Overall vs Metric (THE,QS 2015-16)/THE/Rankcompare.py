import matplotlib as mpl 
import matplotlib.pyplot as plt
import csv 
import numpy as np
from pylab import *
from matplotlib.font_manager import FontProperties

x=[]
y=[]
n=[]
i=0


with open ('Teaching.csv','rt') as csvfile:
	plots= csv.reader(csvfile,delimiter=',')
	for row in plots:
			#print i,row
			#i=i+1
			
		#n.append(row[0])
		x.append(float(row[0]))
		y.append(float(row[1]))
			
fig, ax=plt.subplots()
ax.scatter(x,y, label='Ranking')
ax.set_xlim(xmin=0)
ax.set_ylim(ymax=120)
ax.set_ylim(ymin=0)
	
#m, b = np.polyfit(x, y, 1)

plt.plot(x, y, '.')
#l1=plt.plot(x, m*np.array(x) + b, '-')
plt.xlabel('Overall Score', fontsize=18)
plt.ylabel('Teaching Score', fontsize=18)
#setp(l1,linewidth=2)
plt.title ('THE 2015-16', fontsize=18)
plt.plot([0, 500], [0, 500], 'r', lw=2)
ax.spines['bottom'].set_linewidth(2.0)
ax.spines['left'].set_linewidth(2.0)
ax.spines['top'].set_linewidth(2.0)
ax.spines['right'].set_linewidth(2.0)
plt.show()

