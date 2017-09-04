import os
import shutil
import numpy as np
totalstep=200
step=200
title = 'id, x coord, y coord, z coord, sigma_xx, sigma_yy,sigma_zz,sigma_xy,sigma_xz,sigma_yz\n'
list=[[]]*(totalstep/step+1)
for i in range(0,totalstep+step,step):
    name=str(i)
    csvfile=name.zfill(5)+'.csv'
    if os.path.exists(csvfile):
        os.remove(csvfile)
for i in range(0,totalstep+step,step):
    file='dump.HEA.equil.'+str(i)
    name=str(i)
    newfile=name.zfill(5)+'.csv'
    f=open(file)
    newfile=open(newfile,'a')
    newfile.write(title)
    list[i/step]=[]
    for line in f.readlines()[9:]:
        row=line.split()
        newfile.write((row[0]+','+row[1]+','+row[2]+','+row[3]+','
                   +row[4]+','+row[5]+','+row[6]+','+
                       row[7]+','+row[8]+','+row[9]+'\n'))

        list[i/step].append(row[0]);list[i/step].append(row[1])
        list[i/step].append(row[2]);list[i/step].append(row[3])
        list[i/step].append(row[4]);list[i/step].append(row[5])
        list[i/step].append(row[6]);list[i/step].append(row[7])
        list[i/step].append(row[8]);list[i/step].append(row[9])

    f.close()
    newfile.close()

summary=([[]]*(totalstep/step+1))
for i in range(0,totalstep/step+1,1):
    summary[i]=[]
    for j in range(0,len(list[0]),1):
        summary[i].append(float(list[i][j]))


results=np.array(summary).sum(axis=0)/(totalstep/step+1)


sumfile='sum.csv'
if os.path.exists(sumfile):
    os.remove(sumfile)
title = 'id, x coord, y coord, z coord, sigma_xx, sigma_yy,sigma_zz,sigma_xy,sigma_xz,sigma_yz\n'
outfile=open(sumfile,'a')
outfile.write(title)
for i in range(0,len(list[0]),10):
    outfile.write(str(int(results[i]))+','+str((results[i+1]))+','+str((results[i+2]))+
                  ','+str((results[i+3]))+','+str((results[i+4]))+','+
                  str((results[i+5]))+','+str((results[i+6]))+','+str((results[i+7]))+
                  ','+str((results[i+8]))+','+str((results[i+9]))+'\n')


outfile.close()

csvoutfile='csv/'+'sum'+'.csv'

if os.path.exists(csvoutfile):
    os.remove(csvoutfile)
if os.path.exists('sum.csv'):
    shutil.move('sum.csv', "csv")