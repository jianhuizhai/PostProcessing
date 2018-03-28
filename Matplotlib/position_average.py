import numpy as np
import sys
import matplotlib.pylab as plt
# d is the number of another node


step1='00001000p'
step2='00005000p'
step3='00010000p'
step4='00020000p'
step5='00040000p'
step6='00060000p'

col=0

number=10

file1=np.zeros((number,1000+1))
file2=np.zeros((number,1000+1))
file3=np.zeros((number,1000+1))
file4=np.zeros((number,1000+1))
file5=np.zeros((number,1000+1))
file6=np.zeros((number,1000+1))

# ----------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------
position1=np.zeros(1000+1)
position2=np.zeros(1000+1)
position3=np.zeros(1000+1)
position4=np.zeros(1000+1)
position5=np.zeros(1000+1)
position6=np.zeros(1000+1)

r1=np.zeros((number,1000+1))
r2=np.zeros((number,1000+1))
r3=np.zeros((number,1000+1))
r4=np.zeros((number,1000+1))
r5=np.zeros((number,1000+1))
r6=np.zeros((number,1000+1))


#position2=np.loadtxt(name2,usecols=[col])
#position3=np.loadtxt(name3,usecols=[col])
#position4=np.loadtxt(name4,usecols=[col])
#position5=np.loadtxt(name5,usecols=[col])
#position6=np.loadtxt(name6,usecols=[col])
# ------------------------------------------------------------------------------------
for i in range(0,number):
	name1=step1+repr(i+1)+'.dat'
	name2=step2+repr(i+1)+'.dat'
	name3=step3+repr(i+1)+'.dat'
	name4=step4+repr(i+1)+'.dat'
	name5=step5+repr(i+1)+'.dat'
	name6=step6+repr(i+1)+'.dat'

	position1=np.loadtxt(name1,usecols=[col])

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

print('f1[',begin,']=',f1[begin])
print('f1[',end,']=',f1[end])
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
x=[i for i in range(0,1001)]

plt.plot(np.log(x[begin:end]),np.log(f1[begin:end]),label='step1')
plt.plot(np.log(x[begin:end]),np.log(f2[begin:end]),label='step2')
plt.plot(np.log(x[begin:end]),np.log(f3[begin:end]),label='step3')
plt.plot(np.log(x[begin:end]),np.log(f4[begin:end]),label='step4')
plt.plot(np.log(x[begin:end]),np.log(f5[begin:end]),label='step5')
plt.plot(np.log(x[begin:end]),np.log(f6[begin:end]),label='step6')
#plt.xlim([1,1000])
#plt.ylim([10**(-4),10**(-2)])
if(len(sys.argv)>1):
	end1=int(sys.argv[1])
else:
	end1=8
print('np.log(end1)=',np.log(end1))
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
p1 =np.poly1d(z1)
yvals=p1(np.log(x[begin:end1]))
plot2=plt.plot(np.log(x[begin:end1]), yvals, 'r',label='polyfit values')
#print('coeff=',(yvals[1]-yvals[0])/(np.log(x[2]))-np.log(x[1]))
#ax.set_xscale('log')
#ax.set_yscale('log')
plt.legend()
plt.show()

# -----------------------------------------------------------------------------------------
