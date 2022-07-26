import numpy as np 
import seaborn as sn 
import pandas as pd 
import matplotlib.pyplot as plt 
from mpl_toolkits.axes_grid1.axes_divider import make_axes_locatable
from matplotlib.colors import LinearSegmentedColormap

df = pd.read_csv("out_hydro_Hbond.csv" )
df_a = pd.read_csv("out_acceptor.csv" )
df1= df.set_index('Title')
df_a1= df_a.set_index('Title')

#df1= df1.iloc[:,0:10080]

ax= plt.figure(figsize=(15,6))


#


colors = ['white','navy','maroon'] 
cmap = LinearSegmentedColormap.from_list('', colors)




font1 = {'family':'Times New Roman','color':'black','size':20}
font2 = {'family':'Times New Roman','color':'darkred','size':14}


sn.set(font="Times New Roman", font_scale=1.8)


ax1 = sn.heatmap( df1, linewidth = 0.01, linecolor = 'aliceblue', annot = False, cbar = False, cmap=cmap)

#for _, spine in ax1.spines.items():
 #   spine.set_visible(True)
ax1.axhline(y = 0, color='k',linewidth = 1)
ax1.axhline(y = 8, color = 'k',
            linewidth = 2)
            
ax1.axvline(x = 0, color = 'k',
            linewidth = 1)
  
ax1.axvline(x = 19, 
            color = 'k', linewidth = 2)
  

ax1.set_ylabel('SARS-CoV-2 Variants',  fontdict = font1)
ax1.set_xlabel('Interacting Residues', fontdict = font1)

plt.show()
