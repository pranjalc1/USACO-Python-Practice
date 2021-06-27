'''
ID: pranjal16
LANG: PYTHON3
TASK: wormhole
'''

filein = open('wormhole.in','r')
fileout = open('wormhole.out','w')

text = filein.readlines()
N = int(text[0].strip())
del text[0]

coords = text[:]
coorddict = {}

for i in range(N):
    coords[i] = coords[i].split()
    for j in range(2):
        coords[i][j] = int(coords[i][j])
    coorddict[i+1] = coords[i]

pairings = []
i = N
Nset = set(range(1,N+1))

while len(pairings)==0 or len(pairings[0]) != N:
    if len(pairings) == 0:
        for j in range(2,N+1):
            pairings.append({1:j,j:1})
    else:
        prevpairs = pairings[:]
        pairings = []
        for pairing in prevpairs:
            remaining = list(Nset - set(pairing.values()))
            num = len(remaining)
            for j in range(1,num):
                newpairing = pairing.copy()
                newpairing[remaining[0]] = remaining[j]
                newpairing[remaining[j]] = remaining[0]
                pairings.append(newpairing)

# Inspired by Brian Dean's solution to this problem
for pairing in range(len(pairings)):
    pairings[pairing][0] = 0

coordtoright = {}
for coord1 in coorddict:
    mindistance = [0,10000000000000000]
    for coord2 in coorddict:
        if coorddict[coord1][1] == coorddict[coord2][1] \
           and coorddict[coord2][0] > coorddict[coord1][0] and \
           coorddict[coord2][0]-coorddict[coord1][0] < mindistance[1]:
            mindistance = [coord2,coorddict[coord2][0]-coorddict[coord1][0]]
    coordtoright[coord1] = mindistance[0]

coordtoright[0] = 0

numsolutions = 0
for pairing in pairings:
    cycles = 0
    for start in range(1,N+1):
        i = 1
        position = start
        while i <= N:
            position = pairing[coordtoright[position]]
            i += 1
        if position != 0:
            cycles += 1
    if cycles > 0:
        numsolutions += 1
    

fileout.write(str(numsolutions) + '\n')
fileout.close()
