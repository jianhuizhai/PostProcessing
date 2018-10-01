import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
# time series are: 1000,2000,4000,8000,10000,20000,40000,50000,60000,30000
#					0	  1    2    3    4      5    6      7    8     9
xmajorLocator   = MultipleLocator(0.5)


number=10
f	=np.zeros(number)
time=np.zeros(number)

time[0]=1000
time[1]=2000
time[2]=4000
time[3]=8000
time[4]=10000
time[5]=20000
time[6]=40000
time[7]=50000
time[8]=60000
time[9]=30000
time=time*5*10**(-2)
print('time=',time)

f[0]=0.00046762704484088201
f[1]=0.00054856690913207768
f[2]=0.00065915485697024803
f[3]=0.00075952712348220967
f[4]=0.00079372264429317021
f[5]=0.00095575470358116063
f[6]=0.0011257554868846749
f[7]=0.0011461072059054996
f[8]=0.001235410671431897 
f[9]=0.0010494635810065782

fig = plt.figure()
fig.set_size_inches(18.5, 10.5)

plt.scatter(np.log(time),np.log(f),s=200.0,color='blue',label='simulation')
#plt.plot(np.log(time),np.log(f),'o',color='blue',label='simulation')
#plt.xlabel('log(t(ps))')
#plt.ylabel('log('+r'$\overline{R}$'+')')

z1=np.polyfit(np.log(time),np.log(f),1)
print('z1=',z1)
p1 =np.poly1d(z1)
yvals=p1(np.log(time))
plt.plot(np.log(time), yvals, 'r',linewidth=5.0,color='red',label='fit')

plt.xlim(3.5,8.5)
plt.ylim(-7.8,-6.6)
plt.minorticks_on()
plt.tick_params(which='major',direction='in',width=3.0,length=12)  # 
plt.tick_params(which='minor',direction='in',width=3.0,length=5)

ax = plt.subplot(1,1,1)
#--------------------------------------------------------------------
ax.tick_params(axis='x', pad=13)  # distance between axis and text
ax.tick_params(axis='y', pad=13)

ax.spines['left'].set_linewidth(3.0)
ax.spines['right'].set_linewidth(3.0)
ax.spines['top'].set_linewidth(3.0)
ax.spines['bottom'].set_linewidth(3.0)


plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('log(t(ps))',fontsize=35,labelpad=2)
plt.ylabel('log('+r'$\overline{R}$'+')',fontsize=35,labelpad=2)


lg=plt.legend(loc=2,bbox_to_anchor=(0.015,0.98),fontsize=28,frameon=True,edgecolor='black')
lg.get_frame().set_linewidth(4)

ax.xaxis.set_major_locator(xmajorLocator)
plt.savefig('position_time600K.pdf',bbox_inches="tight")
plt.show()
