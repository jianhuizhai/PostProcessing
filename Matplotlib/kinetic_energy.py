import  numpy as np
import matplotlib.pylab as plt
import sys

ax = plt.subplot(1,1,1)

ke_ave2=np.loadtxt('ke_ave.dat',usecols=[3])/(10**(-11.)*1.38064852*0.5)
Temp2=np.loadtxt('ke_ave.dat',usecols=[2])/(10**(-11.)*1.38064852*0.5)

begin=1
end=int(sys.argv[1])

if(len(sys.argv)>2):
	count=int(sys.argv[2])
	mean=sum(ke_ave2[count:end])/(end-count)
	print('mean Temp=',mean)

x=[i+1 for i in range(begin,end)]
plt.plot(x,Temp2[begin:end],'--',linewidth=2.0,color='g')

plt.plot(x,ke_ave2[begin:end],'-',linewidth=2.0,color='r',label='kinetic temperature')

plt.plot(x,np.ones(len(x))*(Temp2[1]),'--',linewidth=2.0,color='b')
plt.plot(x,np.ones(len(x))*(Temp2[1]+50),'--',linewidth=2.0,color='b')
plt.plot(x,np.ones(len(x))*(Temp2[1]-50),'--',linewidth=2.0,color='b')
plt.plot(x,np.ones(len(x))*(Temp2[1]+100),'--',linewidth=2.0,color='b')
plt.plot(x,np.ones(len(x))*(Temp2[1]-100),'--',linewidth=2.0,color='b')
# print(2*np.pi*np.sqrt(2.9157*10**(-16.)/(3.*10**(-5.))))

# set axis limits
plt.xlim(0.0,end)
plt.ylim(0.0,Temp2[1]*1.5)

# set major and minor ticks
plt.minorticks_on()
# plt.minorticks_off()
plt.tick_params(which='major',direction='in',width=1.5,length=5)  # 
plt.tick_params(which='minor',direction='in',width=1.5,length=3)
# plt.tick_params(top='on',bottom='off',left='off',right='off')
# plt.tick_params(labeltop='on',labelbottom='off',labelleft='off',labelright='off')

# plot label
# plt.ylabel('T(K)')
# plt.xlabel('simulation time step')
# plt.legend(loc=0,) # determine position of legend
# plt.legend(bbox_to_anchor=(0.15, 0.15),ncol=2)  # plot more than two legend in one line

ax.spines['left'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['top'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

# set x y axies parameter
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# set label
ax.set_xlabel('simulation time step',fontsize=12)
ax.set_ylabel('T(K)',fontsize=12)

# set parameters of legend
ax.legend(loc=1,fontsize=12,frameon=True,edgecolor='black')

# save picture
plt.savefig("examples.pdf") 
plt.show()
