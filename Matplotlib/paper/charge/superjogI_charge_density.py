import os
import sys
import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
#import mpl_toolkits.mplot3d as p3d

filename = sys.argv[1]
x, y, density = np.loadtxt(filename, skiprows=4, unpack=True)

for position_file in os.listdir('.'):
    if position_file.startswith('DislocInfo_'):
        dipole = np.loadtxt(position_file, usecols=(4,5,7),skiprows=9)
#====================================================================================
alat = float(input("Lattice parameter : "))
bmag = alat/np.sqrt(2)


plt.figure(figsize=(15,12))
ax = plt.subplot(1,1,1)

levels = [-1.5, -1, -0.5, 0, 0.5, 1]
#plt.scatter(x,y,c=density, vmin=-0.03, vmax=0.03, cmap='coolwarm') # hot, cool, coolwarm, gnuplot, gnuplot2, bwr, Reds
scatters = plt.scatter(x/bmag,       y/alat,c=density*8.5, vmin=-0.015, vmax=0.015, cmap='coolwarm') # hot, cool, coolwarm, gnuplot, gnuplot2, bwr, Reds
scatters = plt.scatter(x/bmag,(y+82.5)/alat,c=density*8.5, vmin=-0.015, vmax=0.015, cmap='coolwarm') # hot, cool, coolwarm, gnuplot, gnuplot2, bwr, Reds

cb = plt.colorbar(scatters, pad=0.01)  # pad controls the distance between bar and picture

cb.set_label(label="Charge density (e/S)",size=45)
cb.ax.tick_params(labelsize=35,direction='in')
'''
cb.set_ticks(np.linspace(-0.015,0.015,7,endpoint=True))
#cbarlevels = ('-0.02', '-0.01', '-0.05', '0', '0.05', '0.01', '0.02')
cbarlevels = ('-0.015','-0.01', '-0.005', '0', '0.005', '0.01', '0.015')
cb.set_ticklabels(cbarlevels)
plt.clim(-0.015, 0.015)   # lim of colorbar
'''

# plot dislocation position with black line
plt.plot(dipole[::2,0]/bmag-0.7, dipole[::2,1]/alat,linewidth='5.0', color='black') 
plt.plot(dipole[1::2,0]/bmag+0.45, dipole[1::2,1]/alat, linewidth='5.0',color='black')

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
#plt.xlabel('[110]'+r'($\mathrm{\AA}$)', fontsize='45')
#plt.ylabel(r'$[1\bar{1}0](\mathrm{\AA})$', fontsize='45')
plt.xlabel(r'$[1\overline{1}0]/b$', fontsize='45')
plt.ylabel(r'$[001]/a$', fontsize='45')

plt.xlim(0,101)
plt.ylim(0,20)
ymajorLocator   = MultipleLocator(5)
ax.yaxis.set_major_locator(ymajorLocator)

plt.savefig("superjogI_chargeDensity.pdf", bbox_inches="tight")
plt.show()