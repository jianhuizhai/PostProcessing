import numpy as np
import sys
import matplotlib.pylab as plt
# d is the number of another node


name=int(sys.argv[1])
step1=repr(name).zfill(8)+'p'

col=0

file1=np.zeros((6,1000+1))


# ----------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
position1=np.zeros(1000+1)

r1=np.zeros((6,1000+1))

#position2=np.loadtxt(name2,usecols=[col])
#position3=np.loadtxt(name3,usecols=[col])
#position4=np.loadtxt(name4,usecols=[col])
#position5=np.loadtxt(name5,usecols=[col])
#position6=np.loadtxt(name6,usecols=[col])
# ------------------------------------------------------------------------------------
for i in range(0,6):
	name1=step1+repr(i+1)+'.dat'

	position1=np.loadtxt(name1,usecols=[col])

	file1[i]=np.loadtxt(name1,usecols=[col])

	for d in range(0,1001,1):
		h1=np.zeros(len(position1)-d)

		for j in range(0,len(position1)-d):
			h1[j]=file1[i][j]-file1[i][j+d]


		r1[i][d]=np.mean(np.abs(h1))

f1=np.sum([r1[0],r1[1],r1[2],r1[3],r1[4],r1[5]],axis=0)/6

#------------------------------------------------------------------------------------


begin = 1
end = 999

print('f1[',begin,']=',f1[begin])
print('f1[',end,']=',f1[end])
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x=[i for i in range(0,1001)]

plt.plot(np.log(x[begin:end]),np.log(f1[begin:end]),label='step1')

#plt.xlim([1,1000])
#plt.ylim([10**(-4),10**(-2)])
if(len(sys.argv)>2):
	end1=int(sys.argv[2])
else:
	end1=8
print('np.log(end1)=',np.log(end1))
z1=np.polyfit(np.log(x[begin:end1]),np.log(f1[begin:end1]),1)

print('z1=',z1)

p1 =np.poly1d(z1)
yvals=p1(np.log(x[begin:end1]))
plot2=plt.plot(np.log(x[begin:end1]), yvals, 'r',label='polyfit values')
#print('coeff=',(yvals[1]-yvals[0])/(np.log(x[2]))-np.log(x[1]))
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.legend()
plt.show()

# -----------------------------------------------------------------------------------------
