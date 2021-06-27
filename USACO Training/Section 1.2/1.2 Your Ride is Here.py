"""
ID: pranjal16
LANG: PYTHON3
TASK: ride
"""
filein = open('ride.in','r')
fileout = open('ride.out','w')

totalValueTop = 1
totalValueBottom = 1

inlist = filein.readlines()

for letter in inlist[0][:-1]:
    totalValueTop *= (ord(letter)-64)

for letter in inlist[1][:-1]:
    totalValueBottom *= (ord(letter)-64)

if totalValueTop%47 == totalValueBottom%47:
    fileout.write('GO\n')
else:
    fileout.write('STAY\n')

filein.close()
fileout.close()
