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

if N % 2 == 0:
    xposs = xcoords[N//2-1:N//2+1]
    yposs = ycoords[N//2-1:N//2+1]
    xposs = xposs[0]-1
    yposs = yposs[0]-1
else:
    xposs = xcoords[N//2]-1
    yposs = ycoords[N//2]-1

answer = 100
for a in range(xposs-2,xposs+5,2):
    for b in range(yposs-2,yposs+5,2):
        possm = findm(a,b)
        if possm < answer:
            answer = possm

fileout.write(str(answer) + '\n')

fileout.close()
