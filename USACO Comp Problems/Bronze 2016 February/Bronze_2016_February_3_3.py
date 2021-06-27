filein = open('balancing.in','r')
fileout = open('balancing.out','w')

text = filein.readlines()
N = int(text.pop(0).split()[0])
cows = [[int(i) for i in cow.split()] for cow in text]
xcoords = [cow[0] for cow in cows]
ycoords = [cow[1] for cow in cows]

filein.close()

xcoords.sort()
ycoords.sort()

xcoords = list(set(xcoords))
ycoords = list(set(ycoords))

def findm(a,b):
    '''finds m for a certain a and b'''
    q1 = 0
    q2 = 0
    q3 = 0
    for cow in cows:
        if cow[0] > a and cow[1] > b:
            q1 += 1
        elif cow[0] < a and cow[1] > b:
            q2 += 1
        elif cow[0] < a and cow[1] < b:
            q3 += 1
    q4 = N - q1 - q2 - q3
    return max(q1,q2,q3,q4)

xposs = [xcoords[0]-1] + [coord + 1 for coord in xcoords]
yposs = [ycoords[0]-1] + [coord + 1 for coord in ycoords]

possab = []
for a in xposs:
    for b in yposs:
        possab.append([a,b])

answer = N
for poss in possab:
    possm = findm(poss[0],poss[1])
    if possm < answer:
        answer = possm

fileout.write(str(answer) + '\n')

fileout.close()
