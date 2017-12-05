import numpy as np
from line_segments_intersection import line_segments_intersection
x=np.zeros(4);y=np.zeros(4);z=np.zeros(4)
x[0]=0;y[0]=0;z[0]=0

deg=30.
b_mag=10**(-4)
x[1]=1
y[1]=1

x[2]=0;y[2]=0

x[3]=1
y[3]=0
links=[[0,1],[2,3]]
line_segments_intersection(links[0],links[1],x,y)