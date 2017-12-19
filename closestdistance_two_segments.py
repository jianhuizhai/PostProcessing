from numpy import dot,cross,array,sqrt,linalg
def closestDistance(a0,a1,b0,b1):
    'finding minimum distance betwen two straight segments'
    'a0-----a1    b0-----b1'
    'p0 is the point on segment1; p1 is the point on segment2'
    r21=(a1-a0)
    r43=(b1-b0)
    r13=(a0-b0)
    k = [[dot(r21,r21),-dot(r21,r43)],[dot(r43,r21),-dot(r43,r43)]]
    k = array(k)
    f = [-dot(r21, r13),-dot(r43,r13)]
    f = array(f)
    aa=cross(r21,r43)
    if sqrt(dot(aa,aa))<=1*10**(-10):
        alpha = 0.
        beta = f[1]/k[1][1]
        F1 = ((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta * b1))
        distance1 = sqrt(dot(F1,F1))
        alpha = 1
        beta = f[1]/k[1][1]
        F2 =((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta*b1))
        distance2 = sqrt(dot(F2,F2))
        alpha = f[0]/k[0][0]
        beta = 0
        F3 = ((1-alpha)*a0 + alpha*a1 - ((1-beta)*b0 + beta*b1))
        distance3 = sqrt(dot(F3,F3))
        alpha = f[0]/k[0][0]
        beta = 1.
        F4 =((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta*b1))
        distance4 = sqrt(dot(F4,F4))
        distance = min(distance1, distance2, distance3, distance4)
    else:
        [alpha, beta] = linalg.solve(k,f)
        F =((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta*b1))
        if (0<alpha<1 and 0<beta<1):
            distance=sqrt(dot(F,F))
        else:
            alpha=0
            beta=0
            F1=((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta*b1))
            distance1=sqrt(dot(F1,F1))
            alpha=0.
            beta=1.
            F2=((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta*b1))
            distance2=sqrt(dot(F2,F2))
            alpha=1.
            beta=0.
            F3=((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta*b1))
            distance3=sqrt(dot(F3,F3))
            alpha =1.
            beta = 1.
            F4 =((1-alpha)*a0+alpha*a1-((1-beta)*b0+beta*b1))
            distance4=sqrt(dot(F4,F4))
            distance=min(distance1,distance2,distance3,distance4)
    p0=(1-alpha)*a0+alpha*a1
    p1=(1-beta)*b0+beta*b1
    return p0,p1,distance