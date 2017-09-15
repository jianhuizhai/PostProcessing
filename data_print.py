def dataprint(x,y,z,v1,v2,v3,links,k,b_mag,m,T):
    import numpy as np
    name = repr(k + 1)
    name = name.zfill(4) + '.dat'
    'meff is the effective mass of dislocation when calculate need multiply the length of dislocation segment'
    meff =0.5*b_mag**2*m
    kb=10**(-11)*1.38064852
    file=open(name,'w+')
    for i in range(len(links)):
        L = np.sqrt((x[links[i][1]]-x[links[i][0]])**2+(y[links[i][1]]-y[links[i][0]])**2+(
        z[links[i][1]]-z[links[i][0]])**2)
        file.write(str(v1[links[i][0]])+' '+str(v1[links[i][1]])+' '+str(0.5*kb*T)+' '+ str(links[i])
                +' '+str(0.5*meff*L*(v1[links[i][0]]**2+v1[links[i][1]]**2)/2) +'\n')
    file.close()