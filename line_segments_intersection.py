def line_segments_intersection(seg1,seg2,x,y):
    # seg1 is line segment 1, it contains the nodes of line segment such as [1,2]
    # seg2 is line segment 2, it contains the nodes of line segment such as [3,4]
    # x is x coordinates of all the nodes; y is y coordinates of all nodes
    # x1,y1 and x2,y2 are coordinates of nodes of one line segment;
    # x3,y3 and x4,y4 are coordinates of nodes of another line segment.
    x1=x[seg1[0]];y1=y[seg1[0]]
    x2=x[seg1[1]];y2=y[seg1[1]]
    x3=x[seg2[0]];y3=y[seg2[0]]
    x4=x[seg2[1]];y4=y[seg2[1]]
    p1q1=[x3-x1,y3-y1]
    q2q1=[x3-x4,y3-y4]
    p2q1=[x3-x2,y3-y2]
    q1p1=[x1-x3,y1-y3]
    p2p1=[x1-x2,y1-y2]
    q2p1=[x1-x4,y1-y4]
    if((cross_product(p1q1,q2q1)*cross_product(p2q1,q2q1)<=0)
            and (cross_product(q1p1,p2p1)*cross_product(q2p1,p2p1)<=0)):
        print('two line segments intersection')
def cross_product(A,B):
    'calculate a1*b2-a2*b1'
    product=A[0]*B[1]-A[1]*B[0]
    return product