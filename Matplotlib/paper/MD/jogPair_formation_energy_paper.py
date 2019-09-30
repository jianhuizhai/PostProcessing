import sys
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pylab as plt

def func_dec(x ,pre, exponent,const):
    return pre*np.power(exponent,x)+const
def func_inc(x, pre, exponent, const):
    return pre*exponent/x + const
#==================================================================================
filename    = sys.argv[1]

#==================================================================================
size, energy, elastic_int = np.loadtxt(filename, usecols=(0,1,2), unpack=True)

#print('filename.split()[0] is :', filename.split('.')[0])
#  multiply 0.5 is to change two jog pair energy to one jog pair energy
energy      = 0.5*energy
elastic_int = 0.5*elastic_int   

'''
#plot_flag = input("Do you want to fit (y or n) : ")
#if(plot_flag == 'y' or plot_flag == 'Y'):
func_flag = input("Inverse fit or exponent fit (1 or 2) : ")
if(func_flag == '1'):
    func = func_inc
    flag = 'inverse'
elif(func_flag == '2'):
    func = func_dec
    flag = 'exponent'

##popt, pcov = curve_fit(func, size[0:3], energy[0:3])
popt, pcov = curve_fit(func, size, energy, maxfev=10000)
pre      = popt[0]
exponent = popt[1]
const    = popt[2]

x=[i for i in np.arange(0.5*np.min(size),2.0*np.max(size),0.05)]
x = np.array(x)
yvals=func(x, pre, exponent, const)
#print('cell size equal 80', func(80, pre, exponent, const) )
#print('The denominator  = ', pre*exponent )
#print('formation energy = ', func(2000, pre, exponent, const) )
#print('formation energy = ', const )
'''

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
plt.xticks(fontsize=36)
plt.yticks(fontsize=36)


#plt.plot(x, yvals, 'r',linewidth=5.0,label='fit')       # fitting data
plt.hlines(np.mean(energy-elastic_int), 0.7*size[0], 1.2*size[-1],linestyles='dashed', linewidth=4 )
print('='*80)
print('The formation energy :{:6.4f} eV.'.format( np.mean(energy-elastic_int) ) )
plt.scatter( size, energy, s=500, color='',edgecolors='black', linewidths=6 )
plt.scatter( size, energy-elastic_int, s=500, marker='s',color='',edgecolors='black',linewidths=6)


plt.xlabel(r'$[001]/a$', fontsize='40')
plt.ylabel(r'$H_{jp}\ (\mathrm{eV})$', fontsize='40')

plt.xlim(15, 45)
#plt.ylim(2.4, 2.8)  ## unit jog
plt.ylim(5.8, 6.3)   ## super jog II (type1)
#plt.ylim(4.7, 5.1)   ## super jog II (type2)
plt.savefig(filename.split('.')[0]+'.pdf', bbox_inches="tight")
plt.show()
