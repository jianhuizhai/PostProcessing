import  numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import sys

ymajorLocator   = MultipleLocator(60)
xmajorLocator   = MultipleLocator(0.02)

# name='ke_ave'+repr(1200)+'.dat'
name='ke_ave.dat'
ke=np.loadtxt(name,usecols=[3])/(10**(-11.)*1.38064852*0.5)
T=np.loadtxt(name,usecols=[2])/(10**(-11.)*1.38064852*0.5)

begin=0
end=int(sys.argv[1])
fig = plt.figure()

if(len(sys.argv)>2):
	count=int(sys.argv[2])
	mean=np.mean(ke[count:end])
	print('mean temp=',mean)
x=[(i+1)*10**(-5)*5 for i in range(begin,end)]

plt.plot(x,ke[begin:end],'-',linewidth=5.0,color='r')
plt.plot(x,T[begin:end],'--',linewidth=5.0,color='b')

plt.xlim(0,end*10**(-5)*5)
plt.ylim(0,T[1]+400)
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


# plt.xticks(fontsize=20c)
plt.xticks(fontsize=30)
plt.yticks(fontsize=30)
plt.xlabel('simulation time(ns)',fontsize=35,labelpad=5)
plt.ylabel('Temperature(K)',fontsize=35,labelpad=5)
# plt.ylabel('T(K)',fontsize=20,fontweight='bold',labelpad=20)

if(len(sys.argv)>3):
	plt.plot(x,np.ones(len(x))*(T[1]+200),'--',linewidth=5.0,color='b')
	plt.plot(x,np.ones(len(x))*(T[1]-200),'--',linewidth=5.0,color='b')
	# plt.plot(x,np.ones(len(x))*(T[1]+150),'--',linewidth=5.0,color='b')
	# plt.plot(x,np.ones(len(x))*(T[1]-150),'--',linewidth=5.0,color='b')

if(len(sys.argv)>4):
	left, bottom, width, height = 0.3, 0.21, 0.4, 0.35

	begin1=int(sys.argv[5]);end1=int(sys.argv[6])
	print('mean_small_volume=',np.mean(ke[begin1:end1]))
	ax2 = fig.add_axes([left, bottom, width, height])

	ax2.plot(x[begin1:end1],ke[begin1:end1],linewidth=5.0,color='r')
	ax2.plot(x[begin1:end1],T[begin1:end1],'--',linewidth=5.0,color='b')
	#ax2.xaxis.get_major_formatter().set_powerlimits((0,10))
	fig.set_size_inches(18.5, 10.5)
	plt.xlim(x[begin1],x[end1])
	if(len(sys.argv)>7):
		d=int(sys.argv[7])
		plt.ylim([T[1]-d,T[1]+d])
	plt.minorticks_on()
	plt.tick_params(which='major',direction='in',width=3.0,length=12)  # 
	plt.tick_params(which='minor',direction='in',width=3.0,length=5)
	ax2.spines['left'].set_linewidth(3.0)
	ax2.spines['right'].set_linewidth(3.0)
	ax2.spines['top'].set_linewidth(3.0)
	ax2.spines['bottom'].set_linewidth(3.0)
	ax2.tick_params(axis='x', pad=10)  # distance between axis and text
	ax2.tick_params(axis='y', pad=10)
	plt.xticks(fontsize=25)
	plt.yticks(fontsize=25)
	ax2.yaxis.set_major_locator(ymajorLocator)
	ax2.xaxis.set_major_locator(xmajorLocator)
	plt.savefig('ke1200.pdf',dpi=200)
plt.show()