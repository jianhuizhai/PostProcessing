import numpy as np
import sys
import matplotlib.pylab as plt
# d is the number of another node

step1=int(sys.argv[1])
bmag=2.56*10**(-10.0)
step2=int(sys.argv[2])
step3=int(sys.argv[3])
step4=int(sys.argv[4])

col=0
# ----------------------------------------------------------------------------------------
name1=repr(step1)
name1=name1.zfill(8)+'p.dat'
name2=repr(step2)
name2=name2.zfill(8)+'p.dat'
name3=repr(step3)
name3=name3.zfill(8)+'p.dat'
name4=repr(step4)
name4=name4.zfill(8)+'p.dat'
#------------------------------------------------------------------------------------------
position1=np.zeros(1000+1)
position2=np.zeros(1000+1)
position3=np.zeros(1000+1)
position4=np.zeros(1000+1)

r1=np.zeros(1000+1)
r2=np.zeros(1000+1)
r3=np.zeros(1000+1)
r4=np.zeros(1000+1)

position1=np.loadtxt(name1,usecols=[col])
position2=np.loadtxt(name2,usecols=[col])
position3=np.loadtxt(name3,usecols=[col])
position4=np.loadtxt(name4,usecols=[col])
# ------------------------------------------------------------------------------------

for d in range(0,1001,1):
	h1=np.zeros(len(position1)-d+1)
	h2=np.zeros(len(position1)-d+1)
	h3=np.zeros(len(position1)-d+1)
	h4=np.zeros(len(position1)-d+1)
	for i in range(0,len(position1)-d):
		h1[i]=position1[i]-position1[i+d]
		h2[i]=position2[i]-position2[i+d]
		h3[i]=position3[i]-position3[i+d]
		h4[i]=position4[i]-position4[i+d]
	r1[d]=np.mean(np.abs(h1))
	r2[d]=np.mean(np.abs(h2))
	r3[d]=np.mean(np.abs(h3))
	r4[d]=np.mean(np.abs(h4))

#------------------------------------------------------------------------------------
begin = 1
end = 999
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x=[i+1 for i in range(0,1001)]

plt.plot(x[begin:end],r1[begin:end],label='step1')
plt.plot(x[begin:end],r2[begin:end],label='step2')
plt.plot(x[begin:end],r3[begin:end],label='step3')
plt.plot(x[begin:end],r4[begin:end],label='step4')

z1=np.polyfit(x[begin:end],r1[begin:end],3)
p1 =np.poly1d(z1) 
yvals=p1(x[begin:end])
#plot2=plt.plot(x[1:end], yvals, 'r',label='polyfit values')
#plt.plot(x,np.zeros(len(x)))
ax.set_xscale('log')
ax.set_yscale('log')
plt.legend()
plt.show()

# -----------------------------------------------------------------------------------------
