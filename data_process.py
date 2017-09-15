import numpy as np
import matplotlib.pylab as plt
f=np.loadtxt('0001.dat')/10**6
x=[i for i in range(0,len(f),1)]
print(f.mean())
print(f.std())
# b is blue, g is green, r is red, c is cyan, m is magenta, y is yellow, k is black, w is white
# '-' is solid, '--' is dashed, '-,' is dash_dot, ':' is dotted, 'None' draw nothing, ' ' draw nothing, '' draw nothing
# 's' square marker, 'p' pentagon marker, '*' star marker, 'h' hexagona1 marker, 'H' hexagon2 marker
# '+' plus marker, 'x' x marker, 'D' diamond marker, 'd' thin diamond marker
plt.plot(x,f,linewidth=2.0,color='b')
plt.plot(x,[0]*len(x),'--',linewidth=2.0,color='g',)
plt.xlabel('node ID')
plt.ylabel('distribution of velocity')
plt.grid(True)
# plt.xlim([0,20]);plt.ylim(-8000,8000)
plt.show()