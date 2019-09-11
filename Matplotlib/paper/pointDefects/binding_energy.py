import numpy as np
import matplotlib.pylab as plt
from mpl_toolkits import mplot3d
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

'''
flag = input("Plot in 2D or 3D (1 or 2) : ")
'''
filename = 'energy_info.dat'

x, y, z, binding_energy = np.loadtxt(filename, usecols=(2,3,4,6), unpack=True)

# reference_eng should be given in here
# reference_eng = -12173104.0172041   ## for o
# reference_eng = -12173105.4983606   ## for mg

# dislocation core position
xc = 149.892
yc = 226.215

#====================================================================================================
#               plot the chosen ions type
#====================================================================================================
'''
if(flag == '1'):
    scatters = plt.scatter(x,y,c=energy-reference_eng, cmap='coolwarm')
    cb = plt.colorbar(scatters, pad=0.01)
elif( flag == '2' ):
    ax = plt.axes(projection='3d')
    scatters = ax.scatter3D(x, y, z, c=energy-reference_eng, cmap='coolwarm')
    plt.colorbar(scatters)
plt.xlabel('x([110])')
plt.ylabel(r'$y([1\bar{1}0])$')
'''
# (18.5,16.5)
plt.figure(figsize=(16.0,14.2))
ax = plt.subplot(1,1,1)

scatters = plt.scatter(x-xc,y-yc,c= binding_energy, s=300,cmap='coolwarm')

cb = plt.colorbar(scatters, pad=0.01)
cb.set_label(label="binding energy (eV)",size=45)
cb.ax.tick_params(labelsize=35,direction='in')

cb.set_ticks(np.linspace(-0.2,1.6,5,endpoint=True))
cbarlevels = ('-0.25', '0.25', '0.75', '1.25', '1.60')
cb.set_ticklabels(cbarlevels)

plt.clim(np.min((binding_energy))-0.1, np.max( binding_energy)  ) # lim of colorbar

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

'''
plt.xlim(-9,9)
plt.ylim(-10, 10)
'''
ymajorLocator   = MultipleLocator(2.5)
xmajorLocator   = MultipleLocator(3.0)
ax.yaxis.set_major_locator(ymajorLocator)
ax.xaxis.set_major_locator(xmajorLocator)

#plt.xlabel('x([110])')
#plt.ylabel(r'$y([1\bar{1}0])$')

plt.xlabel(r'vacancy position along [110] direction $(\mathrm{\AA})$',fontsize=35,labelpad=5)
plt.ylabel(r'vacancy position along $[1\bar{1}0]$ direction $(\mathrm{\AA})$',fontsize=35,labelpad=5)

plt.savefig('binding_energy.pdf', bbox_inches="tight")
plt.show()
