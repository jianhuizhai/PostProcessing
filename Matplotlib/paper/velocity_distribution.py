import numpy as np
from scipy import stats
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import sys

xmajorLocator   = MultipleLocator(50)



begin = int(sys.argv[1])
end   = int(sys.argv[2])
point = int(sys.argv[3])
col=0


kb=10**(-23.)*1.38064852
rho=8.9*10**(3.)
bmag=2.56*10**(-10.0)
m=0.5*rho*bmag**2

if(len(sys.argv)>4):
	L=int(sys.argv[4])*bmag
if(len(sys.argv)>5):
	T=int(sys.argv[5])
std_theory=np.sqrt(kb*T/(m*L))
velocity=np.zeros(end-begin+1)
# ----------------------------------------------------------------------------
j=0

for i in range(begin,end+1,1):
	name=repr(i)
	name=name.zfill(8)+'n.dat'
	v=np.loadtxt(name,usecols=[col])/(10**6)
	velocity[j]=v[point-1]
	j=j+1

mean=np.mean(velocity)
std=np.std(velocity)


v=np.arange(-400,400,0.5)
fv=stats.norm.pdf(v,mean,std)
print('mean=',mean)
print('std=',std)

print('theory of std=',std_theory)


#--------------------------------------------------------------------
plt.figure(figsize=(16,10))
ax = plt.subplot(1,1,1)
ax.tick_params(axis='x', pad=15)  # distance between axis and text
ax.tick_params(axis='y', pad=15)
#--------------------------------------------------------------------
ax.spines['left'].set_linewidth(3.0)
ax.spines['right'].set_linewidth(3.0)
ax.spines['top'].set_linewidth(3.0)
ax.spines['bottom'].set_linewidth(3.0)
# ax.legend(loc=1,fontsize=20,frameon=True,edgecolor='black')

# bins : 11,20,40,0
# normed was deprecated in Matplotlib 2.1 and will be removed in 3.1.
#plt.hist(velocity, 50, normed=True)
plt.hist(velocity, 50, density=True)

plt.xlabel('v(m/s)',fontsize='35')
plt.ylabel('Probability',fontsize='35')
plt.plot(v,fv,'k-',label='fit',linewidth='5')
plt.plot(v,stats.norm.pdf(v,0,std_theory),'r-',label='theory',linewidth='5')

plt.minorticks_on()
plt.tick_params(which='major',direction='in',width=3.0,length=12)  # 
plt.tick_params(which='minor',direction='in',width=3.0,length=5)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlim(-250,250)
plt.ylim(0,0.01)

lg=plt.legend(loc=1,bbox_to_anchor=(0.98,0.98),fontsize=30,frameon=True,edgecolor='black')
lg.get_frame().set_linewidth(5)
# lg.get_frame().set_edgecolor("red")  # set the color of frame to red
ax.xaxis.set_major_locator(xmajorLocator)

plt.savefig("velocity300.pdf",bbox_inches="tight")
plt.show()
