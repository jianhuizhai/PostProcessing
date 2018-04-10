import  numpy as np
import matplotlib.pylab as plt
import sys
# ke_ave1=np.loadtxt('KE_ave10000.dat',usecols=[3])/(10**(-11.)*1.38064852*2)
# Temp1=np.loadtxt('KE_ave10000.dat',usecols=[2])/(10**(-11.)*1.38064852*2)
ke_ave2=np.loadtxt('ke_ave.dat',usecols=[3])/(10**(-11.)*1.38064852*0.5)
Temp2=np.loadtxt('ke_ave.dat',usecols=[2])/(10**(-11.)*1.38064852*0.5)

begin=1
end=int(sys.argv[1])

# if(len(sys.argv)>3):
	# =int(sys.argv[3])
if(len(sys.argv)>2):
	count=int(sys.argv[2])
	mean=np.mean(ke_ave2[count:end])
	print('mean temp=',mean)
x=[i+1 for i in range(begin,end)]
plt.plot(x,Temp2[begin:end],'--',linewidth=2.0,color='g')
# plt.plot(x,ke_ave1,'--',linewidth=2.0,color='g')
plt.plot(x,ke_ave2[begin:end],'-',linewidth=2.0,color='r')
#plt.plot(x,np.ones(len(x))*400,'-',linewidth=2.0,color='b')
if(len(sys.argv)>3):
	plt.plot(x,np.ones(len(x))*(Temp2[1]),'--',linewidth=2.0,color='b')
	plt.plot(x,np.ones(len(x))*(Temp2[1]+100),'--',linewidth=2.0,color='b')
	plt.plot(x,np.ones(len(x))*(Temp2[1]-100),'--',linewidth=2.0,color='b')
	plt.plot(x,np.ones(len(x))*(Temp2[1]+50),'--',linewidth=2.0,color='b')
	plt.plot(x,np.ones(len(x))*(Temp2[1]-50),'--',linewidth=2.0,color='b')
# print(2*np.pi*np.sqrt(2.9157*10**(-16.)/(3.*10**(-5.))))
# plt.xlim(0.0, 3000)# set axis limits
#plt.ylim(0.0, 120)
plt.show()