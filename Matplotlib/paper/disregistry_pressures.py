import numpy as np
import matplotlib.pylab as plt

disreg_100GPa = np.loadtxt('100GPa.dat')
disreg_60GPa  = np.loadtxt('60GPa.dat')
disreg_30GPa  = np.loadtxt('30GPa.dat')
disreg_0GPa   = np.loadtxt('0GPa.dat')

plt.figure(figsize=(18.5,10.5))
ax = plt.subplot(1,1,1)

#------------------------------------------------------------------------------
plt.scatter(disreg_100GPa[:,0], disreg_100GPa[:,1], s=140, label='100GPa')
plt.plot(disreg_100GPa[:,0], disreg_100GPa[:,1],'--', linewidth=3)

plt.scatter(disreg_60GPa[:,0],  disreg_60GPa[:,1], s=140, label='60GPa')
plt.plot(disreg_60GPa[:,0],  disreg_60GPa[:,1], '--', linewidth=3)

plt.scatter(disreg_30GPa[:,0],  disreg_30GPa[:,1], s=140, label='30GPa')
plt.plot(disreg_30GPa[:,0],  disreg_30GPa[:,1], '--', linewidth=3)

plt.scatter(disreg_0GPa[:,0],  disreg_0GPa[:,1],  s=140, label='0GPa')
plt.plot(disreg_0GPa[:,0],  disreg_0GPa[:,1],   '--', linewidth=3)

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
plt.xlim()
plt.ylim(-3.0,0.0)

plt.xlabel('Position along x direction '+r'($\AA$)', fontsize='35')
plt.ylabel('Disregistry '+ r'$\phi (\AA)$', fontsize='35')

lg=plt.legend(fontsize=28,frameon=True,edgecolor='black')
lg.get_frame().set_linewidth(4)
#==================================================================================
plt.savefig('disregistry.pdf')
plt.show()