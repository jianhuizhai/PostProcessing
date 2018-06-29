import os
import shutil
totalstep=1200
step=200
if not os.path.exists("csv"):
    os.makedirs("csv")
title = 'id, x coord, y coord, z coord, sigma_xx, sigma_yy,sigma_zz,sigma_xy,sigma_xz,sigma_yz\n'
# judge the files exist in csv folder or not, if they exist, delete the files.
for i in range(0,totalstep+step,step):
    name=str(i)
    csvfile='csv/'+name.zfill(5)+'.csv'
    print(csvfile)
    if os.path.exists(csvfile):
        os.remove(csvfile)

# generate series  of csv files
for i in range(0,totalstep+step,step):
    file='dump.HEA.equil.'+str(i)
    name=str(i)
    newfile=name.zfill(5)+'.csv'
    print('newfile=',newfile)
    print('file=',file)
    f=open(file)
    newfile=open(newfile,'a')
    newfile.write(title)
    for line in f.readlines()[9:]:
        row=line.split()
        newfile.write((row[0]+','+row[1]+','+row[2]+','+row[3]+','
                   +row[4]+','+row[5]+','+row[6]+','+
                       row[7]+','+row[8]+','+row[9]+'\n'))
    f.close()
    newfile.close()
# move the csv files to csv folder
for i in range(0,totalstep+step,step):
    name=str(i)
    movefile = name.zfill(5) + '.csv'
    print('movefile=',movefile)
    if os.path.exists(movefile):
        shutil.move(movefile,"csv")
