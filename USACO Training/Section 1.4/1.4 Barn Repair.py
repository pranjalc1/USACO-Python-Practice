'''
ID: pranjal16
LANG: PYTHON3
TASK: barn1
'''

filein = open('barn1.in','r')
fileout = open('barn1.out','w')

text = filein.readlines()
MSC = text[0].split()

for n in range(3):
    MSC[n] = int(MSC[n])

for n in range(1,MSC[2]+1):
    text[n] = int(text[n].strip())

text[0] = 0

filein.close()

damaged = text[:]

notdamaged = []
notdamagedgroups = []
stall = 1
newlist = []

while stall <= MSC[1]:
    if stall in damaged:
        if len(newlist) != 0:
            notdamagedgroups.append(newlist)
            newlist = []
    elif stall == MSC[1]:
        newlist.append(stall)
        notdamaged.append(stall)
        notdamagedgroups.append(newlist)
    else:
        newlist.append(stall)
        notdamaged.append(stall)
    stall += 1

notdamagedgroups.sort(key=lambda x:-len(x))
print(notdamagedgroups)

stall = 1
newlist = []
damagedgroups = 0

while stall <= MSC[1]:
    if stall in notdamaged:
        if len(newlist) != 0:
            damagedgroups += 1
            newlist = []
    elif stall == MSC[1]:
        damagedgroups += 1
    else:
        newlist.append(stall)
    stall += 1

numboards = 1
boarded = MSC[1]

while numboards < MSC[0] and numboards < damagedgroups:
    n = len(notdamagedgroups[0])
    if (1 not in notdamagedgroups[0]) and (MSC[1] not in notdamagedgroups[0]):
        numboards += 1
    boarded -= n
    del notdamagedgroups[0]
    print(boarded)

for group in notdamagedgroups:
    if 1 in group or MSC[1] in group:
        boarded -= len(group)

fileout.write(str(boarded) + '\n')
fileout.close()
