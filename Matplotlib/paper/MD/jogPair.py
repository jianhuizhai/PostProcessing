import numpy as np
import os
from search import SearchFile
import matplotlib.pylab as plt

#========================================================================================
linecommon = '===============================================================\n'

#========================================================================================
os.chdir("edge")
filename_dipole = SearchFile.findfile('.', 'DislocInfo_', '.')[2:]
print("filename is ", filename_dipole)
dipole = np.loadtxt(filename_dipole, usecols=(4,5),skiprows=9)

os.chdir("../jog")
filename_jog = SearchFile.findfile('.', 'DislocInfo_', '.')[2:]
print("filename is ", filename_jog)
jog = np.loadtxt(filename_jog, usecols=(4,5),skiprows=9)
#========================================================================================
os.chdir("../")
plt.figure(figsize=(18.5,10.5))
ax = plt.subplot(1,1,1)

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
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)

#-----------------------------------------------------------------------------------
#                           plot data       
#-----------------------------------------------------------------------------------
plt.scatter(dipole[:,1], dipole[:,0], s=200)  # x axis is z coordinate, y axis is y coordinate
plt.scatter(jog[:,1], jog[:,0], s=200)

plt.xlim(0,84.36)

plt.xlabel(r'$z\ \mathrm{(\AA)}$', fontsize='35')
plt.ylabel(r'$y\ \mathrm{(\AA)}$', fontsize='35')

#lg=plt.legend(loc=2,bbox_to_anchor=(0.02,1.0),fontsize=28,frameon=True,edgecolor='black')
#lg.get_frame().set_linewidth(4)

plt.savefig('jog_pair.pdf',bbox_inches="tight")
plt.show()