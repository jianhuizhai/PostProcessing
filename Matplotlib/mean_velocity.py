import numpy as np
import sys
import os

folder = sys.argv[1]
begin  = int(sys.argv[2])
end    = int(sys.argv[3])
os.chdir(folder)
print(os.getcwd())
v=np.loadtxt('mean_velocity.dat',usecols=[1])
# print('len(v)=',len(v))
mean_velocity=np.mean(v[begin:end])
# print('len(v[begin:end])=',len(v[begin:end]))
print('mean_velocity=',mean_velocity)