import os
import numpy as np
import matplotlib.pylab as plt
import sys


number=int(sys.argv[1])
step1 =int(sys.argv[2])
x1    =float(sys.argv[3])
x2    =float(sys.argv[4])

col = 0
file1=np.zeros((number,1000+1))
position1=np.zeros(1000+1)
r1=np.zeros((number,1000+1))

# ---------------------------------------------------------------------------------
for i in range(number):
	os.chdir('/home/jhzhai/jhzhai/Results/600K/'+'sim'+repr(i+1))
	name1=repr(step1).zfill(8)+'p.dat'
	file1[i]=np.loadtxt(name1,usecols=[col])
	for d in range(0,1001,1):
		h1=np.zeros(len(position1)-d)
		for j in range(0,len(position1)-d):
			h1[j]=file1[i][j]-file1[i][j+d]
		r1[i][d]=np.mean(np.abs(h1))
	print(os.getcwd())
#----------------------------------------------------------------------------------
f1=np.zeros(1000+1)
for i in range(0,number):
	f1=r1[i]+f1
f1=f1/number
print('value at x1 is',f1[int(np.exp(x1))])
print('value at x2 is',f1[int(np.exp(x2))])
mean=np.mean(f1[int(np.exp(x1)):int(np.exp(x2))])
print('mean=',mean)
print('mean value in log scale')
print('log.mean=',np.log(mean))

# print('f1[int(np.exp(y1)):int(np.exp(y2))]=',f1[int(np.exp(y1)):int(np.exp(y2))])
begin = 1
end = 999
x=[i for i in range(0,1001)]
plt.plot(np.log(x[begin:end]),np.log(mean)*np.ones(end-begin),'--',color='black')
plt.plot(np.log(x[begin:end]),np.log(f1[begin:end]),label=repr(step1))
plt.vlines(x1, -8, -6.5, colors = "c", linestyles = "dashed")
plt.vlines(x2, -8, -6.5, colors = "c", linestyles = "dashed")

end1=5

z1=np.polyfit(np.log(x[begin:end1]),np.log(f1[begin:end1]),1)
print('z1=',z1)
p1 =np.poly1d(z1)
yvals=p1(np.log(x[begin:end1]))
plot2=plt.plot(np.log(x[begin:end1]), yvals, 'r',label='polyfit values')

plt.legend()
plt.show()