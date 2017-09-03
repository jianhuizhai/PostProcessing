import os
os.remove('step0.csv')
f=open('dump.HEA.equil.0')
# f.read()
newfile = open('step0.csv', 'a')
title = 'id, x coord, y coord, z coord, sigma_xx, sigma_yy,sigma_zz,sigma_xy,sigma_xz,sigma_yz\n'
newfile.write(title)
# rowlist=[]

for line in f.readlines()[9:]:
# newfile.write(f.read().replace(' ', ','))
    # print(line)
    # f.close()
    collist = line.split()
    print('collist=',collist)
    newfile.write((collist[0]+','+collist[1]+','+collist[2]+','+collist[3]+','
                   +collist[4]+','+collist[5]+','+collist[6]+','+
                   collist[7]+','+collist[8]+','+collist[9]+'\n'))
f.close()
newfile.close()