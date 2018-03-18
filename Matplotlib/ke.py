import  numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import sys

ymajorLocator   = MultipleLocator(20)
xmajorLocator   = MultipleLocator(500)
ke=np.loadtxt('ke_ave.dat',usecols=[3])/(10**(-11.)*1.38064852*0.5)
T=np.loadtxt('ke_ave.dat',usecols=[2])/(10**(-11.)*1.38064852*0.5)

begin=1
end=int(sys.argv[1])
fig = plt.figure()

if(len(sys.argv)>2):
	count=int(sys.argv[2])
	mean=np.mean(ke[count:end])
	print('mean temp=',mean)
x=[i+1 for i in range(begin,end)]
plt.plot(x,T[begin:end],'--',linewidth=2.0,color='b')
plt.plot(x,ke[begin:end],'-',linewidth=2.0,color='r')
plt.xlim(0,end)
plt.ylim(0,T[1]*1.5)
plt.minorticks_on()
plt.tick_params(which='major',direction='in',width=1.5,length=5)  # 
plt.tick_params(which='minor',direction='in',width=1.5,length=3)
ax = plt.subplot(1,1,1)

ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('simulation time step',fontsize=12)
plt.ylabel('T(K)',fontsize=12)

if(len(sys.argv)>3):
	plt.plot(x,np.ones(len(x))*(T[1]+100),'--',linewidth=2.0,color='b')
	plt.plot(x,np.ones(len(x))*(T[1]-100),'--',linewidth=2.0,color='b')
	plt.plot(x,np.ones(len(x))*(T[1]+50),'--',linewidth=2.0,color='b')
	plt.plot(x,np.ones(len(x))*(T[1]-50),'--',linewidth=2.0,color='b')

if(len(sys.argv)>4):
	left, bottom, width, height = 0.4, 0.2, 0.3, 0.3
	begin1=2000;end1=4000
	ax2 = fig.add_axes([left, bottom, width, height])

	ax2.plot(x[begin1:end1],ke[begin1:end1], 'r')
	ax2.plot(x[begin1:end1],T[begin1:end1],'--',linewidth=2.0,color='b')
	plt.xlim([begin1,end1])
	plt.ylim([260,340])
	plt.minorticks_on()
	plt.tick_params(which='major',direction='in',width=1.5,length=5)  # 
	plt.tick_params(which='minor',direction='in',width=1.5,length=3)
	ax2.spines['left'].set_linewidth(1.5)
	ax2.spines['right'].set_linewidth(1.5)
	ax2.spines['top'].set_linewidth(1.5)
	ax2.spines['bottom'].set_linewidth(1.5)
	plt.xticks(fontsize=12)
	plt.yticks(fontsize=12)
	ax2.yaxis.set_major_locator(ymajorLocator)
	ax2.xaxis.set_major_locator(xmajorLocator)   
plt.show()
