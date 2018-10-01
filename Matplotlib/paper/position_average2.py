import os
import numpy as np
import matplotlib.pylab as plt
import sys


number=int(sys.argv[1])
step1 =int(sys.argv[2])

col = 0
file1=np.zeros((number,1000+1))
position1=np.zeros(1000+1)
r1=np.zeros((number,1000+1))
name1=repr(step1).zfill(8)+'p.dat'

step2 =int(sys.argv[3])
file2=np.zeros((number,1000+1))
r2=np.zeros((number,1000+1))
name2=repr(step2).zfill(8)+'p.dat'

step3 =int(sys.argv[4])
file3=np.zeros((number,1000+1))
r3=np.zeros((number,1000+1))
name3=repr(step3).zfill(8)+'p.dat'

step4 =int(sys.argv[5])
file4=np.zeros((number,1000+1))
r4=np.zeros((number,1000+1))
name4=repr(step4).zfill(8)+'p.dat'

step5 =int(sys.argv[6])
file5=np.zeros((number,1000+1))
r5=np.zeros((number,1000+1))
name5=repr(step5).zfill(8)+'p.dat'

step6 =int(sys.argv[7])
file6=np.zeros((number,1000+1))
r6=np.zeros((number,1000+1))
name6=repr(step6).zfill(8)+'p.dat'
# ---------------------------------------------------------------------------------
for i in range(number):
	os.chdir('/home/jhzhai/jhzhai/Results/600K/'+'sim'+repr(i+1))
	

	file1[i]=np.loadtxt(name1,usecols=[col])
	file2[i]=np.loadtxt(name2,usecols=[col])
	file3[i]=np.loadtxt(name3,usecols=[col])
	file4[i]=np.loadtxt(name4,usecols=[col])
	file5[i]=np.loadtxt(name5,usecols=[col])
	file6[i]=np.loadtxt(name6,usecols=[col])

	for d in range(0,1001,1):
		h1=np.zeros(len(position1)-d)
		h2=np.zeros(len(position1)-d)
		h3=np.zeros(len(position1)-d)
		h4=np.zeros(len(position1)-d)
		h5=np.zeros(len(position1)-d)
		h6=np.zeros(len(position1)-d)
		for j in range(0,len(position1)-d):
			h1[j]=file1[i][j]-file1[i][j+d]
			h2[j]=file2[i][j]-file2[i][j+d]
			h3[j]=file3[i][j]-file3[i][j+d]
			h4[j]=file4[i][j]-file4[i][j+d]
			h5[j]=file5[i][j]-file5[i][j+d]
			h6[j]=file6[i][j]-file6[i][j+d]
			
		r1[i][d]=np.mean(np.abs(h1))
		r2[i][d]=np.mean(np.abs(h2))
		r3[i][d]=np.mean(np.abs(h3))
		r4[i][d]=np.mean(np.abs(h4))
		r5[i][d]=np.mean(np.abs(h5))
		r6[i][d]=np.mean(np.abs(h6))
	print(os.getcwd())

#----------------------------------------------------------------------------------
#			change folder direction to save figure in parent folder
#----------------------------------------------------------------------------------

os.chdir('/home/jhzhai/jhzhai/Results/600K')
print(os.getcwd())
#----------------------------------------------------------------------------------

f1=np.zeros(1000+1)
f2=np.zeros(1000+1)
f3=np.zeros(1000+1)
f4=np.zeros(1000+1)
f5=np.zeros(1000+1)
f6=np.zeros(1000+1)

for i in range(0,number):
	f1=r1[i]+f1
	f2=r2[i]+f2
	f3=r3[i]+f3
	f4=r4[i]+f4
	f5=r5[i]+f5
	f6=r6[i]+f6

# -----------------------------------------------------------------
f1=f1/number
f2=f2/number
f3=f3/number
f4=f4/number
f5=f5/number
f6=f6/number

#------------------------------------------------------------------------------------

begin = 1
end = 999
x=[i for i in range(0,1001)]

fig = plt.figure()
fig.set_size_inches(18.5, 10.5)

plt.plot(np.log(x[begin:end]),np.log(f1[begin:end]),label=repr(round(step1*5*10**(-5),2))+'ns',linewidth=5.0,color='blue')
plt.plot(np.log(x[begin:end]),np.log(f2[begin:end]),label=repr(round(step2*5*10**(-5),2))+'ns',linewidth=5.0,color='green')
plt.plot(np.log(x[begin:end]),np.log(f3[begin:end]),label=repr(round(step3*5*10**(-5),1))+'ns',linewidth=5.0,color='red')
plt.plot(np.log(x[begin:end]),np.log(f4[begin:end]),label=repr(round(step4*5*10**(-5),1))+'ns',linewidth=5.0,color='olive')
plt.plot(np.log(x[begin:end]),np.log(f5[begin:end]),label=repr(round(step5*5*10**(-5),1))+'ns',linewidth=5.0,color='magenta')
plt.plot(np.log(x[begin:end]),np.log(f6[begin:end]),label=repr(round(step6*5*10**(-5),1))+'ns',linewidth=5.0,color='black')

plt.xlim(0,7)
plt.ylim(-9,-6.5)
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
plt.xlabel('log(d)',fontsize=35,labelpad=0)
plt.ylabel('log(R)',fontsize=35,labelpad=2)

end1=5

z1=np.polyfit(np.log(x[begin:end1]),np.log(f1[begin:end1]),1)
z2=np.polyfit(np.log(x[begin:end1]),np.log(f2[begin:end1]),1)
z3=np.polyfit(np.log(x[begin:end1]),np.log(f3[begin:end1]),1)
z4=np.polyfit(np.log(x[begin:end1]),np.log(f4[begin:end1]),1)
z5=np.polyfit(np.log(x[begin:end1]),np.log(f5[begin:end1]),1)
z6=np.polyfit(np.log(x[begin:end1]),np.log(f6[begin:end1]),1)
print('z1=',z1)
print('z2=',z2)
print('z3=',z3)
print('z4=',z4)
print('z5=',z5)
print('z6=',z6)

lg=plt.legend(loc=2,bbox_to_anchor=(0.015,0.98),fontsize=28,frameon=True,edgecolor='black')
lg.get_frame().set_linewidth(4)
plt.savefig('position600K.pdf',bbox_inches="tight")
plt.show()
