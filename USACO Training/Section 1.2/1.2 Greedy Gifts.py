"""
ID: pranjal16
LANG: PYTHON3
TASK: gift1
"""

filein = open('gift1.in','r')
fileout = open('gift1.out','w')

inlist = filein.readlines()

NP = int(inlist[0].strip())
nameValueDict = {}
namesInOrder = inlist[1:NP+1].copy()

for i in inlist[1:NP+1]:
    nameValueDict[i.strip()] = 0

del inlist[1:NP+1]

while len(inlist) > 1:
    giverName = inlist[1].strip()
    donation = inlist[2].split()
    if int(donation[1]) == 0:
        del inlist[1:3]
        continue
    moneyToEach = int(donation[0])//int(donation[1])
    for j in inlist[3:int(donation[1])+3]:
        nameValueDict[j.strip()] += moneyToEach
    nameValueDict[giverName] -= int(donation[1])*moneyToEach
    del inlist[1:int(donation[1])+3]

for name in namesInOrder:
    fileout.write(name.strip() + ' ' + str(nameValueDict[name.strip()])+'\n')

filein.close()
fileout.close()
