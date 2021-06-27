filein = open('hoofball.in','r')
fileout = open('hoofball.out','w')

text = filein.readlines()
N = int(text.pop(0).strip())
coords = [int(i) for i in text[0].split()]
coords.sort()

filein.close()

def check(cow):
    '''checks the cows that passing a ball to cow will give'''
    listofcows = [cow]
    while True:
        if cow == 0:
            cow += 1
        elif cow == N-1:
            cow -= 1
        else:
            left = coords[cow-1]
            right = coords[cow+1]
            middle = coords[cow]
            if abs(left-middle) <= abs(right-middle):
                cow -= 1
            else:
                cow += 1
        if cow not in listofcows:
            listofcows.append(cow)
        else:
            listofcows.sort()
            return listofcows

circles = []
for cow in range(N):
    circles.append(check(cow))

dones = [[0 for i in acheck] for acheck in circles]
lengths = [len(acheck) for acheck in circles]

numcows = 0
done = [0 for i in range(N)]

while 0 in done:
    for cow in range(N):
        for apass in range(len(circles[cow])):
            if done[circles[cow][apass]]:
                dones[cow][apass] = 1
        lengths[cow] = dones[cow].count(0)
    maximum = max(lengths)
    newcow = lengths.index(maximum)
    for cow in circles[newcow]:
        done[cow] = 1
    numcows += 1

fileout.write(str(numcows) + '\n')
fileout.close()
