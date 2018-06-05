import os
import numpy as np
import matplotlib.pylab as plt
import sys
from matplotlib.ticker import MultipleLocator, FormatStrFormatter

xmajorLocator   = MultipleLocator(1)

col = 0
number = 6
# ---------------------------------------------------------------------------------
f1 = np.loadtxt('1000.dat',usecols=[col])
f2 = np.loadtxt('5000.dat',usecols=[col])
f3 = np.loadtxt('10000.dat',usecols=[col])
f4 = np.loadtxt('20000.dat',usecols=[col])
f5 = np.loadtxt('40000.dat',usecols=[col])
f6 = np.loadtxt('50000.dat',usecols=[col])
#----------------------------------------------------------------------------------
time = np.zeros(number)
kesi = np.zeros(number)

w1    = np.zeros(1001)
w2    = np.zeros(1001)
w3    = np.zeros(1001)
w4    = np.zeros(1001)
w5    = np.zeros(1001)
w6    = np.zeros(1001)


time[0] = 1000*5*10**(-14)/(10**(-9))
time[1] = 5000*5*10**(-14)/(10**(-9))
time[2] = 10000*5*10**(-14)/(10**(-9))
time[3] = 20000*5*10**(-14)/(10**(-9))
time[4] = 40000*5*10**(-14)/(10**(-9))
time[5] = 50000*5*10**(-14)/(10**(-9))

begin = 1
end = 1000
x=[i for i in range(0,1001)]

p = 2.3
z = 0.25

# w2[i] = time[1]**(kesi[1]/z)*f(i/kesi[1],p,c)*f2[i]

for i in range(0,1001):
	w1[i] = f1[i]/time[0]**z
	w2[i] = f2[i]/time[1]**z
	w3[i] = f3[i]/time[2]**z
	w4[i] = f4[i]/time[3]**z
	w5[i] = f5[i]/time[4]**z
	w6[i] = f6[i]/time[5]**z

fig = plt.figure()
fig.set_size_inches(18.5, 10.5)

#plt.plot(np.log(x[begin:end]),np.log(f1[begin:end]),label=repr(round(1000*5*10**(-5),2))+'ns',linewidth=5.0,color='blue')
#plt.plot(np.log(x[begin:end]),np.log(f2[begin:end]),label=repr(round(5000*5*10**(-5),2))+'ns',linewidth=5.0,color='green')
#plt.plot(np.log(x[begin:end]),np.log(f3[begin:end]),label=repr(round(10000*5*10**(-5),1))+'ns',linewidth=5.0,color='red')
#plt.plot(np.log(x[begin:end]),np.log(f4[begin:end]),label=repr(round(20000*5*10**(-5),1))+'ns',linewidth=5.0,color='olive')
#plt.plot(np.log(x[begin:end]),np.log(f5[begin:end]),label=repr(round(40000*5*10**(-5),1))+'ns',linewidth=5.0,color='magenta')
#plt.plot(np.log(x[begin:end]),np.log(f6[begin:end]),label=repr(round(50000*5*10**(-5),1))+'ns',linewidth=5.0,color='black')

plt.plot(np.log(x[begin:end]/time[0]**(p*z)),np.log(w1[begin:end]),label=repr(round(1000*5*10**(-5),2))+'ns',linewidth=5.0,color='blue')
plt.plot(np.log(x[begin:end]/time[1]**(p*z)),np.log(w2[begin:end]),label=repr(round(5000*5*10**(-5),2))+'ns',linewidth=5.0,color='green')
plt.plot(np.log(x[begin:end]/time[2]**(p*z)),np.log(w3[begin:end]),label=repr(round(10000*5*10**(-5),1))+'ns',linewidth=5.0,color='red')
plt.plot(np.log(x[begin:end]/time[3]**(p*z)),np.log(w4[begin:end]),label=repr(round(20000*5*10**(-5),1))+'ns',linewidth=5.0,color='olive')
plt.plot(np.log(x[begin:end]/time[4]**(p*z)),np.log(w5[begin:end]),label=repr(round(40000*5*10**(-5),1))+'ns',linewidth=5.0,color='magenta')
plt.plot(np.log(x[begin:end]/time[5]**(p*z)),np.log(w6[begin:end]),label=repr(round(50000*5*10**(-5),1))+'ns',linewidth=5.0,color='black')

plt.xlim(-1,9)
plt.ylim(-9.5,-7.0)
plt.minorticks_on()
plt.tick_params(which='major',direction='in',width=3.0,length=12)  # 
plt.tick_params(which='minor',direction='in',width=3.0,length=5)
ax = plt.subplot(1,1,1)
#--------------------------------------------------------------------
ax.tick_params(axis='x', pad=15)  # distance between axis and text
ax.tick_params(axis='y', pad=15)
#--------------------------------------------------------------------
ax.spines['left'].set_linewidth(3.0)
ax.spines['right'].set_linewidth(3.0)
ax.spines['top'].set_linewidth(3.0)
ax.spines['bottom'].set_linewidth(3.0)

plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('log(d/'+r'$t^{2.3*0.25}$'+')',fontsize=35,labelpad=0)
plt.ylabel('log(R/t'+r'$^{0.25}$'+')',fontsize=35,labelpad=2)

end1=5

z1=np.polyfit(np.log(x[begin:end1]),np.log(f1[begin:end1]),1)
z2=np.polyfit(np.log(x[begin:end1]),np.log(f2[begin:end1]),1)
z3=np.polyfit(np.log(x[begin:end1]),np.log(f3[begin:end1]),1)
z4=np.polyfit(np.log(x[begin:end1]),np.log(f4[begin:end1]),1)
z5=np.polyfit(np.log(x[begin:end1]),np.log(f5[begin:end1]),1)
z6=np.polyfit(np.log(x[begin:end1]),np.log(f6[begin:end1]),1)
#print('z1=',z1)
#print('z2=',z2)
#print('z3=',z3)
#print('z4=',z4)
#print('z5=',z5)
#print('z6=',z6)

ax.xaxis.set_major_locator(xmajorLocator)
lg=plt.legend(loc=2,bbox_to_anchor=(0.015,0.98),fontsize=28,frameon=True,edgecolor='black')
lg.get_frame().set_linewidth(4)
plt.savefig('scaling300K.pdf',bbox_inches="tight")
plt.show()