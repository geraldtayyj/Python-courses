# Use the following data for this assignment:
# %matplotlib notebook
import pandas as pd
import numpy as np
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(12345)
df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df["average"] = df.mean(axis=1)

y = df.mean(axis=1)
mean = y.tolist()
yerrs = df.std(axis=1)/(3650**0.5)
yerrs_list = yerrs.tolist()

#work on bar chart first
fig = plt.figure(figsize = (6, 5))
##colour gradient
p = (0,0.09, 0.18, 0.27, 0.36, 0.45, 0.55, 0.64, 0.73, 0.82, 0.91, 1.00)
plot = plt.scatter(p, p, c = p, cmap = 'RdBu_r')
plt.clf()
plt.colorbar(plot)
bars = plt.bar(df.index, y,yerr = yerrs, capsize = 10)
y_set=40000
##labels for y_set adjuster
plt.subplots_adjust(left=0.25)
plt.axhline(y=y_set, ls = "--", label = y_set)
plt.text(x=1990, y = y_set, s = str(int(y_set)))
### adjusting colour of bar charts
for i in range(len(df.index)):
    if (1-((y_set-mean[i] + yerrs_list[i]) / (2*yerrs_list[i]))) > 1:
        colour = cm.RdBu_r(1.0)
    elif (1-((y_set-mean[i] + yerrs_list[i]) / (2*yerrs_list[i]))) < 0:
        colour = cm.RdBu_r(0.0)
    else:
        colour = cm.RdBu_r(1-((y_set-mean[i] + yerrs_list[i]) / (2*yerrs_list[i])))
    bars[i].set_color(colour)
    
def onclick(event):
    '''to update y_set value and colour of bar charts accordingly'''
    plt.cla()
    y_set = event.ydata
    bars = plt.bar(df.index, y,yerr = yerrs, capsize = 10)   
    plt.axhline(y=y_set)
    plt.text(x=1990, y = y_set, s = str(int(y_set)))
    for i in range(len(df.index)):
        if (1-((y_set-mean[i] + yerrs_list[i]) / (2*yerrs_list[i]))) > 1:
            colour = cm.RdBu_r(1.0)
        elif (1-((y_set-mean[i] + yerrs_list[i]) / (2*yerrs_list[i]))) < 0:
            colour = cm.RdBu_r(0.0)
        else:
            colour = cm.RdBu_r(1-((y_set-mean[i] + yerrs_list[i]) / (2*yerrs_list[i])))
        bars[i].set_color(colour)
    plt.show()
    
# tell mpl_connect we want to pass a 'button_press_event' into onclick when the event is detected
plt.gcf().canvas.mpl_connect('button_press_event', onclick)    