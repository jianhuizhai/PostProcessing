import sys
import numpy as np
import matplotlib.pylab as plt
#import mpl_toolkits.mplot3d as p3d

filename = sys.argv[1]
x, y, density = np.loadtxt(filename, skiprows=4, unpack=True)

plt.figure(figsize=(18.5,16.5))
ax = plt.subplot(1,1,1)

#plt.scatter(x,y,c=density, vmin=-0.03, vmax=0.03, cmap='coolwarm') # hot, cool, coolwarm, gnuplot, gnuplot2, bwr, Reds
scatters = plt.scatter(x,y,c=density, cmap='coolwarm') # hot, cool, coolwarm, gnuplot, gnuplot2, bwr, Reds
cb = plt.colorbar(scatters, pad=0.01)  # pad controls the distance between bar and picture
plt.clim(-0.03, 0.03)   # lim of colorbar
cb.set_label(label="Charge density (e/S)",size=45)
cb.ax.tick_params(labelsize=35,direction='in')
#--------------------------------------------------------------------
ax.tick_params(axis='x', pad=15)  # distance between axis and text
ax.tick_params(axis='y', pad=15)
#--------------------------------------------------------------------
ax.spines['left'].set_linewidth(3.0)
ax.spines['right'].set_linewidth(3.0)
ax.spines['top'].set_linewidth(3.0)
ax.spines['bottom'].set_linewidth(3.0)


#===================================================================================
plt.minorticks_on()
plt.tick_params(which='major',direction='in',width=3.0,length=12)  # 
plt.tick_params(which='minor',direction='in',width=3.0,length=5)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)

ax.tick_params(axis='x', pad=10)  # distance between axis and text
ax.tick_params(axis='y', pad=10)

#-----------------------------------------------------------------------------------
plt.xlabel('[110]'+r'($\mathrm{\AA}$)', fontsize='45')
plt.ylabel(r'$[1\bar{1}0](\mathrm{\AA})$', fontsize='45')

plt.xlim(0,)
plt.ylim(0,)

plt.savefig("density.pdf", bbox_inches="tight")
plt.show()